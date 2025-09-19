
<!--# 🇺🇸💳 https://quip.com/otqrA6r0s9cC/-AnyPayercom-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: any-payer.org
  Name: AnyPayer

  
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
      
