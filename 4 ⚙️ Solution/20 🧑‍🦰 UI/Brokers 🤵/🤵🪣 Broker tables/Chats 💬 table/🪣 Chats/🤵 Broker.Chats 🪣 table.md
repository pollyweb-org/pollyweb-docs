# 🤵🪣 Chats @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)

<br/>

## State Transitions


| Flow ⏩ | [State 🛢](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 State.md>) | Handler 🔔 | Next action | Details
|-|-|-|-|-|
|[`Open`](<../🪣🧱 10 Open ⏩ Flow/🤵 Broker.Chats.Open ⏩ flow.md>)|`ASKED`| [`Asked`](<../🪣🧱 11 Asked 🔔 event/🤵 OnChatAsked 🔔 handler.md>) | [`Resolve@Printer` 🚀](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 📃 handler.md>) | 
||`RESOLVED`|[`Resolved`](<../🪣🧱 12 Resolved 🔔 event/🤵 OnChatResolved 🔔 handler.md>) | [`About@Graph` 🚀](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 About/🕸 About 📃 handler.md>) | Final [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
||`DETAILED`|[`Detailed`](<../🪣🧱 13 Detailed 🔔 event/🤵 OnChatDetailed 🔔 handler.md>) | [`Open@Notifier` 🐌](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) | With translations
||`OPENED`|[`Opened`](<../🪣🧱 14 Opened 🔔 event/🤵 OnChatOpened 🔔 handler.md>) | [`Present@Finder` 🐌](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>) | Open on [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
||`PRESENTED`|  [`Presented`](<../🪣🧱 15 Presented 🔔 event/🤵 OnChatPresented 🔔 handler.md>) ||With  [Finder 🔎](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) intro
||`ACTIVATED`|  [`Activated`](<../🪣🧱 16 Activated 🔔 event/🤵 OnChatActivated 🔔 handler.md>)| [`Hello@Host` 🐌](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | With [Broker 🤵](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) intro
|[`Abandon`](<../🪣🧱 30 Abandon ⏩ Flow/🤵 Broker.Chats.Abandon ⏩ flow.md>)|`ABANDONED`|[`Abandoned`](<../🪣🧱 31 Abandoned 🔔 event/🤵 OnChatAbandoned 🔔 handler.md>)| [`Abandoned@Host` 🐌](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Abandoned 🤵🐌🤗/🤗 Abandoned 🐌 msg.md>) | Abandoned by user
|[`Wrap`](<../🪣🧱 40 Wrap ⏩ Flow/🤵 Broker.Chats.Wrap ⏩ flow.md>)|`WRAPPED`|[`Wrapped`](<../🪣🧱 41 Wrap 🔔 event/🤵 OnChatWrapped 🔔 handler.md>)| |Closed by [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)
|

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chats
Item: Chat
```

<br/>

Here's the [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) definition, referencing [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Pops`](<../../Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)

```yaml
Parents:
    
    Pop: # Pop that created the Chat
        Pops.ID: Chats.Pop

    Wallet: # Receiver of Open@Notifier
        Wallets.ID: Chats.Wallet
    
    Host: # Receiver of Hello@Host
        Domains.Name: Chats.Host, 
        Domains.Wallet: Chats.Wallet
```


<br/>

Here's the [Item 🛢 Propagate](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) definition, referencing [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>)

```yaml
Propagate: Host
```

<br/>

Here's the [Item 🛢 Children](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) definition, referencing [`Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)

```yaml
Children: Chatters
```

<br/>

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
Handlers:
    
    # Frontend updates
    ALTERED    >> OnChatAltered:     # call Updated@Notifier

    # Open flow
    ASKED      >> OnChatAsked:       # call Resolve@Printer
    RESOLVED   >> OnChatResolved:    # call About@Graph
    DETAILED   >> OnChatDetailed:    # call Open@Notifier
    OPENED     >> OnChatOpened:      # call Present@Finder
    PRESENTED  >> OnChatPresented:   # add the Broker
    ACTIVE     >> OnChatActivated:   # call Hello@Host or Pop

    # Localize flow
    UPDATED    >> OnChatLocalized:   # call Translate@Graph
        Assert: New.Language    

    # Abandon flow
    ABANDONED  >> OnChatAbandoned:   # call Abandoned@Host

    # Close flow
    TERMINATED >> OnChatTerminated:  # call Terminated@Host
    WRAPPED    >> OnChatWrapped:     # call @Advertise
```

<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    # Bulk assertions
    AllOf: 
    UUIDs: 
    Texts: 

    # Field assertions
    .State.IsIn: ACTIVE, ABANDONED, TERMINATED
    
```

Uses: [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>) [`.IsLanguage`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLanguage ⓕ.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Pop@Broker, Locate@Broker
ID: <chat-uuid>          # Automatic Chat ID
Hook: <hook-uuid>        # Wallet hook reference
Wallet: <wallet-uuid>    # Wallet reference
```

From [`Pop@Broker` 🐌 handler](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>)

```yaml
Pop: <pop-uuid>          # Pop reference
```

From [`Locate@Broker` 🐌 handler](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 📃 handler.md>)

```yaml
Origin: <chat-uuid>      # Origin chat (if any)
Locator: $.Msg.Locator   # Locator to parse on insert
```

From [`OnChatInserted` 🔔 handler](<../🪣🧱 11 Asked 🔔 event/🤵 OnChatAsked 🔔 handler.md>)

```yaml
Host: any-host.dom       # Host domain name
Key: ANY-KEY             # Locator key for the Host
Inputs: any-inputs       # Locator inputs
```

From [`OnChatResolved` 🔔 handler](<../🪣🧱 12 Resolved 🔔 event/🤵 OnChatResolved 🔔 handler.md>)

```yaml
Notifier: any-wallet.dom # Notifier wallet domain
Language: en-us          # To change the language of the chat
HostTitle: Any Host      # Host title from a Graph
Description: Bla, bla    # Host description from a Graph
SmallIcon: <base64>      # Host small icon from a Graph
BigIcon: <base64>        # Host big icon from a Graph
```

From [`Opened` 🐌 handler](<../../../🤵🅰️ Broker methods/Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 📃 handler.md>)

```yaml
PublicKey: <PublicKey>  # For domains to verify Wallet messages
```

From [`Emoji@Broker` 🚀 handler](<../../../🤵🅰️ Broker methods/Chats 💬 Emoji 🤗🚀🤵/🤵 Emoji 📃 handler.md>)

```yaml 
Emoji: 😃                # New chat emoji 
```

<br/>

## Fields

Field|Type|Details|Origin|Purpose
|-|-|-|-|-
|`ID`|uuid | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID | [`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Host` | text | [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Host$`|text | [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) title |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Emoji`|text | [Manifest 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) emoji |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`PublicKey` | text | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) verification |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chat@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Origin` | uuid | Parent [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Presented@`](<../../../🤵🅰️ Broker methods/Chats 💬 Presented 🔎🐌🤵/🤵 Presented 🐌 msg.md>)
|
