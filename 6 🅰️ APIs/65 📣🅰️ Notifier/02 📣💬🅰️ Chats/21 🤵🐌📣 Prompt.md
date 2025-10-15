# 🤵🐌📣 Prompt @ Notifier

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/31 🤗⏩🧑‍🦰 Prompt 🤔 flow.md>) flow, succeeded by:
> <br/>• [`Prompted@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/50 🤗🅰️ Host/54 🧑‍🦰🚀🤗 Prompted@Host.md>) message
> <br/>• [`Reply@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/50 🤗🅰️ Host/55 🧑‍🦰🐌🤗 Reply@Host.md>) message
> <br/>• [`Download@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/50 🤗🅰️ Host/56 🧑‍🦰🚀🤗 Download@Host.md>)  message


[Broker 🤵 domains](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) 
* forward   [Prompts 🤔](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) 
* from [Host 🤗 domains](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) 
* to [Notifier 📣 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>).




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
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/$ 📣 Notifier domain.md>) name
||`Subject`|string|`Prompt@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) ID from [`Converse@Notifier`](<21 🤵🐌📣 Converse.md>)
|      |`ChatID`  |uuid  | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Prompt@Broker`](<../../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>)
|      |`PromptID`|uuid  | [Prompt 🤔](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) ID from [`Prompt@Broker`](<../../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>)
|      |`Sender`  |string| [Host 🤗](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) from [`Prompt@Broker`](<../../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>)
|