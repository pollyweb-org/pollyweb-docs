# 💼🐌🤵 Identify @ Broker



## Async Message 🐌

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Identify@Broker

Body:
    Chat: <chat-uuid>
    Identity: any-identity.dom
    Biostamp: <biostamp-uuid>
    Identified: <hook-uuid>
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)  | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | ||`To`|string  | [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` |text| `Identify@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Identity` |text| [Identity 🆔](<../../../../50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔 Identity 🫥 agent.md>) name || 
||`Biostamp`  | uuid    | [Identity 🆔](<../../../../50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔 Identity 🫥 agent.md>) biostamp || 
||`Identified`  | uuid    | [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) hook || 
|
