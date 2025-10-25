📨 Domain Message
===

1. **What are messages?**

    [Messages 📨](<📨 Message.md>) 
    * are data structures 
    * with which [domains 👥](<../../40 👥 Domains/👥 Domain.md>) communicate with one another.

    ---
    <br/>


1. **How does a domain send a request to another domain?**

    ![](<.📎 Assets/📨 Domain Message.png>)

    For two [domains 👥](<../../40 👥 Domains/👥 Domain.md>) to communicate with one another (e.g., for `any-sender.dom` to send a message to `any-receiver.dom`), the following steps are required.

    | # |  Step
    |-|-
    | 1 | As a pre-condition for sending messages, a sender needs to generate a an asymmetric key-pair, then register the public key of the key-pair in its DNS record following the [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) protocol used by e-mail servers.
    | 2 | When sending a message, the sender wraps the message in an JSON envelope, signs the envelope with the private key of the mentioned key-pair, and sends the signed message via HTTPS POST to the receiver's well-known inbox API endpoint (e.g., `https://nlweb.any-receiver.com/inbox`). 
    | 3 | When receiving the signed message, the receiver reads the public key from the sender's [DKIM 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>), confirms if the sender is using DNSSEC, and confirms if the message's signature matches the sender's public key.


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

1. **What else is to know about Messages?**

    This document includes the following subsections.

    | Subsection | Purpose
    |-|-
    | [✉️ Envelope](<📨⏩ Message flows/Envelope ✉️.md>) | The structure of a [Message 📨](<📨 Message.md>)
    | [🔏 Signatures](<📨⏩ Message flows/Signatures 🔏.md>) | How [Messages 📨](<📨 Message.md>) are signed and verified
    | [🚀 Sync Requests](<📨⏩ Message flows/Sync Requests 🚀.md>) | HTTP requests that wait an answer
    | [🐌 Async Messages ](<📨⏩ Message flows/Async Messages 🐌.md>) | Event-driven fire-and-forget [Messages 📨](<📨 Message.md>)
    
    ---
    <br/>
