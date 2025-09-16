📨 Domain Communication FAQ
===

1. **How does a domain send a request to another domain?**

    ![](<.📎 Assets/📨 Comms.png>)

    For two [domains 👥](<../44 📜 Manifests/00 👥 Domain.md>) to communicate with one another (e.g., for `any-sender.com` to send a message to `any-receiver.com`), the following steps are required.

    | # |  Step
    |-|-
    | 1 | As a pre-condition for sending messages, a sender needs to generate a an asymmetric key-pair, then register the public key of the key-pair in its DNS record following the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) protocol used by e-mail servers.
    | 2 | When sending a message, the sender wraps the message in an JSON envelope, signs the envelope with the private key of the mentioned key-pair, and sends the signed message via HTTPS POST to the receiver's well-known inbox API endpoint (e.g., `https://nlweb.any-receiver.com/inbox`). 
    | 3 | When receiving the signed message, the receiver reads the public key from the sender's [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>), confirms if the sender is using DNSSEC, and confirms if the message's signature matches the sender's public key.


    ---

2. **What is contained in a domain message envelope?**

    Messages from domains are sent in envelopes similar to email messages, containing the following properties.

    |Property| Description
    |-|-
    | **Code** | The [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) of the envelope (e.g., `nlweb.org/msg:1.0`).
    | **From** | The name of the [domain 👥](<../44 📜 Manifests/00 👥 Domain.md>) who sent the message (e.g., `any-sender.com`).
    | **To**| The name of the [domain 👥](<../44 📜 Manifests/00 👥 Domain.md>) for whom the message is intended (e.g., `any-receiver.com`).
    | **Correlation**| The unique ID in the sender (e.g., `125a5c75-cb72-43d2-9695-37026dfcaa48`).
    | **Timestamp**| The date and time of the message, in UTC format (e.g., `2018-12-10T13:45:00.000Z`).
    | **Subject**| The method to be executed on the receiver (e.g., `AnyMethod`).
    | **Body**| The content inside the envelope.
    | **Hash**| The canonical hash of the envelope.
    | **Signature**| The signature of the envelope using the sender's private key.
    | **Key**| The name of the corresponding public key in the sender's [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>).

    ---

1. **What are the technical workflows around messages?**

    | Workflow | Description
    |-|-
    | [🚀 Synchronous requests](<../../../5 ⏩ Flows/01 👥⏩ Domains/02 👥⏩🚀 Sender outbox.md>) | [Domains 👥](<../44 📜 Manifests/00 👥 Domain.md>) send requests and wait for the immediate response over an HTTPS request.
    | [🐌 Asynchronous messages](<../../../5 ⏩ Flows/01 👥⏩ Domains/03 👥⏩🐌 Sender events.md>) | [Domains 👥](<../44 📜 Manifests/00 👥 Domain.md>) send fire-and-forget messages and events. Any eventual answer, if expected, will arrive via another asynchronous message.

    ---

2. **Is this compatible with W3C DIDcomm?**

    No. 
    
    - W3C DIDcomm is a protocol specific for  [W3C distributed identities (DIDs) 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/03 🛂 Travel ID landscape/10 📺 W3C VC Ledgers.md>). 
    
    - NLWeb advocates for fully offline verification of credentials presented via a QR code, where consumer domains can use cached public keys of issuer domains to verify the signature in the QR 
        - this requires a small footprint of all-encompassed data in the QR. 
    
    - Conversely, W3C advocates for Verifiable Credentials (VCs) supported by DIDs that can be printed into a QR code just like a URL;
        - the DID key needs to be translated into a DID Document by an online key-value database before the consumer domain can read and validate its content;
        - because of this limitation, NLWeb does not implement DIDs.

    ---

3. **How do sender domains prevent man-in-the-middle attacks?**

    By using HTTPS POST requests, sender domains ensure outbound messages are encrypted, and rely on trusted Certificate Authorities (CAs) to validate the TLS certificate of the receiver. 
    - By using a well-known URL prefix plus the receiver’s domain, sender domains rely only on DNS for network discovery.

    ---

4. **How do receiver domains know who sent a message?**

    An NLWeb envelope resembles an email message, containing a header and a body. 
    - The header contains the sender’s domain name (e.g., `any-sender.com`) and the receiver’s domain name (e.g., `any-receiver.com`), as well as other metadata. 
    - Receivers discard envelopes not intended to them.

    ---

5. **How do receiver domains prevent sender impersonation attacks?**

    NLWeb domains implement the ubiquitous [DKIM (rfc6376) protocol 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) used by email servers to verify envelopes received from other domains. 
    
    - Sender domains hash their envelopes with JSON Canonicalization Scheme (rfc8785) and sign them with their private half of the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key-pair. 
    
    - Receiver domains look up the public half of the sender’s [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key-pair to verify the signature of incoming envelopes. The receiver expects to find the sender’s public key in DKIM format in a DNS entry named “nlweb” (e.g., `nlweb._domainkey.any-sender.com`). 
    
    - The envelope is discarded if the sender’s [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) is not correctly implemented, or the sender’s public key is unable to verify the signature in the envelope.

    ---

6. **How do receiver domains prevent DNS spoofing attacks?**

    When getting the sender’s [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) public key, receiver domains check if DNSSEC is implemented on the sender’s domain;
    - if not implemented, the envelope is discarded.

    ---

7. **How do receiver domains prevent replay attacks?**

    An NLWeb envelop contains the sender’s timestamp in UTC format - receivers discard envelopes with a timestamp outside accepted time boundaries. 
    
    - An envelope also contains a correlation UUID that uniquely identifies the outbound message in the sender’s domain.
    - Receivers discard envelopes with duplicate incoming correlations within accepted time boundaries.

    ---

8. **How do receiver domains handle upgraded schema versions?**

    An NLWeb envelop contains a schema identifier that allows receivers to support multiple versions concurrently, handling incoming envelopes differently depending on its version. 
    - Envelopes with unsupported versions are discarded.

    ---

9.  **How do receiver domains reply to incoming messages?**

    In NLWeb, communications are asynchronous to minimize wait times in HTTPS communications and reduce the serverless compute cost of sending outbound messages. 
    
    - Thus, the receiver is expected to store the envelope in a resilient queue and immediately return a successful HTTPS 200 response. 
    
    - The receiver then processes the incoming envelopes asynchronously by consuming them from the queue - it discards invalid envelopes, and replies to valid ones by sending a new envelope to the sender.

    ---

10. **How do receiver domains differentiate methods?**

    An NLWeb envelop contains a subject that identifies how the receiver should handle the message (e.g., payment request). 
    - Receivers discard envelopes with unexpected subjects.

    ---

11. **How can senders know if receivers discarded messages?**

    When discarding an invalid message, receiver domains send a feedback message back to the sender with the original correlation ID. 
    - The feedback is sent via HTTPS POST to the well-known feedback endpoint at the sender's domain (e.g., `https://nlweb.any-sender.com/feedback`). 
    
    To avoid infinite loops, this endpoint has a loose validation and does not provide follow-up feedbacks on incoming feedback messages;
    - e.g., if both sender and receiver have invalid [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) entries, the receiver will discard the initial message from the sender because it cannot validate the signature, and will provide feedback to the sender about it; 
    - the sender will also not be able to validate the receiver's feedback signature, but will try to process the feedback nonetheless.

    ---

12. **With HTTPS compression, how is CRIME/BREACH prevented?** 

    CRIME/BREACH prevention still needs to be analyzed by a security expert.

    ---

