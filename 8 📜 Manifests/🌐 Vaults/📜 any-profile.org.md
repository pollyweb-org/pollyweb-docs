
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/📜 Manifest.md>): any-profile.org

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: any-profile.org
  Name: Any Persona

Trusts:
  
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
    
  # Trust all requests from anyone.
  - Role: CONSUMER
    Query: nlweb.org/PERSONA/*
    