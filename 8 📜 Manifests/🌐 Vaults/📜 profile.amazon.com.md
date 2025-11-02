
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): profile.amazon.dom
<!--# 🧢 https://quip.com/XsoCA8E6EEU9/-AnyPersonacom-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: profile.amazon.com
  Title: Amazon
  
Trusts:
  
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      

  # Trust all requests from anyone.
  - Role: CONSUMER
    Query: nlweb.dom/PERSONA/*
    