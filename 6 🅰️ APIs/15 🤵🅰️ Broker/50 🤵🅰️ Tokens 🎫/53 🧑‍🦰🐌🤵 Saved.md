<!-- #TODO -->

<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTe327e788ccd54eefbe5f7e844 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L88 -->

# 🧑‍🦰🐌🤵 Saved @ Broker



## Async Message

|Property|Type|Description
|-|-|-

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Accepted@Broker

Body:
    ChatID: <session-uuid>
    TokenID: <offer-uuid>
    Issuer: any-host.com
    Path: /storage/tf/creds/<issuer>/<token-uuid>
```