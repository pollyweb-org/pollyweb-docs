
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>): any-profile.org

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: any-profile.org
  Name: Any Persona
  Resources:
    NLWEB: 🧢 https://quip.com/XsoCA8E6EEU9/-AnyPersonacom
  
Trusts:
  
  - Title: Protection from malicious domains. 
    Action: INHERIT
    Domain: any-firewall.org
      
  - Title: Trust all requests from anyone.
    Role: CONSUMER
    Query: nlweb.org/PERSONA/*
    