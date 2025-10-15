# 🔃 Syncer tool

> Relates to [Resourcer 🗃️ domain role](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/$ 🗃️🎭 Resourcer role.md>).

<br/>


1. **What is a Syncer tool?**

    A [Syncer 🔃 tool](<01 🔃🛠️ Syncer tool.md>)
    * is a command-line tool
    * to sync local files 
    * with a [Resourcer 🗃️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/$ 🗃️🎭 Resourcer role.md>).

    ---
    <br/>

1. **What commands are supported on the terminal?**

    |Command 🧑‍💻| Description
    |-|-
    |[⏩ `clone`](<../../5 ⏩ Flows/77 🔃⏩ Syncer/10 🔃⏩🗃️ Clone.md>) | Registers [Syncer 🔃 tools](<../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) on [Resourcers 🗃️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/$ 🗃️🎭 Resourcer role.md>)
    |[⏩ `sync`](<../../5 ⏩ Flows/77 🔃⏩ Syncer/20 🔃⏩🗃️ Sync.md>) | Syncs local files with [Resourcer 🗃️ domains](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/$ 🗃️🎭 Resourcer role.md>) 
    |[⏩ `chat`](<../../6 🅰️ APIs/78 🗃️🅰️ Resourcer/70 🔃🐌🗃️ Chat.md>)| Opens [Chats 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with [Resourcer 🗃️ domains](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/$ 🗃️🎭 Resourcer role.md>)
    <!--|`test <env>`| Runs test scripts on an environment<br/>- e.g., `my-hoster test local`-->

    ---
    <br/>


1. **Is it encrypted?**

    Yes. All communication is done over HTTPS.

    ---
    <br/>

1. **Is it authenticated?**

    Yes. 
    * First, users use their [Wallet 🧑‍🦰 apps](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to approve the [Clone ⏩](<../../5 ⏩ Flows/77 🔃⏩ Syncer/10 🔃⏩🗃️ Clone.md>) with one-time passwords, registering the [Syncer's 🔃](<../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) public key on the [Resourcer 🗃️ domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/60 🗃️ Resourcers/$ 🗃️🎭 Resourcer role.md>).

    * Follow-up requests are then signed with the [Syncer's 🔃](<../../9 😃 Talkers/90 ☁️ Hosters/01 🔃🛠️ Syncer tool.md>) private key.

    ---
    <br/>

1. **How are changes identified?**

    Using SHA-256 hashing.

    ---
    <br/>


