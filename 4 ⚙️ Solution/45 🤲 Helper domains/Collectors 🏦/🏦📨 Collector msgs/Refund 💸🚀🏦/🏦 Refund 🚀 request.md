<!-- #TODO -->


# 💸🚀🏦 Refund @ [Collector](<../../🏦 Collector/🏦🤲 Collector helper.md>)


## Synchronous Call 🚀

|Object|Property|Type|Description
|-|-|-|-
| Header |`From`| string
||`To`|string
||`Subject` |text| `Refund@Collector`
|Body| `ChargeID` | uuid

```yaml
Header:
    From: any-seller.dom
    To: any-collector.dom
    Subject: Refund@Collector

Body:
    ChargeID: <charge-uuid>
```
