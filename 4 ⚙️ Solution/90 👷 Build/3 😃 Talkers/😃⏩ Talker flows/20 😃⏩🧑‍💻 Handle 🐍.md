# 😃⏩🤗 Handle @ Talker

> Implements [Hoster ☁️ helper domain](<../../../45 🤲 Helper domains/55 ☁️ Hosters/☁️🤲 Hoster helper.md>)

* [Talkers 😃](<../😃 Talker.md>) ask [Hosted 📦 domains](<../../1 📦 Hosteds/📦👥 Hosted domain.md>) 
    * to handle [{Function} 🐍](<../😃💾 Talker data/12 🐍 {Function}.md>) evaluations 
    * and return the computed result.

<br/>

## ⏩ Flow diagram

![alt text](<.📎 Assets/Handle.png>)

| # | Call | Description
|-|-|-
|1| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Talkers 😃](<../😃 Talker.md>) handle replies to [Prompts 🤔](<../../../35 Chats/🤔 Prompts/🤔 Prompt.md>)
|2| [😃🐌🧑‍💻 `Handle@Hosted`](<../../1 📦 Hosteds/📦🅰️ Hosted methods/😃🐌📦 Handle.md>) | [Talkers 😃](<../😃 Talker.md>) delegate functions to [Hosteds 📦](<../../1 📦 Hosteds/📦👥 Hosted domain.md>)
|3| [🧑‍💻🚀😃 `Placed@Talker`](<../😃🅰️ Talker methods/10 🧑‍💻🚀😃 Placed.md>) | [Hosteds 📦](<../../1 📦 Hosteds/📦👥 Hosted domain.md>) read [$Placeholder 💾](<../😃💾 Talker data/10 💾 $Placeholder.md>) values
|4| [🧑‍💻🐌😃 `Handled@Talker`](<../😃🅰️ Talker methods/40 🧑‍💻🐌😃 Handled.md>) | [Hosteds 📦](<../../1 📦 Hosteds/📦👥 Hosted domain.md>) return the evaluated result 
|5| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | [Talkers 😃](<../😃 Talker.md>) continue the [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>)
|

<br/>

## FAQ

1. **Why isn't [`Handle@Hosted`](<../../1 📦 Hosteds/📦🅰️ Hosted methods/😃🐌📦 Handle.md>) synchronous?**

    For a number of reasons:

    * `Timeout` This allows [Hosted 📦 domains](<../../1 📦 Hosteds/📦👥 Hosted domain.md>) to talk as long as they want to reply.

    * `Cost` The [Talker 😃 API](<../😃 Talker.md>) doesn't need to pay cloud compute costs for idle time waiting for a response from [Hosted 📦 domains](<../../1 📦 Hosteds/📦👥 Hosted domain.md>).

    * `User Experience` [Hosted 📦 domains](<../../1 📦 Hosteds/📦👥 Hosted domain.md>) can immediately confirm that a long-running task was started, then continuously send updates regarding the task progress - see the [😃⏩🧑‍💻 Wait ⏸️](<30 😃⏩🧑‍💻 Wait ⏸️.md>) flow or details on this.

    ---
    <br/>


1. **Why isn't the [Talker 😃 API](<../😃 Talker.md>) a separate domain?**

    [Talkers 😃](<../😃 Talker.md>) manage a wide number of messages for multiple [domain roles 🎭](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>);
    * e.g., [Host 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>), [Vault 🗄️](<../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>), [Issuer 🎴](<../../../41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>), [Seller 💵](<../../../41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>).
    * Exposing endpoints for each method of each role is cumbersome.

    ---
    <br/>