# 🔃 Syncer tool


1. **Is it encrypted?**

    Yes. All communication is done over HTTPS.

    ---
    <br/>

1. **Is it authenticated?**

    Yes. 
    * First, users use their [Wallet 🧑‍🦰 apps](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to approve the [Clone ⏩](<10 🔃⏩🗃️ Clone.md>) with one-time passwords, registering the [Syncer's 🔃](<../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) public key on the [Resourcer 🗃️ domain](<../../9 😃 Talkers/90 ☁️ Hosters/02 🗃️🎭 Resourcer role.md>).

    * Follow-up requests are then signed with the [Syncer's 🔃](<../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) private key.

    ---
    <br/>

1. **How are changes identified?**

    Using SHA-256 hashing.

    ---
    <br/>




1. **What commands are supported on the terminal CLI?**

    The terminal Command Line Interface (CLI) supports the following commands.

    |🧑‍💻 Command | Description
    |-|-
    |`clone <name>` | Generates a [QR Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>)<br> for the user to scan with the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>to clone the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) to a local folder<br/>- e.g., `my-hoster clone my-domain`
    |`sync` | Syncs the changes with the [Hoster ☁️ domain](<05 ☁️🛠️ Hoster helper.md>) <br/>- e.g., `my-hoster sync`
    |`chat <env>`| Opens a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) with an environment<br/>on the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>- e.g., `my-hoster chat local`
    <!--|`test <env>`| Runs test scripts on an environment<br/>- e.g., `my-hoster test local`-->

    ---
    <br/>




1. **What does a terminal CLI interaction looks like?**

    |🧑‍💻 Command | 🖥️ Display |  Workstation
    |-|-|-
    |`$ clone my-domain` | ⏳ Scan the QR code... | [✨ scan](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>)
    || ✅ Domain cloned to folder
    |`code .` | &lt;opens visual studio code&gt;| 🧑‍💻 implement
    |`$ sync` | ✅ Changes synchronized.
    |`$ chat dev` | ⏳ Chat on your Wallet... | [💬 chat](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
    || ✅ Chat finished. | 
    |`$ chat prod` | ⏳ Chat on your Wallet... | [💬 chat](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
    || ✅ Chat finished. | 
    <!--|`$ test dev` | ✅ Tested successfully. | 🥳 celebrate-->
    
    

    ---
    <br/>




1. **What happens when the Wallet scans the QR?**

    | Service | Prompt  | User 
    | - | - | - 
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | ℹ️ Cloning request:<br/>- domain: my-domain<br/>- from: London, UK
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | 😃 Authorize? [Yes, No]<br/>- [ I don't recognize it ] | > Yes
    | [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) | ✅ Authorized!
    
    ---
    <br/>
