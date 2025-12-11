# ⭐🐌🤗 Rated@Host

> About
* Part of [Host 🤗 domain](<../../🤗 Host role/🤗🎭 Host role.md>)

<br/>

## Asynchronous Message ⭐🐌

```yaml
Header:
    From: any-reviewer.dom
    To: any-host.dom
    Subject: Rated@Host

Body:
    Rate: <rate-uuid>   # for replying
    Form: AnyForm       # last Inform@Broker, if any
    Stars: 4            # from 1 to 5
    Feedback: Could be faster and cheaper.
```

|Object|Property|Type|Description | Origin
|-|-|-|-|-
| Header    |`From`|text| [Reviewer ⭐](<../../../../50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) name | 
| |`To`|text| [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) name | 
| | `Subject`     | string    | `Rated@Host`
| Body      | `Rate`    | uuid      | [Reviewer ⭐](<../../../../50 🫥 Agent domains/Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) hook
| | `Form`    | text      | Last [Consumer 💼](<../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) form | [`Inform@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
| | `Stars`   | num       | Rating from 1 to 5
| | `Feedback`| text      | Optional  message