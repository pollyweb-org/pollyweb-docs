<!-- TODO -->

# ⏰🔔 Triggered @ Alarm

> Triggers an alarm set by the [`Trigger@Alarm` 🐌 msg](<../⏰📨 Alarm msgs/Trigger 👥🐌⏰/⏰ Trigger 🐌 msg.md>)


## Async Event 🔔

```yaml
Header:
    From: any-alarm.dom
    To: any-domain.dom
    Subject: Triggered@Timer

Body:
    Hook: {object}
```


|Object|Property|Type|Description
|-|-|-|-
| Header    |`From`|text| [Alarm ⏰](<../⏰🤲 Alarm helper.md>) domain
|           |`To`|text| Domain from [`Trigger@Alarm`](<../⏰📨 Alarm msgs/Trigger 👥🐌⏰/⏰ Trigger 🐌 msg.md>)
|           | `Subject`     | string    | `Triggered@Alarm`
| Body      | `Hook`        | object    | Object set by [`Trigger@Alarm`](<../⏰📨 Alarm msgs/Trigger 👥🐌⏰/⏰ Trigger 🐌 msg.md>)
|