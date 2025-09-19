
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>): any-firewall.org

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: any-firewall.org
  Name: AWS Trust Firewall

  
Trusts:
  
  - Title: Block malicious domains from asking user to share information, and vaults from sharing it.
    Action: REVOKE
    Domains:
      - imgur.com
      - torrentfreak.com
      - requestservice.live
      - atm.any-fintech.org
      