<!-- Docs: -->
<!-- Code: -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L116 -->


# 🤗🐌🤵 Goodbye @ Broker

> The [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) inform the [user's Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ending.

> Used in [🤗⏩🧑‍🦰 Goodbye](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/07 🤗⏩🧑‍🦰 Goodbye 👋.md>).

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
|Header|`From`     | string  | [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
||`Subject` | string | `Goodbye@Broker`
|Body|`ChatID`   | uuid    | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) 
|