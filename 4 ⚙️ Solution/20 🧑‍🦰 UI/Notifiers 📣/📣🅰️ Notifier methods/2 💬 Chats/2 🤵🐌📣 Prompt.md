# 🤵🐌📣 Prompt @ Notifier

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow, succeeded by:
> <br/>• [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>) message
> <br/>• [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) message
> <br/>• [`Download@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Download.md>)  message


[Broker 🤵 domains](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) 
* forward   [Prompts 🤔](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) 
* from [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
* to [Notifier 📣 domains](<../../📣👥 Notifier domain.md>).




<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-notifier.dom
    Subject: Prompt@Notifier
    
Body:
    Wallet: <wallet-uuid>
    Chat: <chat-uuid>
    Prompt: <prompt-uuid>
    Sender: any-agent.com
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../../Brokers 🤵/🤵🤲 Broker helper.md>) name
||`To`|string| [Notifier 📣 domain](<../../📣👥 Notifier domain.md>) name
||`Subject`|string|`Prompt@Notifier`
|Body  |`Wallet` |uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) ID from [`Converse@Notifier`](<1 🤵🐌📣 Converse.md>)
|      |`Chat`  |uuid  | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Prompt@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🤗🐌🤵 Prompt.md>)
|      |`Prompt`|uuid  | [Prompt 🤔](<../../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) ID from [`Prompt@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🤗🐌🤵 Prompt.md>)
|      |`Sender`  |string| [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) from [`Prompt@Broker`](<../../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🤗🐌🤵 Prompt.md>)
|