<!-- Docs: -->
<!-- Code: -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L116 -->


# 🤗🐌🤵 Goodbye @ Broker

* The [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) 
    * informs the [user's Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) 
    * of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ending.
* Used in:
    * [👋 Goodbye @ Host ⏩ flow](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/⏩ Host flows/37 🤗⏩🧑‍🦰 Goodbye 👋 flow.md>) 
    * [👋 Talker `GOODBYE` command](<../../../9 😃 Talkers/60 ⏩ Msg flows/50 👋 GOODBYE.md>)

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
|Header|`From`     | string  | [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)
||`Subject` | string | `Goodbye@Broker`
|Body|`ChatID`   | uuid    | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) 
|