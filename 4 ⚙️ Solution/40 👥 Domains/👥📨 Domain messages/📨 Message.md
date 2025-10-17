📨 Domain Message
===

1. **How does a domain send a request to another domain?**

    ![](<.📎 Assets/📨 Domain Message.png>)

    For two [domains 👥](<../👥 Domains/👥 Domain.md>) to communicate with one another (e.g., for `any-sender.com` to send a message to `any-receiver.com`), the following steps are required.

    | # |  Step
    |-|-
    | 1 | As a pre-condition for sending messages, a sender needs to generate a an asymmetric key-pair, then register the public key of the key-pair in its DNS record following the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) protocol used by e-mail servers.
    | 2 | When sending a message, the sender wraps the message in an JSON envelope, signs the envelope with the private key of the mentioned key-pair, and sends the signed message via HTTPS POST to the receiver's well-known inbox API endpoint (e.g., `https://nlweb.any-receiver.com/inbox`). 
    | 3 | When receiving the signed message, the receiver reads the public key from the sender's [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>), confirms if the sender is using DNSSEC, and confirms if the message's signature matches the sender's public key.


    ---
    <br/>



1. **What are the technical workflows around messages?**

    | Workflow | Description
    |-|-
    | 🚀 [Synchronous requests](<../👥📨 Domain Messages/📨⏩ Message flows/Send Sync 🚀.md>) | [Domains 👥](<../👥 Domains/👥 Domain.md>) send requests and wait for the immediate response over an HTTPS request.
    | 🐌 [Asynchronous messages](<../👥📨 Domain Messages/📨⏩ Message flows/Send Async 🐌.md>) | [Domains 👥](<../👥 Domains/👥 Domain.md>) send fire-and-forget messages and events. Any eventual answer, if expected, will arrive via another asynchronous message.

    ---
    <br/>



1. **Is this compatible with W3C DIDcomm?**

    No. 
    
    - W3C DIDcomm is a protocol specific for  [W3C distributed identities (DIDs) 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>). 
    
    - NLWeb advocates for fully offline verification of credentials presented via a QR code, where consumer domains can use cached public keys of issuer domains to verify the signature in the QR 
        - this requires a small footprint of all-encompassed data in the QR. 
    
    - Conversely, W3C advocates for Verifiable Credentials (VCs) supported by DIDs that can be printed into a QR code just like a URL;
        - the DID key needs to be translated into a DID Document by an online key-value database before the consumer domain can read and validate its content;
        - because of this limitation, NLWeb does not implement DIDs.

    ---
    <br/>

1. **How do sender domains prevent man-in-the-middle attacks?**

    By using HTTPS POST requests, sender domains ensure outbound messages are encrypted, and rely on trusted Certificate Authorities (CAs) to validate the TLS certificate of the receiver. 
    - By using a well-known URL prefix plus the receiver’s domain, sender domains rely only on DNS for network discovery.

    ---
    <br/>



1. **Can messages be compressed?** 

    HTTPS already handles compression:
    - `HTTP/2` and `HTTP/3` compress the header;
    - `Accept-Encoding` with `br, gzip` compresses the body. 

    ---
    <br/>

1. **With HTTPS compression, how is BREACH prevented?** 

    BREACH is a category of vulnerabilities where, to be vulnerable, a web application must:     
    * be served from a server that uses HTTP-level compression,
    * reflect user-input in HTTP response bodies,
    * and reflect a secret (such as a CSRF token) in HTTP response bodies.
  
    Additionally, while not strictly a requirement, the attack is helped greatly by responses that remain mostly the same (modulo the attacker's guess). 
    * This is because the difference in size of the responses measured by the attacker can be quite small. 
    * Any noise in the side-channel makes the attack more difficult (though not impossible). 

    BREACH was assessed for NLWeb, and it was determined that the protocol is not exposed to these specific risks.

    ---
    <br/>


1. **Why are Messages in JSON while Manifests are in YAML?** 

    NLWeb uses JSON, YAML, or MARKDOWN depending on the requirements.

    | Format | Rational
    |-|-
    | `JSON` | Structured JSON for machine-to-machine payloads, because it's faster and widely supported by cloud providers; e.g.: <br/>• [domain Messages 📨](<📨 Message.md>) between any two [domains 👥](<../👥 Domains/👥 Domain.md>), <br/>• data sharing between a [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) and a [Consumer 💼](<../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) domains, <br/>• payments between a [Payer 💳](<../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) and a [Collector](<../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) domains.
    | `YAML` | Structured YAML for human-to-machine settings, because it supports comments and it's easier for humans to read, while still supporting schema validations; <br/>• e.g.: [Schema Codes 🧩](<../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) and [domain Manifests 📜](<../👥📜 Domain Manifests/📜 Manifest.md>).
    | `MARKDOWN` | Unstructured MARKDOWN for human-to-LLM instructions, when schema validations are not required; <br/>• e.g., description of products and services by business owners (like a detailed restaurant menu) for user [Curator 🧚 agents](<../../50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) to filter on behalf of users.
    
    ---
    <br/>


1. **How can senders know if receivers discarded messages?**

    When discarding an invalid message, receiver domains send feedback to the sender with the original correlation ID. 
    
    * Sender domains define their [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) in the `Identity` section of their [domain Manifest 📜](<../👥📜 Domain Manifests/📜 Manifest.md>).
       * If the `Feedback` property is not defined, then no feedback is given.
       * Domains get of the [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) by calling the [Identity@Broker 🚀 request](<../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>).
  
        ```yaml
        🤝: nlweb.dom/MANIFEST/ABOUT
        About:
          Name: any-sender.com
          Feedback: any-buffer.dom
        ```

    * The feedback is sent via a [Buffer ⏳ helper domain](<../../45 🤲 Helper domains/Buffers ⏳/⏳🤲 Buffer helper.md>) defined by the sender's domain, using the [Feedback@Buffer 🐌 API message](<../../45 🤲 Helper domains/Buffers ⏳/⏳🅰️ Buffer methods/👥🐌⏳ Feedback.md>). 
        ```yaml
        🤝: nlweb.dom/MSG:1.0
        Header:
            From: any-receiver.com
            To: any-buffer.dom
            Subject: Feedback@Buffer
        Body:
            Correlation: <correlation-uuid>
            Status: Discarded
            Reason: Invalid DKIM signature.
        ```

    ---
    <br/>
