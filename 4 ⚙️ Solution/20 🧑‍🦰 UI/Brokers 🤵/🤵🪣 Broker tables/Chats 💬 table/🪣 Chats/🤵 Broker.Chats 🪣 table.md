# 🤵🪣 Chats @ Broker table

> Implements the [Broker 🤵 domain][Broker domain]

> Stores [Chats 💬][Chat]



## Schema

Here's the [Itemized 🛢 schema][Itemized dataset].

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
| Parents   | [`Wallets` 🪣][Wallets] | [Wallets 🧑‍🦰][Wallet app]
|           | [`Domains` 🪣][Domains] | [domains 👥][domains]
| Children | [`Chatters` 🪣][Chatters] | [Chat 💬][Chat] participants


## Handlers

| Event  🔔 | [Handler 📃][Handler] | [Message 📨][Message] | Target
|-|-|-|-
|`ALTERED`|[OnAltered][OnAltered] | [`Update@`][Updated@Notifier method] | [Notifier 📣][Notifier domain]
|`INSERTED`|[OnInserted][OnInserted] | [`Resolve@`][Resolve@] | [Printer 🖨️][Printer helper]
|`RESOLVED`|[OnResolved][OnResolved] | [`About@`][About@] |[Graph 🕸][Graph domain]
|`DETAILED`|[OnDetailed][OnDetailed] | [`Open@`][Open@] | [Notifier 📣][Notifier domain]
|`OPENED`|[OnOpened][OnOpened] | [`Present@`][Present@] | [Finder 🔎][Finder domain]
|`PRESENTED`|[OnPresented][OnPresented] | [`Prompt@`][Prompt@Broker method] | [Notifier 📣][Notifier domain]
|`STARTED`|[OnStarted][OnStarted] | [`Hello@`][Hello@] | [Host 🤗][Host domain]
|`UPDATED`|[OnLocalized][OnLocalized] | [`Translate@`][Translate@] | [Graph 🕸][Graph domain]
|`ABANDONED`|[OnAbandoned][OnAbandoned] | [`Abandoned@`][Abandoned@] | [Host 🤗][Host domain]
|`DONE`|[OnDone][OnDone]
|

## Example

Here's the [`READ` command][READ] result.

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
|`ID`|uuid | [Chat 💬][Chat] ID |[`Locate@`][Locate@]| [`Chats@`][Chat@]
|`Wallet`| uuid | [Wallet 🧑‍🦰][Wallet app] ID | [`Locate@`][Locate@] | [`Chats@`][Chat@]
|`Host` | text | [Host 🤗][Host domain] name |[`Locate@`][Locate@]| [`Chats@`][Chat@]
|`Host$`|text | [Host 🤗][Host domain] title |[`Locate@`][Locate@]| [`Chats@`][Chat@]
|`Emoji`|text | [Manifest 📜][Manifest] emoji |[`Locate@`][Locate@]| [`Chats@`][Chat@]
|`PublicKey` | text | [Wallet 🧑‍🦰][Wallet app] verification |[`Locate@`][Locate@]| [`Chat@`][Chat@]
|`Origin` | uuid | Parent [Chat 💬][Chat] |[`Locate@`][Locate@] | [`Presented@`][Presented@]
|

[Abandoned@]: <../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Abandoned 🤵🐌🤗/🤗 Abandoned 🐌 msg.md>
[About@]: <../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 About/🕸 About 📃 handler.md>
[Broker domain]: <../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>
[Chat]: <../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>
[Chat@]: <../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>
[Chatters]: <../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>
[domains]: <../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>
[Finder domain]: <../../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>
[Graph domain]: <../../../../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph/🕸🤲 Graph helper.md>
[Handler]: <../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>
[Hello@]: <../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>
[Host domain]: <../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>
[Itemized dataset]: <../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>
[Locate@]: <../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>
[Manifest]: <../../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>
[Message]: <../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>
[Notifier domain]: <../../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>
[OnAbandoned]: <../🪣🔔 8 Abandoned/🤵 OnChatAbandoned 📃 handler.md>
[OnAltered]: <../🪣🔔 0 Altered/🤵 OnChatAltered 📃 handler.md>
[OnDetailed]: <../🪣🔔 3 Detailed/🤵 OnChatDetailed 📃 handler.md>
[OnDone]: <../🪣🔔 9 Done/🤵 OnChatDone 📃 handler.md>
[OnInserted]: <../🪣🔔 1 Inserted/🤵 OnChatInserted 📃 handler.md>
[OnLocalized]: <../🪣🔔 7 Localized/🤵 OnChatLocalized 📃 handler.md>
[OnOpened]: <../🪣🔔 4 Opened/🤵 OnChatOpened 📃 script.md>
[OnPresented]: <../🪣🔔 5 Presented/🤵 OnChatPresented 📃 handler.md>
[OnResolved]: <../🪣🔔 2 Resolved/🤵 OnChatResolved 📃 handler.md>
[OnStarted]: <../🪣🔔 6 Started/🤵 OnChatStarted 📃 handler.md>
[Open@]: <../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>
[Present@]: <../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>
[Presented@]: <../../../🤵🅰️ Broker methods/Chats 💬 Presented 🔎🐌🤵/🤵 Presented 🐌 msg.md>
[Printer helper]: <../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>
[Prompt@Broker method]: <../../../🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>
[READ]: <../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>
[Resolve@]: <../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 📃 handler.md>
[Translate@]: <../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 📃 handler.md>
[Updated@Notifier method]: <../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>
[Wallet app]: <../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>
[Wallets]: <../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>
