📨 Domain Message
===

1. **How does a domain send a request to another domain?**

    ![](<.📎 Assets/📨 Comms.png>)

    For two [domains 👥](<../$ 👥 Domains/00 👥 Domain.md>) to communicate with one another (e.g., for `any-sender.com` to send a message to `any-receiver.com`), the following steps are required.

    | # |  Step
    |-|-
    | 1 | As a pre-condition for sending messages, a sender needs to generate a an asymmetric key-pair, then register the public key of the key-pair in its DNS record following the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) protocol used by e-mail servers.
    | 2 | When sending a message, the sender wraps the message in an JSON envelope, signs the envelope with the private key of the mentioned key-pair, and sends the signed message via HTTPS POST to the receiver's well-known inbox API endpoint (e.g., `https://nlweb.any-receiver.com/inbox`). 
    | 3 | When receiving the signed message, the receiver reads the public key from the sender's [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>), confirms if the sender is using DNSSEC, and confirms if the message's signature matches the sender's public key.


    ---
    <br/>

1. **What does a domain message look like?**

    Messages from [domains 👥](<../$ 👥 Domains/00 👥 Domain.md>) are sent in JSON envelopes similar to email messages. 
    
    * The [Schema 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) is defined at [`nlweb.org/MSG 🧩`](<../../../7 🧩 Codes/$/🧩 MSG code.md>).
    * Consider the the following example, converted from JSON to YAML for readability.

    ```yaml
    🤝: nlweb.org/MSG:1.0

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

    The following properties are a summary of the schema at [`nlweb.org/MSG 🧩`](<../../../7 🧩 Codes/$/🧩 MSG code.md>).

    |Property| Description
    |-|-
    | `🤝` | The versioned [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) of the envelope.
    | `From` | The name of the [domain 👥](<../$ 👥 Domains/00 👥 Domain.md>) who sent the message.
    | `To`| The name of the [domain 👥](<../$ 👥 Domains/00 👥 Domain.md>) for whom the message is intended.
    | `Correlation`| The unique ID in the sender, for deduping.
    | `Timestamp`| The date and time of the message, in UTC format.
    | `Subject`| The method to be executed on the receiver.
    | `Body`| The content inside the envelope.
    | `Hash`| The canonical hash of the envelope's header and body.
    | `Signature`| The signature of the envelope using the sender's private key.
    | `DKIM`| The name of the corresponding public key in the sender's [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>).

    ---
    <br/>


1. **How do receiver domains handle upgraded schema versions?**

    An NLWeb envelop contains a [Schema Code 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) that allows receivers to support multiple versions concurrently, handling incoming envelopes differently depending on its version;
    - e.g., `🤝: nlweb.org/MSG:1.0`
    - Envelopes with unsupported versions are discarded.

    ---
    <br/>


1. **How do receiver domains know who sent a message?**

    An NLWeb envelope resembles an email message, containing a `Header` and a `Body`. 
    - The header contains the sender’s domain name (e.g., `any-sender.com`) and the receiver’s domain name (e.g., `any-receiver.com`), as well as other metadata. 
    - Receivers discard envelopes not intended to them.

    ---
    <br/>

1. **How do receiver domains prevent sender impersonation attacks?**

    NLWeb domains implement the ubiquitous [DKIM (rfc6376) protocol 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) used by email servers to verify envelopes received from other domains. 
    
    - Sender domains hash their envelopes with JSON Canonicalization Scheme (rfc8785) and sign them with their private half of the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key-pair. 
    
    - Receiver domains look up the public half of the sender’s [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key-pair to verify the signature of incoming envelopes. The receiver expects to find the sender’s public key in DKIM format in a DNS entry named “nlweb” (e.g., `nlweb._domainkey.any-sender.com`). 
    
    - The envelope is discarded if the sender’s [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) is not correctly implemented, or the sender’s public key is unable to verify the signature in the envelope.

    ---
    <br/>

1. **How do receiver domains prevent DNS spoofing attacks?**

    When getting the sender’s [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) public key, receiver domains check if DNSSEC is implemented on the sender’s domain;
    - if not implemented, the envelope is discarded.

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
    - e.g., `Hello@Host` refers to the [Hello 🐌 method](<../../../6 🅰️ APIs/50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>) in the [Host 🤗 domain role](<../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>).
    - The possible `Subject` values are defined by the APIs implemented by [domain Roles 🎭](<../$ 👥 Domains/00 👥 Domain.md>).
    - Receivers discard envelopes with unexpected subjects.

    ---
    <br/>
   
1. **What is the signature for?**

    Senders sign the header and body of envelopes with [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) private key,
    - [domains 👥](<../$ 👥 Domains/00 👥 Domain.md>) verify incoming [domain 👥](<../$ 👥 Domains/00 👥 Domain.md>) messages with the sender's [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) public key,
    - and [Broker 🤵 domains](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) verify incoming [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) messages with the their pre-shared public key.
    
    ---
    <br/>

1. **How to create the canonical version of the envelope?**
   
    To create a canonical version of the envelope:
    1. create an object with just {header,body} content;
    2. compact the content with [JSON Canonicalization Scheme (JCS) ⤴](https://www.rfc-editor.org/rfc/rfc8785).

    ---
    <br/>

1. **How to create the canonical hash with OpenSSL?**
   
    To generate the hash with OpenSSL, prepare the following file:
    - `canonical.json`: a canonical representation of {header,body}.
  
    Then run: 
    * `$ cat canonical.json | openssl dgst -sha256 > hash.txt`
    * `$ truncate -s -1 hash.txt`
    * `$ cat hash.txt`

    ---
    <br/>


1. **How to create a signature with OpenSSL?**

    To create a signature with OpenSSL, first prepare the following files:
      - `canonical.json`: a canonical representation of {header,body};
      - `private.pem`: the private signature of the [domain 👥](<../$ 👥 Domains/00 👥 Domain.md>).
  
    Then run the following commands on a terminal: 
    * `$ openssl dgst -sha256 -sign private.pem -out signature.sha1 canonical.json`
    * `$ openssl base64 -A -in signature.sha1 -out signature.txt`
    * `$ cat signature.txt`

    ---
    <br/>

1. **How to validate a signature with OpenSSL?**

    To validate a signature with OpenSSL, first prepare the following files:
    - `signature.txt`: the signature received in a message from another [domain 👥](<../$ 👥 Domains/00 👥 Domain.md>);
    - `canonical.json`: a canonical representation of the received {header,body};
    - `public.pem`: the public key of the sender [domain 👥](<../$ 👥 Domains/00 👥 Domain.md>).
  
    Then run the following commands on a terminal: 
    * $ `openssl enc -d -A -base64 -in signature.txt -out signature.sha1`
    * $ `openssl dgst -sha256 -verify public.pem -signature signature.sha1 canonical.json`

    ---
    <br/>

1. **What are the technical workflows around messages?**

    | Workflow | Description
    |-|-
    | 🚀 Synchronous requests | [Domains 👥](<../$ 👥 Domains/00 👥 Domain.md>) send requests and wait for the immediate response over an HTTPS request.
    | 🐌 Asynchronous messages | [Domains 👥](<../$ 👥 Domains/00 👥 Domain.md>) send fire-and-forget messages and events. Any eventual answer, if expected, will arrive via another asynchronous message.

    ---
    <br/>


1. **How do Synchronous Requests work?**

    ![SyncRequest](<../../../5 ⏩ Flows/30 👥⏩ Domains/.📎 Assets/⚙️🚀 SyncRequest.png>)

    ---
    <br/>

1. **How do Async Messages work?**

    ![AsyncMessage](<../../../5 ⏩ Flows/30 👥⏩ Domains/.📎 Assets/⚙️🐌 AsyncMessage.png>)
    
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


9.  **How do receiver domains reply to incoming messages?**

    In NLWeb, communications are asynchronous to minimize wait times in HTTPS communications and reduce the serverless compute cost of sending outbound messages. 
    
    - Thus, the receiver is expected to store the envelope in a resilient queue and immediately return a successful HTTPS 200 response. 
    
    - The receiver then processes the incoming envelopes asynchronously by consuming them from the queue - it discards invalid envelopes, and replies to valid ones by sending a new envelope to the sender.

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
    | `JSON` | Structured JSON for machine-to-machine payloads, because it's faster and widely supported by cloud providers; e.g.: <br/>• [domain Messages 📨](<01 📨 Domain Message.md>) between any two [domains 👥](<../$ 👥 Domains/00 👥 Domain.md>), <br/>• data sharing between a [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) and a [Consumer 💼](<../../41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) domains, <br/>• payments between a [Payer 💳](<../../50 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) and a [Collector](<../../45 🛠️ Helper domains/30 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) domains.
    | `YAML` | Structured YAML for human-to-machine settings, because it supports comments and it's easier for humans to read, while still supporting schema validations; <br/>• e.g.: [Schema Codes 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) and [domain Manifests 📜](<../44 📜 Manifests/$ 📜 Domain Manifest.md>).
    | `MARKDOWN` | Unstructured MARKDOWN for human-to-LLM instructions, when schema validations are not required; <br/>• e.g., description of products and services by business owners (like a detailed restaurant menu) for user [Curator 🧚 agents](<../../50 🫥 Agents/30 🧚 Curators/$ 🧚🫥 Curator agent.md>) to filter on behalf of users.
    
    ---
    <br/>


1. **How can senders know if receivers discarded messages?**

    When discarding an invalid message, receiver domains send feedback to the sender with the original correlation ID. 
    
    * Sender domains define their [Buffer ⏳ helper domain](<../../45 🛠️ Helper domains/27 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) in the `Identity` section of their [domain Manifest 📜](<../44 📜 Manifests/$ 📜 Domain Manifest.md>).
       * If the `Feedback` property is not defined, then no feedback is given.
       * Domains get of the [Buffer ⏳ helper domain](<../../45 🛠️ Helper domains/27 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) by calling the [Identity@Broker 🚀 request](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/04 👥🚀🕸 Identity.md>).
  
        ```yaml
        🤝: nlweb.org/MANIFEST/ABOUT
        About:
          Name: any-sender.com
          Feedback: any-buffer.com
        ```

    * The feedback is sent via a [Buffer ⏳ helper domain](<../../45 🛠️ Helper domains/27 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) defined by the sender's domain, using the [Feedback@Buffer 🐌 API message](<../../../6 🅰️ APIs/20 ⏳🅰️ Buffer/01 👥🐌⏳ Feedback.md>). 
        ```yaml
        🤝: nlweb.org/MSG:1.0
        Header:
            From: any-receiver.com
            To: any-buffer.com
            Subject: Feedback@Buffer
        Body:
            Correlation: <correlation-uuid>
            Status: Discarded
            Reason: Invalid DKIM signature.
        ```

    ---
    <br/>
