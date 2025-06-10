🔏 Domain signature FAQ
===

1. **How do sender domains sign files**?

    ![](<./📎 Assets/📨 Signature Domains.png>)

    The signature has the form of a [Token 🎫](<../../20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>) added as metadata to the file. 
    
    To sign a file, sender domains: 
    - 1/ calculate the hash of the file without the signature; 
    - 2/ bundle the hash with the file's locator within the domain; 
    - 3/ sign the bundle with the private part of their key pair; and 
    - 4/ add the signature Token to the file. 

    ---

1. **How do receiver domains verify a sender's signature**?

    To verify a file, receiver domains: 
    - 1/ calculate the hash of the file without the signature [Token 🎫](<../../20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>) and compare it with the hash in the signature; 
    - 2/ verify the Token. 

    ---

1. **What if the public key of the sender changes?**

    NLWeb supports the rotation of domain DKIM public keys for any [Token 🎫](<../../20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>), including digital signatures. 
    
    See [Issuers 🎴](<../../20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/02 ✅ 🎴🎭 Issuer role.md>) for details on how to rotate public keys supported with the support of [Listeners 👂](<../44 ✅ 📜 Manifests/02 ✅ 👂👥 Listener helper.md>) and [Graphs 🕸](<../44 ✅ 📜 Manifests/03 ✅ 🕸👥 Graph helper.md>).

    ---

1. **What's the reason for removing the signature from hash**?

    When metadata is added to a file, it changes its hash. Thus, it's impossible to add the hash of a file to the file itself, because the act of doing so automatically changes the hash.

    ---

1. **Can other metadata be added to files after being signed**?

    No. That would invalidate the hash in the signature.

    ---

1. **Can signatures be invalidated by zipping the file**?

    No. The binary nature of digital files ensure their integrity.

    ---

1. **Can senders sign files with an expiration date?**

    Yes. See [Issuers 🎴](<../../20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/02 ✅ 🎴🎭 Issuer role.md>) for details on how to create temporary [Tokens 🎫](<../../20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>).

    ---
