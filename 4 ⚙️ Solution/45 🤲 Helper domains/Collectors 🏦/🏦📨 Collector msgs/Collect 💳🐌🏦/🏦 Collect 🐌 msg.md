<!-- #TODO -->


# 💳🐌🏦 Collect @ [Collector](<../../🏦 Collector/🏦🤲 Collector helper.md>)


## Async Message 🐌

|Property|Type|Description
|-|-|-

```yaml
Header:
   From: any-payer.dom
   To: collector.dom
   Subject: Collect@Collector
   
Body:
   Session: 
      Host: any-seller.dom
      Broker: any-broker.dom
      Locator: <any-locator>
      SessionID: <session-uuid>
   Charge: 
      ChargeID: <charge-uuid>
      Operation: DEBIT
      Amount: 10.54
      Currency: USD
      Collectors: 
         - any-collector.dom
   Transaction: 
      a: 1
```


---