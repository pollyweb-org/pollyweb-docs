# 📜 Hosted `Manifest` folder

> Part of [Hosted 🧑‍💻 domain](<01 🧑‍💻 Hosted domain.md>)

<br/>


1. **What is the Manifest folder?**

    The `📜 Manifest/` folder 
    * contains the [domain Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) parts
    * broken into multiple files and folders.
    
    ---
    <br/>

1. **What are the advantages of multiple files?**

    Advantage | Details
    |-|-
    |`Maintenance` | Multiple files change in a granular fashion.
    |`Resilience` | If one file has an error, the others still work.
    |`Size limits`| Independent parts don't hit cloud size limits. 
    

    ---
    <br/>

1. **What is the structure of a Manifest?**

    * `📜 Manifest/` 
        * [`👥 Identity.yaml`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/04 👥🚀🕸 Identity.md>) 
        * `📝 Forms/`   
            * [`📝 FORM-1.yaml`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/01 👥🚀🕸 Form.md>)
        * `🧩 Codes/` 
            * [`🧩 CODE-1.yaml`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>)
            * `GROUP-A/`
                * [`🧩 CODE-A2.yaml`](<../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>)
        * `👍 Trusts/` 
            * [`👍 TRUST-1.yaml`](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) 
            * `GROUP-C/`
                * [`👍 TRUST-C2.yaml`](<../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) 
        * `🪢 Services/` 
            * `🪢 INTEGRATION-1.yaml`
            * `GROUP-S/`
                * `🪢 INTEGRATION-S2.yaml`

    ---
    <br/>