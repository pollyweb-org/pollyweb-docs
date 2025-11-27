# 🗄️ OnOfferOffered 📃 handler

> Implementation 
* Part of the [Vault 🗄️ domain](<../../../🗄️ Vault/🗄️🎭 Vault role.md>)

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that reacts to the [`BIND` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>), 
    * which is implemented by the [`BIND` 📃 script](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND 📃 script.md>).

<br/>

## Diagram

![alt text](<🗄️ OnOfferOffered ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnOfferOffered:

# Assert the Offer
- ASSERT|$Offer:
    AllOf: Broker, Hook, Chat, Schemas
    Texts: Broker
    UUIDs: Hook, Chat
    Lists: Schemas

# Send the message to the Broker
- SEND:
    Header:
        To: $Offer.Broker
        Subject: Bind@Broker
    Body:
        Chat: $Offer.Chat
        Offer: $Offer.ID
        Schemas: $Offer.Schemas
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Vault.Binds`](<../../Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Bind@Broker` 🅰️ method](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
|