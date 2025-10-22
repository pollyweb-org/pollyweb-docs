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
        Hook: MyPool1-Script
        Data: {...}

    Deletes:
      - Pool: Pool2
        Key: another-item-key
        Hook: MyPool2-Script
        Timeout: 30 days
```