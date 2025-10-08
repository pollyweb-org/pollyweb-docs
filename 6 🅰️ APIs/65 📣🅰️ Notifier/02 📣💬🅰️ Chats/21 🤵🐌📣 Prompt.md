# 🤵🐌📣 Prompt @ Notifier

> [Brokers 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) forward   [Prompts 🤔](<../../../9 😃 Talkers/3 Prompts/10 🤔📘 Prompt definitions/01 🤔 Prompt.md>) from [Host 🤗 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to [Notifier 📣 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>).

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) flow.



<br/>

## 🐌 Async Message

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
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) name
||`Subject`|string|`Prompt@Notifier`
|Body  |`WalletID` |uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) ID from [`Onboard@`](<../01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|      |`ChatID`  |uuid  | Chat ID 
|      |`PromptID`|uuid  | [Prompt 🤔](<../../../9 😃 Talkers/3 Prompts/10 🤔📘 Prompt definitions/01 🤔 Prompt.md>) callback on the Host domain
|      |`Sender`  |string| [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) or agent domain name
|