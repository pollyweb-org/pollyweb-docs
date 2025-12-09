# 🤝 SaveSequence 🚀 call

```yaml
Header:
    From: any-domain.dom
    To: any-biller.dom
    Subject: SaveSequence@Biller

Body:
    Name: AnySequence
    Reset: YEARLY    # Optional, reset period
    Base: 1000       # Optional, base on reset
    Next: 1234       # Optional, next number to set
```

<br/>

## FAQ

1. **Why not an async message?**

    Using a synchronous call allows for immediate confirmation of success, ensuring that the client domain can proceed with its operations without delay.

    ---
    <br/>