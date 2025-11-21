# 🤵🪣 Chats @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)



## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chats
Item: Chat
Key: ID

Parents:
    Wallet: { Wallets.ID: Chats.Wallet }
    Host: { Domains.Name: Chats.Host }

Propagate:
    - Host

Children:
    Chatters: { Chatters.Chat: Chats.ID }

Handlers:
    OnChatChanges: ALTERED                   # call Updated@Notifier
    OnChatCreated: CREATED                   # call Translate@Graph
    OnChatLocated: CREATED > LOCATED         # call Open@Notifier
    OnChatOpened: LOCATED > OPENED           # call Present@Finder
    OnChatPresented: OPENED > PRESENTED      # call Hello@Host
    OnChatTerminated: PRESENTED > TERMINATED # call Terminated@Host
    OnChatWrapped: PRESENTED > WRAPPED

Handlers:

    OnChatTerminated:       # On Pop@Broker + Terminate
        Events: UPDATED     # >> call Terminated@Host
        Assert: 
            New.State: TERMINATED

    OnChatWrapped:          # On Wrap@Broker
        Events: UPDATED     # >> call @Advertise
        Assert:
            New.State: WRAPPED
```

## Links

| Link | Table | Contains
|-|-|-
| Parents   | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) | [Wallets 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|           | [`Domains` 🪣](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
| Children | [`Chatters` 🪣](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants


## Handlers


    OnChatChanges: ALTERED                   # call Updated@Notifier
    OnChatCreated: CREATED                   # call Translate@Graph
    OnChatLocated: CREATED > LOCATED         # call Open@Notifier
    OnChatOpened: LOCATED > OPENED           # call Present@Finder
    OnChatPresented: OPENED > PRESENTED      # call Hello@Host
    OnChatTerminated: PRESENTED > TERMINATED # call Terminated@Host
    OnChatWrapped: PRESENTED > WRAPPED

| Event  🔔 | .Status| [Handler 📃](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) | [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
|-|-|-|-
|`ALTERED`||[OnAltered](<../🪣🔔 0 Altered/🤵 OnChatAltered 📃 handler.md>) | [`Update@Notifier` 🅰️ ](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) 
|`INSERTED`||[OnInserted](<../🪣🔔 1 Inserted/🤵 OnChatInserted 📃 handler.md>) | {{Resolve@Printer}}
||`RESOLVED`|[OnResolved](<../🪣🔔 2 Resolved/🤵 OnChatResolved 📃 handler.md>) | {{About@Graph}}
||`DETAILED`|[OnDetailed](<../🪣🔔 3 Detailed/🤵 OnChatDetailed 📃 handler.md>) | {{Open@Notifier}}
||`OPENED`|[OnOpened](<../🪣🔔 4 Opened/🤵 OnChatOpened 📃 script.md>) | {{Present@Finder}}
||`PRESENTED`|[OnPresented](<../🪣🔔 5 Presented/🤵 OnChatPresented 📃 handler.md>)
||`STARTED`|[OnStarted](<../🪣🔔 6 Started/🤵 OnChatStarted 📃 handler.md>)
|`UPDATED`||[OnLocalized](<../🪣🔔 7 Localized/🤵 OnChatLocalized 📃 handler.md>)
||`LEFT`|[OnLeft](<../🪣🔔 8 Left/🤵 OnChatLeft 📃 handler.md>)
||`DONE`|[OnDone](<../🪣🔔 9 Done/🤵 OnChatDone 📃 handler.md>)


## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Chats|<chat-id>

# From Locate@Broker, Pop@Broker
ID: <chat-uuid>         # Automatic Chat ID
Hook: <hook-uuid>       # Wallet hook reference
Origin: <chat-uuid>     # Origin chat (if any)
Wallet: <wallet-uuid>   # Wallet reference
Locator: $.Msg.Locator  # Locator to parse on insert

# From OnChatInserted
Host: any-host.dom      # Host domain name
Key: ANY-KEY            # Locator key for the Host
Inputs: any-inputs      # Locator inputs

# From OnChatResolved
Language: en-us         # To change the language of the chat
HostTitle: Any Host     # Host title from a Graph
Description: Bla, bla   # Host description from a Graph
SmallIcon: <base64>     # Host small icon from a Graph
BigIcon: <base64>       # Host big icon from a Graph

# from Opened@Broker
PublicKey: <PublicKey>  # For domains to verify Wallet messages

# from Emoji@Broker
Emoji: 😃                # New chat emoji 
```

Property|Type|Details|Origin|Purpose
|-|-|-|-|-
|`ID`|uuid | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID | [`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Host` | text | [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Host$`|text | [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) title |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Emoji`|text | [Manifest 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) emoji |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`PublicKey` | text | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) verification |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chat@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Origin` | uuid | Parent [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Presented@`](<../../../🤵🅰️ Broker methods/Chats 💬 Presented 🔎🐌🤵/🤵 Presented 🐌 msg.md>)
|