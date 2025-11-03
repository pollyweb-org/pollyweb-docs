# 👥🚀🪵 Start @ Logger

> Purpose
* Initiates a log thread.

## Synchronous Request

```yaml
Header:
    From: any-domain.dom
    To: any-logger.dom
    Subject: Start@Logger

Body:
    Delete: 1 day
    Types: 
        - my-type-1
        - my-type-2
```

## Synchronous Response

```yaml
Thread: <thread-uuid>
```