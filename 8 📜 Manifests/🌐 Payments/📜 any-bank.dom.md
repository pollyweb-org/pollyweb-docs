
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): any-bank.dom
<!--# 🧪🏧 https://quip.com/I3iqAi8aUTjg/-Cash-Machine-->

```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: any-bank.dom
  Title: Any Bank


Trusts: 

  # Trust the placeholders.
  - Query: pollyweb.org/BANK/*
    Domain: bank.pollyweb.org


  # Pay to limited collectors.
  - Role: CONSUMER
    Queries: 
      - pollyweb.org/PAY/PAYER
      - pollyweb.org/PAY/PAYMENT
    Domains: 
      - any-collector.dom
```