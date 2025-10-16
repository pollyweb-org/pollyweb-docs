🔏 Domain stamps
===

1. **What is a domain stamp?**

    A domain stamp is a string added as metadata to the file. 

    ---
    <br/>

1. **What are examples of domain stamps?**

    | Example | Details
    |-|-
    | [🚀 Download @ Host](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Download.md>) | Download [Prompt 🤔](<../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) appendixes in [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)

    ---
    <br/>

1. **How does it work**?

    ![](<.📎 Assets/🔏 Domain Signature.png>)

    |#| Step | Details
    |-|-|-
    |1| `DKIM` | Domain A rotates its [DKIM](<../👥📨 Domain Messages/📨 Message.md>) public key.
    |2| `Stamp` | Domain A signs a file with its latest private key, then sends the file to Domain B.
    |3| `Share`| Domain B shares the file with Domain C.
    |4| `Check`| Domain C verifies the signature of the file against the DKIM public key that was active at the time of the signature.

    ---
    <br/>

1. **How is a signature Token added to a file?**

    The signature is added as a property called `NLWeb Signature`.

    Type | Details
    |-|-
    |`PDF`| This is stored as a custom property in Standard PDF Metadata (Document Properties).
    |`PNG`| EXIF metadata from PNG spec. Note that apps like WhatsApp, Facebook, Twitter strip metadata when users upload the images.
    |...| No other type is supported.

    ---
    <br/>

1. **What is contained in a domain stamp?**

    Domain stamps contain the following properties.
    
    ```yaml
    Code: nlweb.org/SIGNATURE:1.0
    Domain: any-domain.dom
    Signed: '2024-09-21T12:34:00Z'
    DKIM: pk1
    Hash: KDHNERT...
    Signature: ABCMIQDALK2Fd...
    ```

    |Property| Type | Details
    |-|-|-
    | `Code` | string |  `nlweb.org/SIGNATURE:1.0`
    | `Domain` | string | The [domain 👥](<../👥 Domains/👥 Domain.md>) name
    | `Hash` | string |  The hash of the file
    | `Signed` | timestamp | When it was signed
    | `DKIM`| string | The [DKIM 📨](<../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Public Key.md>) key used to sign
    | `Signature`| string | The [signature](<../👥📨 Domain Messages/📨 Message.md>) 📨 

    ---
    <br/>

1. **How do sender domains stamp files**?
    
    To stamp a file, sender [domains 👥](<../👥 Domains/👥 Domain.md>): 
    1. calculate the hash of the file without the stamp; 
    2. create a stamp with hash but without the signature;
    3. create a signature from the stamp;
    4. add the signature to the stamp;
    5. add the stamp to the file. 

    ---
    <br/>

1. **How do receiver domains verify a sender's signature**?

    To verify a file, receiver [domains 👥](<../👥 Domains/👥 Domain.md>): 
    1. calculate the hash of the file without the stamp;
    2. compare it with the hash in the stamp; 
    3. get the public key for the DKIM by calling [Public Key @ Graph 🚀](<../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Public Key.md>);
    4. verify if the signature matches the stamp. 

    ---
    <br/>

1. **What if the public key of the sender changes?**

    The stamp contains the key of the DKIM used to sign the file, so it can obtain the public key with [Public Key @ Graph 🚀](<../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Public Key.md>).

    ---
    <br/>

1. **What's the reason for removing the stamp from hash?**

    When metadata is added to a file, it changes its hash. 
    * Thus, it's impossible to add the hash of a file to the file itself, 
    * because the act of doing so automatically changes the hash.

    ---
    <br/>

1. **Can other metadata be added to files after being signed?**

    No. That would invalidate the hash in the signature.

    ---
    <br/>

1. **Can signatures be invalidated by zipping the file**?

    No. The binary nature of digital files ensure their integrity.

    ---
    <br/>
