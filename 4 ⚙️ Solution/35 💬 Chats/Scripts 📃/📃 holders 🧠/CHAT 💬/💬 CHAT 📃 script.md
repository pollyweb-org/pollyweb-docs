<!-- TODO -->
# 😃📃 .CHAT 💬 script

> Part of [Talker 😃 domain](<../../../Talkers 😃/😃🤲 Talker helper.md>)

> Purpose
* [Script 📃](<../../📃 basics/Script 📃.md>) 
    * that implements the [`CHAT` 💬 command](<💬 CHAT ⌘ cmd.md>) 
    * by setting the [`$.Chat` 💬 holder](<../$.Chat 💬/💬 $.Chat 🧠 holder.md>).

## How to run

```yaml
RUN|.CHAT:
    Broker: any-broker.dom
    Chat: <chat-uuid>
    Key: <any-locator-key>
    Role: AGENT
    PublicKey: <key>
    Timezone: PST
    Language: en-us
```

## Script

```yaml
# Assert the required fields
- ASSERT|$.Inputs:
    AllOf: Broker, PublicKey, Role, Chat
    Texts: Broker, PublicKey, Role, Key
    UUIDs: Chat

# Assert regional settings
- ASSERT|$.Inputs:
    AllOf: Timezone, Language
    Texts: Timezone, Language

# Assert the role enum
- ASSERT|$:Role:
    Enum: AGENT, HELPER, HOST

# Update the $.Chat
- EVAL|$.Chat >> $.Chat:

```