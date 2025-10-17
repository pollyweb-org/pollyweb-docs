
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest.md>): any-collector.dom
<!--# 🏳️🏦 https://quip.com/vbUAAxbmqgnY/-AnyCollectoruk-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: any-collector.dom
  Name: Any Collector

  
Trusts:


  # Expose only to certain exchanges.
  - Role: CONSUMER
    Query: nlweb.dom/PAY/COLLECTOR
    Domains:
      - any-exchange.dom
      

  # Collect from limited payers.
  - Role: VAULT
    Query: nlweb.dom/PAY/PAYMENT
    Domains: 
      - any-payer.dom
      - any-exchange.dom
      - any-bank.dom
      