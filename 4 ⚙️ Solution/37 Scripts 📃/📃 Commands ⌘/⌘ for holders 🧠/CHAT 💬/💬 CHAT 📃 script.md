<!-- TODO -->

# 😃📃 .CHAT 💬 script

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    * that implements the [`CHAT` 💬 command](<💬 CHAT ⌘ cmd.md>) 
    * by setting the [`$.Chat` 💬 holder](<../../../📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>).

## How to run

```yaml
RUN|.CHAT:
    Broker: any-broker.dom
    Chat: <chat-uuid>
    Key: <any-locator-key>
    Role: HOST
    PublicKey: <key>
    Timezone: PST
    Language: en-us
```

## Script

```yaml
# Assert the required fields
- ASSERT|$.Inputs:
    - AllOf: Broker, PublicKey, Role, Chat, Timezone, Language
    - Texts: Broker, PublicKey, Role, Key, Timezone, Language
    - UUIDs: Chat
    - Role.IsIn(VAULT, HELPER, HOST)

# Update the $.Chat
- PUT|$.Chat >> $.Chat:

```