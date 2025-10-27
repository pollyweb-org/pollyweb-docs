<!-- TODO -->

# 👥🚀⏰ Export @ Alarm

> Purpose

* Lists all alarms
* Allows domains to migrate


<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-alarm.dom
    Subject: Export@Alarm
```

<br/>

## Synchronous Response 

```yaml
Triggers:
- When: 2023-04-01T05:00:30.001000Z
  Hook: my-hook
```