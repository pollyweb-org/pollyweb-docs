```yaml
Header:
    From: any-domain.dom
    To: any-logger.dom
    Subject: Export@Logger
Body:
    Thread: <thread-uuid>
    Groups: [my-type-1, my-type-2]
    Blame: my-script
    Period: 5 minutes
    Interval: 
        - 2025-10-10T13:00:00Z
        - 2025-10-10T14:00:00Z
```

```yaml
Logs: 
    - Sent: 2025-10-10T13:45:23.123Z
      Log: {...}
```