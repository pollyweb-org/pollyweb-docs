<!-- #TODO -->

<!-- Docs: https://quip.com/TkhkAIHSg8Pp#temp:C:TQG4873a67282734b3184e268682 -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/payments/collector/COLLECTOR_TESTS.py#L95 -->

# 💸🚀🏦 Refund @ [Collector](<../../4 ⚙️ Solution/45 Helpers/18 🏦 Collectors/01 🏦🛠️ Collector helper.md>)


## Synchronous Request 🚀

|Object|Property|Type|Description
|-|-|-|-
| Header | `From` | string
|| `To` | string
||`Subject` | string | `Refund@Collector`
|Body| `ChargeID` | uuid

```yaml
Header:
    From: any-seller.com
    To: any-collector.com
    Subject: Refund@Collector

Body:
    ChargeID: <charge-uuid>
```
