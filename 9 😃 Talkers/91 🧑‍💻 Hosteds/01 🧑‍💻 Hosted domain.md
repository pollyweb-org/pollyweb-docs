<!-- TODO -->

# 🧑‍💻☁️ Hosted domain

> Part of [Hoster ☁️ helper domain](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>)

<br/>


1. **How to set up a Hosted domain?**
 
    |#|Step
    |-|-
    |1| [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) to a [Hoster ☁️ domain](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>)
    |2| [Clone](<../../5 ⏩ Flows/77 🔃⏩ Syncer/10 🔃⏩🗃️ Clone.md>) the files to a local folder
    |3| Spin up an HTTP backend endpoint
    |4| Edit the files and [sync](<../../5 ⏩ Flows/77 🔃⏩ Syncer/20 🔃⏩🗃️ Sync.md>) the changes
    

    ---
    <br/>



1. **What domain files are cloned locally?**

    | File | Format | Purpose
    |-|-|-
    | [🔑 PublicKey](<10 🔑📄 PublicKey file.md>) | TXT | Public key for encryption
    | [📥 Inbound](<11 📥📄 Inbound file.md>) | YAML | Message inbound configuration
    | [📤 Outbound](<12 📤📄 Outbound file.md>) | YAML | Message outbound configuration
    | [🛠️ Helpers](<13 🛠️📄 Helpers file.md>)  | YAML | Required [Helper 🛠️ domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)
    | 🔆 [Locators](<14 🔆📄 Locators file.md>) | YAML | Map of [Locators 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) to [Talkers 😃](<../10 📘 Talker specs/10 😃 Talker.md>)
    | 😃 [Talkers](<15 😃📄 Talkers folder.md>) | Folder | List of [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>) scripts 
    | [📜 Manifest](<16 📜📄 Manifest folder.md>) | Folder | Public [domain Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) parts
    

    ---
    <br/>





1. **What are the API methods?**
   
    | Method | Purpose
    |-|-
    [😃🐌 Handle](<../../6 🅰️ APIs/51 🧑‍💻🅰️ Hosted/01 😃🐌🧑‍💻 Handle.md>) | Evaluates [{Functions}](<../30 🗃️ Talker data/12 🐍 {Function}.md>) in [Talkers 😃](<../10 📘 Talker specs/10 😃 Talker.md>)
    
    ---
    <br/>



1. **What is required from domain owners?**
      
    | Dependency | Purpose
    |-|-
    | [🧑‍🦰 Wallet](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) | To authenticate and [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) with the [Hoster ☁️ ](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>)
    | [💳 Payer](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/04 💳🫥 Payer agent.md>) | To pay for usage and subscription plans.
    | [🆔 Identity](<../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | To authenticate the domain user.
    | [🗂️ Folder](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>) | To manage the settings of the hosted [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    ---
    <br/>