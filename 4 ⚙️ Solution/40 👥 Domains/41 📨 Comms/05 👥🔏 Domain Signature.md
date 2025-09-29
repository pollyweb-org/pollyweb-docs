🔏 Domain signature FAQ
===

1. **What is a domain signature?**

    A domain signature has the form of a [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) added as metadata to the file. 

    ---
    <br/>

1. **What are examples of domain signatures?**

    | Example | Details
    |-|-
    | [🚀 Download @ Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/06 🧑‍🦰🚀🤗 Download.md>) | Download [Prompt 🤔](<../../20 🧑‍🦰 UI/23 💬 Chats/02 🤔 Prompt.md>) appendixes in [Chats 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)

    ---
    <br/>

2. **How does it work**?

    ![](<.📎 Assets/📨 Signature Domains.png>)

    |#| Step | Details
    |-|-|-
    |1| `DKIM` | Domain A rotates its [DKIM](<01 📨 Domain Message.md>) public key.
    |2| `Sign` | Domain A signs a file with its latest private key, then sends the file to Domain B.
    |3| `Share`| Domain B shares the file with Domain C.
    |4| `Check`| Domain C verifies the signature of the file against the DKIM public key that was active at the time of the signature.

    ---
    <br/>

3. **How do sender domains sign files**?
    
    To sign a file, sender [domains 👥](<../44 📜 Manifests/00 👥 Domain.md>): 
    1. calculate the hash of the file without the signature; 
    2. bundle the hash with the file's locator within the domain; 
    3. sign the bundle with the private part of their key pair; and 
    4. add the [signature Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to the file. 

    ---
    <br/>

4. **How do receiver domains verify a sender's signature**?

    To verify a file, receiver [domains 👥](<../44 📜 Manifests/00 👥 Domain.md>): 
    1. calculate the hash of the file without the signature [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) and compare it with the hash in the signature; 
    2. verify the [signature Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>). 

    ---
    <br/>

5. **What if the public key of the sender changes?**

    NLWeb supports the rotation of [domain DKIM public keys](<01 📨 Domain Message.md>) for any [Token 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>), including digital signatures. 
    
    * See [Issuers 🎴](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) for details on how to rotate public keys supported with the support of [Listeners 👂](<../44 📜 Manifests/02 👂🛠️ Listener helper.md>) and [Graphs 🕸](<../44 📜 Manifests/03 🕸🛠️ Graph helper.md>).

    ---
    <br/>

6. **What's the reason for removing the signature from hash**?

    When metadata is added to a file, it changes its hash. 
    * Thus, it's impossible to add the hash of a file to the file itself, 
    * because the act of doing so automatically changes the hash.

    ---
    <br/>

7. **Can other metadata be added to files after being signed**?

    No. That would invalidate the hash in the signature.

    ---
    <br/>

8. **Can signatures be invalidated by zipping the file**?

    No. The binary nature of digital files ensure their integrity.

    ---
    <br/>

9.  **Can senders sign files with an expiration date?**

    Yes. See [Issuers 🎴](<../../20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) for details on how to create temporary [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).

    ---
    <br/>
