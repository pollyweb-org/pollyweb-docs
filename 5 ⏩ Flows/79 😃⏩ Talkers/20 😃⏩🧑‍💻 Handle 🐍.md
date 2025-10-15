# 😃⏩🤗 Handle @ Talker

> Implements [Hoster ☁️ helper domain](<../../9 😃 Talkers/90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>)

* [Talkers 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) ask [Hosted 🧑‍💻 domains](<../../9 😃 Talkers/91 🧑‍💻 Hosteds/01 🧑‍💻 Hosted domain.md>) 
    * to handle [{Function} 🐍](<../../9 😃 Talkers/30 🗃️ Talker data/12 🐍 {Function}.md>) evaluations 
    * and return the computed result.

<br/>

## ⏩ Flow diagram

![alt text](<.📎 Assets/Handle.png>)

| # | Call | Description
|-|-|-
|1| [🤗⏩🧑‍🦰 Prompt 🤔](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Talkers 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) handle replies to [Prompts 🤔](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>)
|2| [😃🐌🧑‍💻 `Handle@Hosted`](<../../6 🅰️ APIs/51 🧑‍💻🅰️ Hosted/01 😃🐌🧑‍💻 Handle.md>) | [Talkers 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) delegate functions to [Hosteds 🧑‍💻](<../../9 😃 Talkers/91 🧑‍💻 Hosteds/01 🧑‍💻 Hosted domain.md>)
|3| [🧑‍💻🚀😃 `Placed@Talker`](<../../6 🅰️ APIs/92 😃🅰️ Talker/10 🧑‍💻🚀😃 Placed.md>) | [Hosteds 🧑‍💻](<../../9 😃 Talkers/91 🧑‍💻 Hosteds/01 🧑‍💻 Hosted domain.md>) read [$Placeholder 💾](<../../9 😃 Talkers/30 🗃️ Talker data/10 💾 $Placeholder.md>) values
|4| [🧑‍💻🐌😃 `Handled@Talker`](<../../6 🅰️ APIs/92 😃🅰️ Talker/40 🧑‍💻🐌😃 Handled.md>) | [Hosteds 🧑‍💻](<../../9 😃 Talkers/91 🧑‍💻 Hosteds/01 🧑‍💻 Hosted domain.md>) return the evaluated result 
|5| [🤗⏩🧑‍🦰 Prompt 🤔](<../50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Talkers 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) continue the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|

<br/>

## FAQ

1. **Why isn't [`Handle@Hosted`](<../../6 🅰️ APIs/51 🧑‍💻🅰️ Hosted/01 😃🐌🧑‍💻 Handle.md>) synchronous?**

    For a number of reasons:

    * `Timeout` This allows [Hosted 🧑‍💻 domains](<../../9 😃 Talkers/91 🧑‍💻 Hosteds/01 🧑‍💻 Hosted domain.md>) to talk as long as they want to reply.

    * `Cost` The [Talker 😃 API](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) doesn't need to pay cloud compute costs for idle time waiting for a response from [Hosted 🧑‍💻 domains](<../../9 😃 Talkers/91 🧑‍💻 Hosteds/01 🧑‍💻 Hosted domain.md>).

    * `User Experience` [Hosted 🧑‍💻 domains](<../../9 😃 Talkers/91 🧑‍💻 Hosteds/01 🧑‍💻 Hosted domain.md>) can immediately confirm that a long-running task was started, then continuously send updates regarding the task progress - see the [😃⏩🧑‍💻 Wait ⏸️](<30 😃⏩🧑‍💻 Wait ⏸️.md>) flow or details on this.

    ---
    <br/>


1. **Why isn't the [Talker 😃 API](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) a separate domain?**

    [Talkers 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) manage a wide number of messages for multiple [domain roles 🎭](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>);
    * e.g., [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>), [Vault 🗄️](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vault/$ 🗄️🎭 Vault role.md>), [Issuer 🎴](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>), [Seller 💵](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>).
    * Exposing endpoints for each method of each role is cumbersome.

    ---
    <br/>