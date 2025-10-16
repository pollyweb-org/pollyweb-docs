
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): any-payer.dom
<!--# 🇺🇸💳 https://quip.com/otqrA6r0s9cC/-AnyPayercom-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: any-payer.dom
  Name: Any Payer

  
Trusts:


  # Pay to limited collectors.
  - Role: CONSUMER
    Queries: 
      - nlweb.dom/PAY/PAYER
      - nlweb.dom/PAY/PAYMENT
    Domains: 
      - any-collector.dom
      - any-exchange.com
      - any-exchange.org
      