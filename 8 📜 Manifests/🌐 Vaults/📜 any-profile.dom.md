
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest.md>): any-profile.dom

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: any-profile.dom
  Name: Any Persona

Trusts:
  
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
    
  # Trust all requests from anyone.
  - Role: CONSUMER
    Query: nlweb.dom/PERSONA/*
    