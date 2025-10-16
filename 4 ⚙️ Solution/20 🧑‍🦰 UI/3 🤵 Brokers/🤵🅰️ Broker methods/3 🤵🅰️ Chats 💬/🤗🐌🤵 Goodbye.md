<!-- Docs: -->
<!-- Code: -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L116 -->


# 🤗🐌🤵 Goodbye @ Broker

* The [Host 🤗 domain](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) 
    * informs the [user's Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) 
    * of the [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ending.
* Used in:
    * [👋 Goodbye @ Host ⏩ flow](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Goodbye 👋.md>) 
    * [👋 Talker `GOODBYE` command](<../../../../35 💬 Chats/😃 Talkers/😃📨 Talker msgs/50 👋 GOODBYE.md>)

<br/> 

## Async Message 🐌

```yaml
Header:
    From: any-host.com
    To: any-broker.com
    Subject: Goodbye@Broker
    
Body:
    ChatID: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>)
||`Subject` | string | `Goodbye@Broker`
|Body|`ChatID`   | uuid    | ID of the [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
|