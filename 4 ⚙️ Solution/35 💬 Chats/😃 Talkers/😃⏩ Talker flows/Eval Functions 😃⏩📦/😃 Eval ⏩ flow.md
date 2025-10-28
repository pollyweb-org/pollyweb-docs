<!-- TODO: Diagram changed -->

# 😃⏩🤗 Handle @ Talker

> Implements [Hoster ☁️ helper domain](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)

* [Talkers 😃](<../../😃 Talker role.md>) ask [Hosted 📦 domains](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) 
    * to handle [{Function} 🐍](<../../😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) evaluations 
    * and return the computed result.

<br/>

## ⏩ Flow diagram

![alt text](<😃 Eval ⚙️ uml.png>)

| # | Call | Description
|-|-|-
|1| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Talkers 😃](<../../😃 Talker role.md>) handle replies to [Prompts 🤔](<../../../🤔 Prompts/🤔 Prompt.md>)
|2| [😃🐌🧑‍💻 `Handle@Hosted`](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>) | [Talkers 😃](<../../😃 Talker role.md>) delegate functions to [Hosteds 📦](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>)
|3| [🧑‍💻🚀😃 `Placed@Talker`](<../../😃🅰️ Talker methods/Placed 🧑‍💻🚀😃/😃 Placed 🚀 request.md>) | [Hosteds 📦](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) read [Holder 🧠](<../../😃⚙️ Talker cmds/...holders 🧠/$Holder 🧠.md>) values
|4| [🧑‍💻🐌😃 `Handled@Talker`](<../../😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>) | [Hosteds 📦](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) return the evaluated result 
|5| [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) | [Talkers 😃](<../../😃 Talker role.md>) continue the [Chat 💬](<../../../💬 Chats/💬 Chat.md>)
|

<br/>

## FAQ

1. **Why isn't [`Handle@Hosted`](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>) synchronous?**

    For a number of reasons:

    * `Timeout` This allows [Hosted 📦 domains](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) to talk as long as they want to reply.

    * `Cost` The [Talker 😃 API](<../../😃 Talker role.md>) doesn't need to pay cloud compute costs for idle time waiting for a response from [Hosted 📦 domains](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>).

    * `User Experience` [Hosted 📦 domains](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) can immediately confirm that a long-running task was started, then continuously send updates regarding the task progress - see the [😃⏩🧑‍💻 Wait 🧘](<../Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>) flow or details on this.

    ---
    <br/>


1. **Why isn't the [Talker 😃 API](<../../😃 Talker role.md>) a separate domain?**

    [Talkers 😃](<../../😃 Talker role.md>) manage a wide number of messages for multiple [domain roles 🎭](<../../../../40 👥 Domains/👥 Domain.md>);
    * e.g., [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>), [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>), [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>), [Seller 💵](<../../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>).
    * Exposing endpoints for each method of each role is cumbersome.

    ---
    <br/>