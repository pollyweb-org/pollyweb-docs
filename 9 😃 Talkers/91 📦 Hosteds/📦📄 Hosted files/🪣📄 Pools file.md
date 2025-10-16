# 🪣📂 Pools folder

> Part of [Hosted 📦 domain](<../📦👥 Hosted domain.md>)

<br/>


1. **What is a Pools file?**

    The `🪣 Pools.yaml` file
    * indexes the [Resources 🗃️ folder](<🗃️📂 Resources folder.md>)
    * to be used by the [Talker `MAP` command](<../../30 🗃️ Talker data/61 🪣 MAP item.md>).
    
    ---
    <br/>

1. **How are pools defined?**

    Pools can either be:
    - a single PDF or YAML file on the root of the folder
    - multiple files in a subfolder (e.g., PNG, PDF)
    - or an external HTTP endpoint.

    ```yaml
    Pools:
        myMarkdownFilePool:
            File: /myMarkdownFilePool.md
        myYamlFilePool:
            File: /myYamlFilePool.yaml
        myPdfFolderPool:
            Folder: /myPdfFolder
        myExternalPool:
            Endpoint: https://rest.any-domain.com/Items/{$key}
    ```
    