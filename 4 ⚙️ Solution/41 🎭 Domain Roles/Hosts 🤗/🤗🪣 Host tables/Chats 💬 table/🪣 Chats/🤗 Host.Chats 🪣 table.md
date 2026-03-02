# 🤗💬 Host.Chats 🪣 table

> Part of [Host 🤗 domain role](<../../../🤗 Host role/🤗🎭 Host role.md>)

> Purpose
* Stores the content of [`Hello@Host`](<../../../🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)

> Data access
* Saved by the [`CHAT`](<../../../🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) command
* Loaded into the [`$.Chat` 🧠 holder](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 

<br/>

## Lifecycle

![alt text](<🤗 Host.Chats ⚙️ table.png>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
Prefix: Host
Name: Chats
Item: Chat
Key: Broker, Chat
```

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    AllOf: Broker, Chat, PublicKey, Timezone, Language
    Texts: PublicKey, Timezone
    UUIDs: Chat
    Broker.IsDomain:
    Language.IsLanguage:
```
Uses: [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsLanguage`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLanguage ⓕ.md>) 

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
Chat: <chat-uuid>       # Key
Broker: any-broker.dom  # Key
```

From the [`Chat@Broker` 🚀 call](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 🚀 call.md>)

```yaml
PublicKey: <public-key> # To verify Wallet messages
Timezone: UTC+1         # For formatting dates
Language: en-us         # For translations

# Locator
Schema: pollyweb.org/THING
Key: MY-THING-ID
Parameters: 
    Param1: Value1
    Param2: Value2

# Shares
SharedBinds: 
    - <bind-#1-uuid>
    - <bind-#2-uuid>
SharedTokens:
    - <token-#1-uuid>
    - <token-#2-uuid>
```

From the [`OnChatBinds` 🔔 handler](<../🪣🔔 12 Binds/🤗 OnChatBinds 🔔 handler.md>)

```yaml
# List of enriched binds
Binds: 
  <bind-uuid-1>:
    ID: <bind-uuid-1>
    Schema: any-authority.dom/ANY-SCHEMA
    Reference: ref-1
    
# Bind of type .BIND, if any
Wallet: <bind-uuid-2>
```

From the [`OnChatTokens` 🔔 handler](<../🪣🔔 13 Tokens/🤗 OnChatTokens 🔔 handler.md>)

```yaml
Tokens: 
  <token-uuid-1>:
    ID: <token-uuid-1>
    Issuer: issuer-1.dom
    Schema: any-authority.dom/ANY-SCHEMA
```

From the [`EMOJI`](<../../../🤗⌘ Host cmds/EMOJI 😶/😶 EMOJI ⌘ cmd.md>) command

```yaml
Emoji: 🤖
```

| Property | Type | Details
|-|-|-
| `Broker`  |text| [Broker 🤵 domain](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) name
| `Chat`    | uuid | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID
| `PublicKey` |text| From [`Hello@Host`](<../../../🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| `Timezone` |text| Timezone code, e.g. `UTC+1`, `PST`
| `Language` |text| Language code, e.g. `en-us`
| `Binds`    |[set](<../../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>)| of [`Vault.Binds` 🪣](<../../../../Vaults 🗄️/🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>) items
| `Tokens`   |[set](<../../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>)| of [`Issuer.Tokens` 🪣](<../../../../Issuers 🎴/🎴🪣 Issuer tables/Tokens 🎫 table/🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>) items
| 

<br/>