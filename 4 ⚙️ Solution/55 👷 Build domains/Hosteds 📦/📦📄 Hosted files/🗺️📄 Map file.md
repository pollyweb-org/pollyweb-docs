# 🗺️📄 Map file

> Part of [Hosted 📦 domain](<../📦👥 Hosted domain.md>)

<br/>

1. **What is a Map file?**

    The `🗺️ Map.yaml` file
    * indexes the [Resources 🗂️ folder](<🗂️📂 Filer folder.md>)
    * and the [Tables 🪣 folder](<🪣📂 Tables folder.md>)
    * to be used by the [Talker `GET` command](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets/GET ⏬ item.md>).
    
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
            Endpoint: https://rest.any-domain.dom/Items/{$key}
    ```

    ---
    <br/>    
