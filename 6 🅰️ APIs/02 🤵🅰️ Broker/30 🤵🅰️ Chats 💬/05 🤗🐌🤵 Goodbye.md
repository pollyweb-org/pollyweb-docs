<!-- #TODO -->

<!-- Docs: -->
<!-- Code: -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L116 -->


# 🤗🐌🤵 Goodbye @ Broker


## Properties

| Property | Schema | Notes
|-|-|-
| ServiceID | nlweb.org/HOSTS/RATED
| InteractionID | nlweb.org/HOSTS/RATED
||


## Async Message

```yaml
Header:
    From: any-host.org
    To: any-broker.org
    Subject: Goodbye@Broker
    
Body:
    ChatID: <session-uuid>
    Message: Parking ended for vehicle AB-12-34.
```