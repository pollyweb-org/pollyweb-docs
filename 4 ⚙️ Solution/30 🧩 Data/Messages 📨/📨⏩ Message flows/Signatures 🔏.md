📨🔏 Message Signatures
===

> Part of [domain Message 📨](<../📨 Message/📨 Message.md>)

<br/> 

1. **What is the signature for?**

    Senders sign the header and body of envelopes with [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) private key,
    - [domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) verify incoming [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) messages with the sender's [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) public key,
    - and [Broker 🤵 domains](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) verify incoming [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) messages with the their pre-shared public key.
    
    ---
    <br/>



1. **How do receiver domains prevent sender impersonation attacks?**

    PollyWeb domains implement the ubiquitous [DKIM (rfc6376) protocol 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) used by email servers to verify envelopes received from other domains. 
    
    - Sender domains hash their envelopes with JSON Canonicalization Scheme (rfc8785) and sign them with their private half of the [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key-pair. 
    
    - Receiver domains look up the public half of the sender’s [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) key-pair to verify the signature of incoming envelopes. The receiver expects to find the sender’s public key in DKIM format in a DNS entry named “pw” (e.g., `pw._domainkey.any-sender.dom`). 
    
    - The envelope is discarded if the sender’s [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) is not correctly implemented, or the sender’s public key is unable to verify the signature in the envelope.

    ---
    <br/>


1. **How do receiver domains prevent DNS spoofing attacks?**

    When getting the sender’s [DKIM 📺](<../../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/07 📺 Email DKIM.md>) public key, receiver domains check if DNSSEC is implemented on the sender’s domain;
    - if not implemented, the envelope is discarded.

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
      - `private.pem`: the private signature of the [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>).
  
    Then run the following commands on a terminal: 
    * `$ openssl dgst -sha256 -sign private.pem -out signature.sha1 canonical.json`
    * `$ openssl base64 -A -in signature.sha1 -out signature.txt`
    * `$ cat signature.txt`

    ---
    <br/>

1. **How to validate a signature with OpenSSL?**

    To validate a signature with OpenSSL, first prepare the following files:
    - `signature.txt`: the signature received in a message from another [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>);
    - `canonical.json`: a canonical representation of the received {header,body};
    - `public.pem`: the public key of the sender [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>).
  
    Then run the following commands on a terminal: 
    * $ `openssl enc -d -A -base64 -in signature.txt -out signature.sha1`
    * $ `openssl dgst -sha256 -verify public.pem -signature signature.sha1 canonical.json`

    ---
    <br/>