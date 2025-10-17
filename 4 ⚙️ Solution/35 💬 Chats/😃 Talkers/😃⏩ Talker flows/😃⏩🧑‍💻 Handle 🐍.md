# 😃⏩🤗 Handle @ Talker

> Implements [Hoster ☁️ helper domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)

* [Talkers 😃](<../😃 Talker.md>) ask [Hosted 📦 domains](<../../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>) 
    * to handle [{Function} 🐍](<../😃💾 Talker data/{Function} 🐍.md>) evaluations 
    * and return the computed result.

<br/>

## ⏩ Flow diagram

![alt text](<.📎 Assets/Handle.png>)

| # | Call | Description
|-|-|-
|1| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Talkers 😃](<../😃 Talker.md>) handle replies to [Prompts 🤔](<../../🤔 Prompts/🤔 Prompt.md>)
|2| [😃🐌🧑‍💻 `Handle@Hosted`](<../../../55 👷 Build domains/📦 Hosteds/📦🅰️ Hosted methods/😃🐌📦 Handle.md>) | [Talkers 😃](<../😃 Talker.md>) delegate functions to [Hosteds 📦](<../../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>)
|3| [🧑‍💻🚀😃 `Placed@Talker`](<../😃🅰️ Talker methods/🧑‍💻🚀😃 Placed.md>) | [Hosteds 📦](<../../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>) read [$Placeholder 💾](<../😃💾 Talker data/$Placeholder 💾.md>) values
|4| [🧑‍💻🐌😃 `Handled@Talker`](<../😃🅰️ Talker methods/🧑‍💻🐌😃 Handled.md>) | [Hosteds 📦](<../../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>) return the evaluated result 
|5| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Talkers 😃](<../😃 Talker.md>) continue the [Chat 💬](<../../💬 Chats/💬 Chat.md>)
|

<br/>

## FAQ

1. **Why isn't [`Handle@Hosted`](<../../../55 👷 Build domains/📦 Hosteds/📦🅰️ Hosted methods/😃🐌📦 Handle.md>) synchronous?**

    For a number of reasons:

    * `Timeout` This allows [Hosted 📦 domains](<../../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>) to talk as long as they want to reply.

    * `Cost` The [Talker 😃 API](<../😃 Talker.md>) doesn't need to pay cloud compute costs for idle time waiting for a response from [Hosted 📦 domains](<../../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>).

    * `User Experience` [Hosted 📦 domains](<../../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>) can immediately confirm that a long-running task was started, then continuously send updates regarding the task progress - see the [😃⏩🧑‍💻 Wait ⏸️](<😃⏩🧑‍💻 Wait ⏸️.md>) flow or details on this.

    ---
    <br/>


1. **Why isn't the [Talker 😃 API](<../😃 Talker.md>) a separate domain?**

    [Talkers 😃](<../😃 Talker.md>) manage a wide number of messages for multiple [domain roles 🎭](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>);
    * e.g., [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>), [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>), [Issuer 🎴](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>), [Seller 💵](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>).
    * Exposing endpoints for each method of each role is cumbersome.

    ---
    <br/>