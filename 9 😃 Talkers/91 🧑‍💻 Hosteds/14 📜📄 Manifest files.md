# 📜 Hosted `Manifest` file

> Part of [Hosted 🧑‍💻 domain](<01 🧑‍💻 Hosted domain.md>)

<br/>


1. **How to break the Manifest file when too big?**

    To break a [domain Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) file, replace it with a folder of the same name, then create the following structure.

    * `📜 Manifest/` → folder instead of a file.
        * [`📜 Identity.yaml`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/04 👥🚀🕸 Identity.md>) 
        * `🧩 Codes/` 
            * `GROUP-A/`
                * [`🧩 CODE-A1.yaml`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>)
                * [`🧩 CODE-A2.yaml`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>)
        * `✏️ Forms/` → tree of flows   
            * [`✏️ FORM-1.yaml`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/01 👥🚀🕸 Form.md>)
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