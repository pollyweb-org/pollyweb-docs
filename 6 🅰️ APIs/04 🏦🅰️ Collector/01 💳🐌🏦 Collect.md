<!-- #TODO -->

<!-- Docs: https://quip.com/TkhkAIHSg8Pp#temp:C:TQGa949e2cdc69f4d63900ca6c1b -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/payments/collector/COLLECTOR_TESTS.py#L16 -->


# 💳🐌🏦 Collect @ [Collector](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>)


## Async Message 🐌

|Property|Type|Description
|-|-|-


* Header:
   * From: `any-payer.com`
   * To: `collector.com`
   * Subject: `Collect@Collector`
* Body:
   * Session: 
      * Host: `any-seller.com`
      * Broker: `any-broker.com`
      * Locator: `<any-locator>`
      * SessionID: `<session-uuid>`
   * Charge: 
      * ChargeID: `<charge-uuid>`
      * Operation: `DEBIT`
      * Amount: `10.54`
      * Currency: `USD`
      * Collectors [ `any-collector.com` ]
   * Transaction: { "a", "1" }


---