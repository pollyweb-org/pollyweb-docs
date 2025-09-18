<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZeda25d5a05a3470a994e6689d -->


# 🤵🐌🗄️ Suppress @ Vault


> A [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) notifies the [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) 
> * of a checked out [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) 
> * where the user was asked to share information from the [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) 
> * although the broker doesn’t know if the user actually approved the discloser or not.
>
## Message 🐌

|Property|Type|Description
|-|-|-
| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
| `To` | string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
| `Subject` | string | `Suppress@Vault`
| `Consumer` | string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>)
| `ChatID`| UUID | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID

```yaml
Header:
    From: any-broker.com
    To: any-vault.com
    Subject: Suppress@Vault
Body:
    Consumer: any-consumer.com
    ChatID: <chat-uuid>
```