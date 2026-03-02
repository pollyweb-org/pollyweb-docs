# 🤵🪣 Chats @ Broker table

> Abouts
* Implements the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>)
* Stores [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)

<br/>

## State Transitions


| Flow ⏩ | [State 🛢](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 State.md>) | Blame | Next action | Details
|-|-|-|-|-
|[`Open`](<../🪣🧱 10 Open ⏩ flow/🤵 Broker.Chats.Open ⏩ flow.md>)|[`ASKED`](<../🪣🧱 11 Asked 🔔 event/🤵 OnChatAsked 🔔 handler.md>) |[`Locate` 🐌](<../../../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 📃 handler.md>)| [`Resolve@Printer` 🚀](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️📨 Printer msgs/Resolve 👥🚀🖨️/🖨️ Resolve 📃 handler.md>) | Inserted
||[`RESOLVED`](<../🪣🧱 12 Resolved 🔔 event/🤵 OnChatResolved 🔔 handler.md>) || [`About@Graph` 🚀](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 📃 handler.md>) | Final [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
||[`DETAILED`](<../🪣🧱 13 Detailed 🔔 event/🤵 OnChatDetailed 🔔 handler.md>) || [`Open@Notifier` 🐌](<../../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) | With translations
||[`OPENED`](<../🪣🧱 14 Opened 🔔 event/🤵 OnChatOpened 🔔 handler.md>) |[`Opened` 🐌](<../../../🤵📨 Broker msgs/Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 📃 handler.md>)| [`Present@Finder` 🐌](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎😃 Finder Talkers/Present/🔎 Present 🐌 msg.md>) | Open on [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
||[`ACTIVATED`](<../🪣🧱 16 Activated 🔔 event/🤵 OnChatActivated 🔔 handler.md>)|| [`Hello@Host` 🐌](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | With [Broker 🤵](<../../../🤵/🤵 Broker 🤲 helper.md>) intro
|[`Abandon`](<../🪣🧱 40 Abandon ⏩ flow/🤵 Broker.Chats.Abandon ⏩ flow.md>)|[`ABANDONED`](<../🪣🧱 41 Abandoned 🔔 event/🤵 OnChatAbandoned 🔔 handler.md>)| [`Locate` 🐌](<../../../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) |[`Abandoned@Host` 🐌](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Abandoned 🤵🐌🤗/🤗 Abandoned 🐌 msg.md>) | Abandoned by user
|[`Wrap`](<../🪣🧱 50 Wrap ⏩ flow/🤵 Broker.Chats.Wrap ⏩ flow.md>)|[`WRAPPED`](<../🪣🧱 51 Wrap 🔔 event/🤵 OnChatWrapped 🔔 handler.md>)| [`Goodbye` 🐌](<../../../🤵📨 Broker msgs/Chats 💬 Goodbye 🤗🐌🤵/🤵 Goodbye 📃 handler.md>) ||Closed by [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)
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

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Forms`](<../../Forms 📝 table/🪣 Forms/🤵 Broker.Forms 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)

```yaml
Parents:

    Form: # Active form

    Wallet: # Receiver of Open@Notifier
    
    Host: # Receiver of Hello@Host
        Domains.Name: Chats.Host, 
        Domains.Wallet: Chats.Wallet
```


<br/>

Here's the [Item 🛢 Propagate](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) definition, referencing [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>)

```yaml
Propagate:
    Host # Auto-create a Domain to represent the Host
```

<br/>

The [Item 🛢 Children](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) are: [`Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Forms`](<../../Forms 📝 table/🪣 Forms/🤵 Broker.Forms 🪣 table.md>)

```yaml
Children: 
    - Chatters  # Domains added to the Chat
    - Forms     # Manifest Forms activated on the Chat
```

<br/>

The [Item 🛢 Cascade](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Cascade.md>) deletes are: [`Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) [`Forms`](<../../Forms 📝 table/🪣 Forms/🤵 Broker.Forms 🪣 table.md>)

```yaml
Cascade: Chatters, Forms
```

<br/>

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
Handlers:
    
    # Frontend updates
    ALTERED    >> OnChatAltered:     # call Updated@Notifier

    # Open flow
    ASKED               >> OnChatAsked:     # call Resolve@Printer
    ASKED > RESOLVED    >> OnChatResolved:  # call About@Graph
    RESOLVED > DETAILED >> OnChatDetailed:  # call Open@Notifier
    DETAILED > OPENED   >> OnChatOpened:    # call Present@Finder
    OPENED > PRESENTED  >> OnChatPresented: # add the Broker
    PRESENTED > ACTIVE  >> OnChatActivated: # call Hello@Host or Pop

    # Localize flow
    UPDATED.Language    >> OnChatLocalized: # call Translate@Graph
        
    # Inform flow
    ACTIVE > INFORM     >> OnChatInform:    # call Form@Graph
    INFORM > INFORMED   >> OnChatInformed:  # call Informed@Notifier

    # Abandon flow
    ABANDONED           >> OnChatAbandoned: # call Abandoned@Host

    # Close flow
    WRAPPED             >> OnChatWrapped:   # call @Advertise
```

<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
  
    # Bulk assertions
    AllOf: Wallet
    UUIDs: Wallet, Hook, Origin, Pop
    OneOf: Locator, Host
    Texts: HostTitle, Description, SmallIcon, BigIcon, ChatEmoji
    
    # Field assertions
    Host.IsDomain:
    Language.IsLanguage:
    Locator.IsLocator: 
    ChatEmoji.IsEmoji:
    Emoji.IsEmoji:

    # Possible states
    .State.IsIn: 
        ASKED, RESOLVED, DETAILED, OPENED, PRESENTED, ACTIVE, 
        ABANDONED, WRAPPED
```

Uses: [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsLanguage`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLanguage ⓕ.md>) [`.IsLocator`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLocator ⓕ.md>) [`.IsEmoji`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsEmoji ⓕ.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Pop@Broker, Locate@Broker
ID: <chat-uuid>          # Automatic Chat ID
Hook: <hook-uuid>        # Wallet hook reference
Wallet: <wallet-uuid>    # Wallet reference
```

From [`Locate@Broker` 🐌 handler](<../../../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 📃 handler.md>)

```yaml
Origin: <chat-uuid>      # Origin chat (if any)
Locator: .HOST,any-domain.dom,ANY-LOCATOR  # Locator to parse
```

From [`OnChatAsked` 🔔 handler](<../🪣🧱 11 Asked 🔔 event/🤵 OnChatAsked 🔔 handler.md>)

```yaml
Host: any-host.dom       # Host domain name
Key: ANY-KEY             # Locator key for the Host
Inputs: any-inputs       # Locator inputs
```

From [`OnChatResolved` 🔔 handler](<../🪣🧱 12 Resolved 🔔 event/🤵 OnChatResolved 🔔 handler.md>)

```yaml
Language: en-us          # To change the language of the chat
HostTitle: Any Host      # Host title from a Graph
Description: Bla, bla    # Host description from a Graph
SmallIcon: <base64>      # Host small icon from a Graph
BigIcon: <base64>        # Host big icon from a Graph
HostEmoji: 🤗            # Host emoji from a Graph
```

From [`Opened` 🐌 handler](<../../../🤵📨 Broker msgs/Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 📃 handler.md>)

```yaml
PublicKey: <PublicKey>  # For domains to verify Wallet messages
```

From [`Emoji@Broker` 🚀 handler](<../../../🤵📨 Broker msgs/Chats 💬 Emoji 🤗🚀🤵/🤵 Emoji 📃 handler.md>)

```yaml 
Emoji: 😃   # New chat emoji 
```

From [`Inform@Broker` 🐌 handler](<../../Forms 📝 table/🪣🧱 1 Informed 🔔/🤵 OnFormInformed 🔔 handler.md>)

```yaml
Form: <form-uuid>    # Form being informed about
FormSchemas:         # Schemas collected in the Form
  - .CURATOR/CURATE
  - .PAYER/CHARGE
```