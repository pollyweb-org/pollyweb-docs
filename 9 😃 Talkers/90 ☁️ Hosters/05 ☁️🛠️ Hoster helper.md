# 🧑‍💻🛠️ Hoster helper FAQ

|.|.|.
|-|-|-
|3| `Clone`| On a workstation terminal, <br/>the user [scans ✨](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/03 🧑‍🦰✨ Wallet QR scan.md>) the terminal QR code <br/>to link the terminal to the [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)<br/>and download the [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) settings.
|4| `Edit`| On a code editor (e.g., Visual Studio Code)<br/>the user configures the logic webhooks <br/>and the public [domain 📜 Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>).
|5| `Sync`| On the workstation terminal, <br/>the user synchronizes the changes <br/>with the [Hoster ☁️ domain](<05 ☁️🛠️ Hoster helper.md>).
|6| `Test`| From the workstation terminal, <br/>the user opens [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) for manual testing.

1. **What is a Hoster?**

    A [🧑‍💻 Hoster](<05 ☁️🛠️ Hoster helper.md>) is 
    * any [Helper 🛠️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)
    * that hosts the infrastructure of a [Hosted 🧑‍💻 domain](<10 🧑‍💻☁️ Hosted domain.md>)
    * and allow their owners to manage them with a [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

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
