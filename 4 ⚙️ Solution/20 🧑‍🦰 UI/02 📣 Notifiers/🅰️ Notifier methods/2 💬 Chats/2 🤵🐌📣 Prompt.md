# 🤵🐌📣 Prompt @ Notifier

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow, succeeded by:
> <br/>• [`Prompted@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/54 🧑‍🦰🚀🤗 Prompted@Host.md>) message
> <br/>• [`Reply@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/55 🧑‍🦰🐌🤗 Reply@Host.md>) message
> <br/>• [`Download@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/56 🧑‍🦰🚀🤗 Download@Host.md>)  message


[Broker 🤵 domains](<../../../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) 
* forward   [Prompts 🤔](<../../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) 
* from [Host 🤗 domains](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) 
* to [Notifier 📣 domains](<../../📣 Notifier domain.md>).




<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-notifier.com
    Subject: Prompt@Notifier
Body:
    WalletID: <wallet-uuid>
    ChatID: <chat-uuid>
    PromptID: <prompt-uuid>
    Sender: any-agent.com
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../📣 Notifier domain.md>) name
||`Subject`|string|`Prompt@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) ID from [`Converse@Notifier`](<1 🤵🐌📣 Converse.md>)
|      |`ChatID`  |uuid  | [Chat 💬](<../../../12 💬 Chats/$ 💬 Chat.md>) ID from [`Prompt@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>)
|      |`PromptID`|uuid  | [Prompt 🤔](<../../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) ID from [`Prompt@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>)
|      |`Sender`  |string| [Host 🤗](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) from [`Prompt@Broker`](<../../../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>)
|