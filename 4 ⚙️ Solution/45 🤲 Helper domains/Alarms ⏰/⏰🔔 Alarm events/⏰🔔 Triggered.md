<!-- TODO -->

# ⏰🔔 Triggered @ Alarm

> Triggers an alarm set by the [`Trigger@Alarm` 🅰️ method](<../⏰🅰️ Alarm methods/👥🐌⏰ Trigger/👥🐌⏰ Trigger.md>)


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
| Header    | `From`        | string    | [Alarm ⏰](<../⏰🤲 Alarm helper.md>) domain
|           | `To`          | string    | Domain from [`Trigger@Alarm`](<../⏰🅰️ Alarm methods/👥🐌⏰ Trigger/👥🐌⏰ Trigger.md>)
|           | `Subject`     | string    | `Triggered@Alarm`
| Body      | `Hook`        | object    | Object set by [`Trigger@Alarm`](<../⏰🅰️ Alarm methods/👥🐌⏰ Trigger/👥🐌⏰ Trigger.md>)
|