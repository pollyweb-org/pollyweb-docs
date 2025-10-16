
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): any-collector.dom
<!--# 🏳️🏦 https://quip.com/vbUAAxbmqgnY/-AnyCollectoruk-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: any-collector.dom
  Name: Any Collector

  
Trusts:


  # Expose only to certain exchanges.
  - Role: CONSUMER
    Query: nlweb.org/PAY/COLLECTOR
    Domains:
      - any-exchange.org
      

  # Collect from limited payers.
  - Role: VAULT
    Query: nlweb.org/PAY/PAYMENT
    Domains: 
      - any-payer.dom
      - any-exchange.org
      - any-bank.org
      