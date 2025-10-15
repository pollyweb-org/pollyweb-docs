
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>): any-payer.org
<!--# 🇺🇸💳 https://quip.com/otqrA6r0s9cC/-AnyPayercom-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: any-payer.org
  Name: Any Payer

  
Trusts:


  # Pay to limited collectors.
  - Role: CONSUMER
    Queries: 
      - nlweb.org/PAY/PAYER
      - nlweb.org/PAY/PAYMENT
    Domains: 
      - any-collector.org
      - any-exchange.com
      - any-exchange.org
      