<!-- #TODO -->

<!-- Docs: -->
<!-- Code: -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L135 -->


# 🧑‍🦰🐌🤵 Unbind @ Broker

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Unbind@Broker
Body:
    BindID: <bind-uuid>
```

|Property|Type|Description
|-|-|-