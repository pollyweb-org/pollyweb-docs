
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): any-collector.dom


```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: any-collector.dom
  Title: Any Collector

  
Trusts:


  # Expose only to certain exchanges.
  - Role: CONSUMER
    Query: pollyweb.org/PAY/COLLECTOR
    Domains:
      - any-exchange.dom
      

  # Collect from limited payers.
  - Role: VAULT
    Query: pollyweb.org/PAY/PAYMENT
    Domains: 
      - any-payer.dom
      - any-exchange.dom
      - any-bank.dom
```      