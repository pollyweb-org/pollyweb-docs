# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) `REVIEWER`/`REVIEW`

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)


```yaml
Path: /REVIEWER/REVIEW
Title: Chat review

Fields:
    Rate: For replying
    Form: Last Inform@Broker, if any
    Stars: From 1 to 5
    Feedback: Free text

Asserts:
    AllOf: Rate, Stars
    UUIDs: Rate
    Texts: Feedback, Form
    Stars.IsNum:
    Stars.IsBetween(1,5):
```

Uses: [`.IsNum`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsNum ⓕ.md>) [`.IsBetween`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsBetween ⓕ.md>) [`Inform@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)