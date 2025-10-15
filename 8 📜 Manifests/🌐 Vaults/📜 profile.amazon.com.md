
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>): profile.amazon.com
<!--# 🧢 https://quip.com/XsoCA8E6EEU9/-AnyPersonacom-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: profile.amazon.com
  Name: Amazon
  
Trusts:
  
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      

  # Trust all requests from anyone.
  - Role: CONSUMER
    Query: nlweb.org/PERSONA/*
    