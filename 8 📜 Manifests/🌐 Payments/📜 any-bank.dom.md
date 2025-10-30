
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): any-bank.dom
<!--# 🧪🏧 https://quip.com/I3iqAi8aUTjg/-Cash-Machine-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: any-bank.dom
  Name: Any Bank


Trusts: 

  # Trust the placeholders.
  - Query: nlweb.dom/BANK/*
    Domain: bank.nlweb.dom


  # Pay to limited collectors.
  - Role: CONSUMER
    Queries: 
      - nlweb.dom/PAY/PAYER
      - nlweb.dom/PAY/PAYMENT
    Domains: 
      - any-collector.dom