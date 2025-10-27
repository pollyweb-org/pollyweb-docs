# 👥🐌⏰ Trigger @ Alarm

> Purpose

* Registers an alarm to be triggered by the [`Triggered@Alarm` 🔔 event](<../../⏰🔔 Alarm events/⏰🔔 Triggered.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-domain.dom
    To: any-alarm.dom
    Subject: Trigger@Timer

Body:
    When: 2023-04-01T05:00:30.001000Z
    Hook: {object}
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | Any domain setting the alarm
|           | `To`          | string    | [Alarm ⏰](<../../⏰🤲 Alarm helper.md>) domain
|           | `Subject`     | string    | `Trigger@Alarm`
| Body      | `When`        | time | When to trigger the alarm
|           | `Hook`        | object    | Object to return by [`Triggered@Alarm`](<../../⏰🔔 Alarm events/⏰🔔 Triggered.md>)
|