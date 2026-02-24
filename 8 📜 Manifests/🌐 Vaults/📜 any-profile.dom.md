
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): any-profile.dom

```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: any-profile.dom
  Title: Any Persona

Trusts:
  
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
    
  # Trust all requests from anyone.
  - Role: CONSUMER
    Query: pollyweb.org/PERSONA/*
```