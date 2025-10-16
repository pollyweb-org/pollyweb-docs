
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): any-profile.org

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: any-profile.org
  Name: Any Persona

Trusts:
  
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
    
  # Trust all requests from anyone.
  - Role: CONSUMER
    Query: nlweb.dom/PERSONA/*
    