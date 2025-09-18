<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZa3f3ba7f94154a2fbd520e931 -->


# 🧑‍🦰🐌🗄️ Disclose @ Vault

> Request for a Vault to share data about a user to a Consumer.

## Message 🐌


|Property|Type|Description
|-|-|-
| `From` | string | [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
| `To` | string | [Vault 🗄️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
| `Subject` | string | `Disclose@Vault`
| `ChatID`| UUID | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
| `Consumer` | string | [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>)
| `Language` | string | ISO language code
| `BindID` | UUID | [Bind 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)



```yaml
Header:
    Subject: Disclose@Vault
Body:
    ChatID: 125a5c75-cb72-43d2-9695-37026dfcaa48
    Consumer: any-coffee-shop.com
    Language: en-us
    BindID: 793af21d-12b1-4cea-8b55-623a19a28fc5
```

## Steps

* Validate the user’s signature in the ✉️ Msg
    * compare with the key in 🪣 Wallets
* Verify if 📡 Consumer is trustable:
    * call 🚀 Trusted: 🕸 Graph (CONSUMER)
* Ask any additional question to the user (e.g., OTP):
    * Add to 🪣 Disclosures
    * Call 🐌 Prompt: 🤵📎 Broker. Prompt
* Send details to 💼 Consumer:
    * Call [Consume @ Consumer 🐌](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>)

---