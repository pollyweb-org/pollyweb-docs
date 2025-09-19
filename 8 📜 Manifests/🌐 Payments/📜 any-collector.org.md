
# 📜 any-collector.org
<!--# 🏳️🏦 https://quip.com/vbUAAxbmqgnY/-AnyCollectoruk-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: any-collector.org
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
      - any-payer.org
      - any-exchange.org
      - any-bank.org
      
