<!-- #TODO -->

<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->


# 🤵🐌📣 Prompt @ Notifier

> Domains send prompts for users to read or reply to.

> The response goes directly to the sender.


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
|Header|`From`|string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`To`|string| [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>) name
||`Subject`|string|`Prompt@Notifier`
|Body  |`WalletID` |UUID  | Wallet ID 
|      |`ChatID`  |UUID  | Chat ID 
|      |`PromptID`|UUID  | [Prompt 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/02 🤔 Prompt.md>) callback on the Host domain
|      |`Sender`  |string| [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) or agent domain name
|