# 🤵🐌📣 Prompt @ Notifier

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow, succeeded by:
> <br/>• [`Prompted@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>) message
> <br/>• [`Reply@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) message
> <br/>• [`Download@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Download.md>)  message


[Broker 🤵 domains](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) 
* forward   [Prompts 🤔](<../../../../35 Chats/🤔 Prompts/🤔 Prompt.md>) 
* from [Host 🤗 domains](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) 
* to [Notifier 📣 domains](<../../📣👥 Notifier domain.md>).




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
|Header|`From`|string | [Broker 🤵 domain](<../../../3 🤵 Brokers/🤵🤲 Broker helper.md>) name
||`To`|string| [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) name
||`Subject`|string|`Prompt@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) ID from [`Converse@Notifier`](<1 🤵🐌📣 Converse.md>)
|      |`ChatID`  |uuid  | [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>) ID from [`Prompt@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🤗🐌🤵 Prompt.md>)
|      |`PromptID`|uuid  | [Prompt 🤔](<../../../../35 Chats/🤔 Prompts/🤔 Prompt.md>) ID from [`Prompt@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🤗🐌🤵 Prompt.md>)
|      |`Sender`  |string| [Host 🤗](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) from [`Prompt@Broker`](<../../../3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🤗🐌🤵 Prompt.md>)
|