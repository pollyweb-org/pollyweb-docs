# 🤵🪣 Chats @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)



## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chats
Key: ID

Parents:
    Wallet: { Wallets.ID: Chats.Wallet }
    Host: { Domains.Name: Chats.Host }

Propagate:
    - Host

Children:
    Chatters: { Chatters.Chat: Chats.ID }

Handlers:
    
    OnChatChanges:          # On insert, updated, delete
        Events: ALTERED     # >> call Updated@Notifier
    
    OnChatLocated:          # On Locate@Broker
        Events: INSERTED    # >> call Open@Notifier
    
    OnChatOpened:           # On Opened@Broker
        Events: UPDATED     # >> call Present@Finder
        Assert: 
            New.Status: OPENED

    OnChatPresented:        # On Presented@Broker
        Events: UPDATED     # >> call Hello@Host
        Assert: 
            New.Status: PRESENTED

    OnChatTerminated:       # On Join@Broker + Terminate
        Events: UPDATED     # >> call Terminated@Host
        Assert: 
            New.Status: TERMINATED

    OnChatWrapped:          # On Wrap@Broker
        Events: UPDATED     # >> call @Advertise
        Assert:
            New.Status: WRAPPED
```

## Links

| Link | Table | Contains
|-|-|-
| Parents   | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>) | [Wallets 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|           | [`Domains` 🪣](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
| Children | [`Chatters` 🪣](<../../Chatters 👥 table/🤵 Broker.Chatters 🪣 table.md>) | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants


## Handlers

| [Handler 🔔](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) | [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
|-|-
|[`OnChatChanges` 📃](<../🪣🔔 OnChatAltered/🤵 OnChatAltered 📃 handler.md>) | [`Update@Notifier` 🅰️ ](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)


## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Chats|<chat-id>

ID: <chat-uuid>
Wallet: <wallet-uuid>

# Host info
Host: any-host.dom
Host$: Any Host
Emoji: 😃

# For Wallets to sign messages
PrivateKey: <PrivateKey>

# For domains to verify Wallet messages
PublicKey: <PublicKey>

# Origin chat (if any)
Origin: <origin-chat-uuid>
```

Property|Type|Details|Origin|Purpose
|-|-|-|-|-
|`ID`|uuid | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID |[`Assess@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 request.md>)
|`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID | [`Assess@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 request.md>)
|`Host` | text | [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name |[`Assess@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 request.md>)
|`Host$`|text | [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) title |[`Assess@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 request.md>)
|`Emoji`|text | [Manifest 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) emoji |[`Assess@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 request.md>)
|`PublicKey` | text | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) verification |[`Assess@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chat@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 request.md>)
|`Origin` | uuid | Parent [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) |[`Assess@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | [`Introduced@`](<../../../🤵🅰️ Broker methods/Chats 💬 Introduced 🔎🐌🤵/🤵 Introduced 🐌 msg.md>)
|