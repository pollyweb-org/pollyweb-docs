# 📨✉️ Message Envelope

> Part of [domain Message 📨](<../📨 Message.md>)

<br/> 


1. **What does a domain message look like?**

    Messages from [domains 👥](<../../../40 👥 Domains/👥 Domain.md>) are sent in JSON envelopes similar to email messages. 
    
    * The [Schema 🧩](<../../Schema Codes 🧩/🧩 Schema Code.md>) is defined at [`nlweb.dom/MSG 🧩`](<../📨🧩 Message schemas/🧩 MSG.md>).
    * Consider the the following example, converted from JSON to YAML for readability.

    ```yaml
    🤝: nlweb.dom/MSG:1.0

    Header:
        From: any-sender.com
        To: any-receiver.com
        Correlation: 125a5c75-cb72-43d2-9695-37026dfcaa48
        Timestamp: 2018-12-10T13:45:00.000Z
        Subject: AnyMethod
        DKIM: pk1

    Body: {...}

    Hash: ee6ca2a43ec05d...
    Signature: Lw7sQp6zkOGyJ+OzGn+B...
    ```

    ---
    <br/>

1. **What is contained in a domain message envelope?**

    The following properties are a summary of the schema at [`nlweb.dom/MSG 🧩`](<../📨🧩 Message schemas/🧩 MSG.md>).

    |Property| Description
    |-|-
    | `🤝` | The versioned [Schema Code 🧩](<../../Schema Codes 🧩/🧩 Schema Code.md>) of the envelope.
    | `From` | The name of the [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) who sent the message.
    | `To`| The name of the [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) for whom the message is intended.
    | `Correlation`| The unique ID in the sender, for deduping.
    | `Timestamp`| The date and time of the message, in UTC format.
    | `Subject`| The method to be executed on the receiver.
    | `Body`| The content inside the envelope.
    | `Hash`| The canonical hash of the envelope's header and body.
    | [`Signature`](<Signatures 🔏.md>)| The signature of the envelope using the sender's private key.
    | [`DKIM`](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>)| The name of the corresponding public key in the sender's [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>).

    ---
    <br/>


1. **How do receiver domains handle upgraded schema versions?**

    An NLWeb envelop contains a [Schema Code 🧩](<../../Schema Codes 🧩/🧩 Schema Code.md>) that allows receivers to support multiple versions concurrently, handling incoming envelopes differently depending on its version;
    - e.g., `🤝: nlweb.dom/MSG:1.0`
    - Envelopes with unsupported versions are discarded.

    ---
    <br/>


1. **How do receiver domains know who sent a message?**

    An NLWeb envelope resembles an email message, containing a `Header` and a `Body`. 
    - The header contains the sender’s domain name (e.g., `any-sender.com`) and the receiver’s domain name (e.g., `any-receiver.com`), as well as other metadata. 
    - Receivers discard envelopes not intended to them.

    ---
    <br/>

1. **How do receiver domains prevent replay attacks?**

    An NLWeb envelop contains the sender’s `Timestamp` in UTC format.
    - Receivers discard envelopes with a timestamp outside accepted time boundaries. 
    
    An envelope also contains a `Correlation` UUID.
    - This uniquely identifies the outbound message in the sender’s domain.
    - Receivers discard envelopes with duplicate incoming correlations within accepted time boundaries.

    ---
    <br/>

1. **How do receiver domains differentiate methods?**

    An NLWeb envelop contains a `Subject` that identifies how the receiver should handle the message:
    - e.g., `Hello@Host` refers to the [Hello 🐌 method](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) in the [Host 🤗 domain role](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>).
    - The possible `Subject` values are defined by the APIs implemented by [domain Roles 🎭](<../../../40 👥 Domains/👥 Domain.md>).
    - Receivers discard envelopes with unexpected subjects.

    ---
    <br/>
   


1. **Why are Messages in JSON while Manifests are in YAML?** 

    NLWeb uses JSON, YAML, or MARKDOWN depending on the requirements.

    | Format | Rational
    |-|-
    | `JSON` | Structured JSON for machine-to-machine payloads, because it's faster and widely supported by cloud providers; e.g.: <br/>• [domain Messages 📨](<../📨 Message.md>) between any two [domains 👥](<../../../40 👥 Domains/👥 Domain.md>), <br/>• data sharing between a [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) and a [Consumer 💼](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) domains, <br/>• payments between a [Payer 💳](<../../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) and a [Collector 🏦](<../../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) domains.
    | `YAML` | Structured YAML for human-to-machine settings, because it supports comments and it's easier for humans to read, while still supporting schema validations; <br/>• e.g.: [Schema Codes 🧩](<../../Schema Codes 🧩/🧩 Schema Code.md>) and [domain Manifests 📜](<../../Manifests 📜/📜 Manifest.md>).
    | `MARKDOWN` | Unstructured MARKDOWN for human-to-LLM instructions, when schema validations are not required; <br/>• e.g., description of products and services by business owners (like a detailed restaurant menu) for user [Curator 🧚 agents](<../../../50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) to filter on behalf of users.
    
    ---
    <br/>

