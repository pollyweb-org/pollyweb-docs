
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/📜 Manifest.md>): any-bank.org
<!--# 🧪🏧 https://quip.com/I3iqAi8aUTjg/-Cash-Machine-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: any-bank.org
  Name: Any Bank


Trusts: 

  # Trust the placeholders.
  - Query: nlweb.org/BANK/*
    Domain: bank.nlweb.org


  # Pay to limited collectors.
  - Role: CONSUMER
    Queries: 
      - nlweb.org/PAY/PAYER
      - nlweb.org/PAY/PAYMENT
    Domains: 
      - any-collector.org