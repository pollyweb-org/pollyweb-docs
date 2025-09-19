<!--# 🧢 https://quip.com/XsoCA8E6EEU9/-AnyProfilecom-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: profile.amazon.com
  Name: Amazon
  
Trusts:
  
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      

  # Trust all requests from anyone.
  - Role: CONSUMER
    Query: nlweb.org/PROFILE/*
    
