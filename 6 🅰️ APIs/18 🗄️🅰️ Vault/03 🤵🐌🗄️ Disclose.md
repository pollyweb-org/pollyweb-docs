<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZa3f3ba7f94154a2fbd520e931 -->


# 🧑‍🦰🐌🗄️ Disclose @ Vault

> Request for a Vault to share data about a user to a Consumer.

## Message 🐌


|Object|Property|Type|Description
|-|-|-|-
| Header| `From` | string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|| `To` | string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) name
|| `Subject` | string | `Disclose@Vault`
|Body| `ChatID`| UUID | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
|| `Consumer` | string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
|| `Language` | string | ISO language code
|| `BindID` | UUID | [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) ID



```yaml
Header:
    From: any-broker.com
    To: any-broker.com
    Subject: Disclose@Vault
    
Body:
    ChatID: <chat-uuid>
    Consumer: any-coffee-shop.com
    Language: en-us
    BindID: <bind-uuid>
```
<br/>

## Steps

* Validate the signature of the message
* Verify if the Consumer is trustable
* Ask any additional question to the user (e.g., OTP)
* Send the data to the Consumer

---