<!-- Docs: -->
<!-- Source: -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L116 -->

<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

# 🤗🐌🤵 Goodbye @ Broker

> Purpose

* The [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
    * informs the [user's Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) 
    * of the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ending.

> Used in
* [👋 Goodbye @ Host ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Goodbye 🤗⏩👋/🤗 Goodbye ⏩ flow.md>) 
* [👋 Talker `GOODBYE` command](<../../../../35 💬 Chats/Scripts 📃/📃 methods 🤵/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-host.dom
    To: any-broker.dom
    Subject: Goodbye@Broker
    
Body:
    Chat: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>)
||`Subject` | string | `Goodbye@Broker`
|Body|`Chat`   | uuid    | ID of the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
|