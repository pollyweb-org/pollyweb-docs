<!-- TODO: detail -->

# 👥🚀🛢 Transact

```yaml
Header:
    From: any-talker.dom
    To: any-itemizer.dom
    Subject: Transact@Itemizer

Body:
    Blame: SaveToken

    Saves:
      - Pool: MyPool
        Key: my-item-key
        Timeout: 30 days
        Data: {...}

    Deletes:
      - Pool: Pool2
        Key: another-item-key
        Timeout: 30 days
```