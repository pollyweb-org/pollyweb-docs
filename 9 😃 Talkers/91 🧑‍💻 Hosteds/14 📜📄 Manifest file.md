
1. **How to break the Manifest file when too big?**

    To break a [domain Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) file, replace it with a folder of the same name, then create the following structure.

    * `📜 Manifest/` → folder instead of a file.
        * `📜 Manifest.yaml` → identity section 👥
        * `🧩 Codes/` → tree of schema codes 🧩
            * `GROUP-A/`
                * `🧩 CODE-A1.yaml`
                * `🧩 CODE-A2.yaml`
        * `✏️ Flows/` → tree of flows   
            * `✏️ FLOW-1.yaml`
        * `🪢 Services/` → tree of API integrations 🪢
            * `GROUP-S/`
                * `🪢 INTEGRATION-1.yaml`
                * `🪢 INTEGRATION-2.yaml`
        * `👍 Trusts/` → tree of trusts 👍
            * `GROUP-B/`
            * `GROUP-C/`
                * `👍 TRUST-BC1.yaml`
                * `👍 TRUST-B1.yaml`

    ---
    <br/>