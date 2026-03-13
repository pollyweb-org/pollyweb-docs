# 📨✉️ Message Envelope

> Part of [domain Message 📨](<../📨 Message/📨 Message.md>)

<br/> 


1. **What does a domain message look like?**

    Messages from [domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) are sent in JSON envelopes similar to email messages. 
    
    * The [Schema 🧩](<../../Codes 🧩/🧩 Schema Code.md>) is defined at [`pollyweb.org/MSG 🧩`](<../📨🧩 Message schemas/🧩 MSG.md>).
    * Consider the the following example, converted from JSON to YAML for readability.

    ```yaml
    Header:
        Schema: pollyweb.org/MSG:1.0
        From: any-sender.dom
        To: any-receiver.dom
        Subject: AnyMethod
        Correlation: 125a5c75-cb72-43d2-9695-37026dfcaa48
        Timestamp: 2018-12-10T13:45:00.000Z
        Selector: pk1

    Body: {...}

    Hash: ee6ca2a43ec05d...
    Signature: Lw7sQp6zkOGyJ+OzGn+B...
    ```

    ---
    <br/>

1. **What is contained in a domain message envelope?**

    The following properties are a summary of the schema at [`pollyweb.org/MSG 🧩`](<../📨🧩 Message schemas/🧩 MSG.md>).

    |Property| Description
    |-|-
    | `Schema` | The versioned [Schema 🧩](<../../Codes 🧩/🧩 Schema Code.md>) of the envelope.
    |`From`| The name of the [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) who sent the message.
    |`To`| The name of the [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) for whom the message is intended.
    | `Correlation`| The unique ID in the sender, for deduping.
    | `Timestamp`| The date and time of the message, in UTC format.
    | `Subject`| The method to be executed on the receiver.
    | `Body`| The content inside the envelope.
    | `Hash`| The canonical hash of the envelope's header and body.
    | [`Signature`](<Signatures 🔏.md>)| The signature of the envelope (except the body) using the sender's private key.
    | `Selector` | The name of the corresponding public key in the sender's DKIM DNS records.

    ---
    <br/>


1. **How do receiver domains handle upgraded schema versions?**

    An PollyWeb envelop contains a [Schema 🧩](<../../Codes 🧩/🧩 Schema Code.md>) that allows receivers to support multiple versions concurrently, handling incoming envelopes differently depending on its version;
    - e.g., `Header.Schema: pollyweb.org/MSG:1.0`
    - Envelopes with unsupported versions are discarded.

    ---
    <br/>


1. **How do receiver domains know who sent a message?**

    An PollyWeb envelope resembles an email message, containing a `Header` and a `Body`. 
    - The header contains the sender’s domain name (e.g., `any-sender.dom`) and the receiver’s domain name (e.g., `any-receiver.dom`), as well as other metadata. 
    - Receivers discard envelopes not intended to them.

    ---
    <br/>

1. **How do receiver domains prevent replay attacks?**

    An PollyWeb envelop contains the sender’s `Timestamp` in UTC format.
    - Receivers discard envelopes with a timestamp outside accepted time boundaries. 
    
    An envelope also contains a `Correlation` UUID.
    - This uniquely identifies the outbound message in the sender’s domain.
    - Receivers discard envelopes with duplicate incoming correlations within accepted time boundaries.

    ---
    <br/>

1. **How do receiver domains differentiate methods?**

    An PollyWeb envelop contains a `Subject` that identifies how the receiver should handle the message:
    - e.g., `Hello@Host` refers to the [Hello 🐌 method](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) in the [Host 🤗 domain role](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).
    - The possible `Subject` values are defined by the APIs implemented by [Roles 🎭](<../../../40 👥 Domains/👥 Domain/👥🎭 Domain Role.md>).
    - Receivers discard envelopes with unexpected subjects.

    ---
    <br/>
   


1. **Why are Messages in JSON while Manifests are in YAML?** 

    PollyWeb uses JSON, YAML, or MARKDOWN depending on the requirements.

    | Format | Rational
    |-|-
    | `JSON` | Structured JSON for machine-to-machine payloads, because it's faster and widely supported by cloud providers; e.g.: <br/>• [domain Messages 📨](<../📨 Message/📨 Message.md>) between any two [domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>), <br/>• data sharing between a [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) and a [Consumer 💼](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) domains, <br/>• payments between a [Payer 💳](<../../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) and a [Collector 🏦](<../../../45 🤲 Helper domains/Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>) domains.
    | `YAML` | Structured YAML for human-to-machine settings, because it supports comments and it's easier for humans to read, while still supporting schema validations; <br/>• e.g.: [Schema Codes 🧩](<../../Codes 🧩/🧩 Schema Code.md>) and [domain Manifests 📜](<../../Manifests 📜/📜 Manifest/📜 Manifest.md>).
    | `MARKDOWN` | Unstructured MARKDOWN for human-to-LLM instructions, when schema validations are not required; <br/>• e.g., description of products and services by business owners (like a detailed restaurant menu) for user [Curator 🧚 agents](<../../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) to filter on behalf of users.
    
    ---
    <br/>
