🤗💬 Host prompts FAQ
===

1. **How can Hosts leverage reference data, like countries?**

    [Hosts 🤗](<03 ✅ 🤗🎭 Host role.md>) can use data sets exposed by [🪣 Dataset](<05 ✅ 🪣🎭 Dataset role.md>) domains.

    ---

1. **How can Hosts protect users from input fatigue?**

    NLWeb advocates for [Hosts 🤗](<04 ✅ 🤗💬 Host chats.md>) to request as little prompts from users as possible - instead, request users to share datasets. 
    * When prompts are inevitable, avoid text prompts - instead, prefer low-effort prompts (e.g., searchable lists with one or many possible options).

    ---

1. **How can admins create chat workflows?**

    [🦜 Talker](<../../../8 ⏳ 🧑‍💻 SDKs/30 ⏳ 💬 Talker SDK/31 ⏳ 😃 Workflow talkers.md>) scripts allow admins to define workflow steps in a single line of YAML, reducing a 10-step workflow into a simple small 10-line YAML file. 
    * These YAML files map to python code snippets for complex operations. 
    * The SDK automatically deploys the python code as cloud functions into the cloud account, and sets up the talk interactions in the account's NLWeb framework. 

    ---

1. **How can Hosts replicate a CRUD application?**

    For create-read-update-and-delete (CRUD) workflows, the NLWeb SDK can dynamically generate the workflows based on [🧩 Schema Definitions](<../../../8 ⏳ 🧑‍💻 SDKs/30 ⏳ 💬 Talker SDK/32 ⏳ 🗂️ CRUD talkers.md>). 
    
    * This simplifies the configuration by allowing domain admins to use YAML files to define the structure of the data to be stored (i.e., entities, properties, and relationships) without needing to define all the workflow steps to manage it.

    ---


## See also:

- [💬 Chats](<01 ✅ 💬 Chat.md>)
- [🧑‍🦰💬 Wallet chats](<02 ✅ 🧑‍🦰💬 Wallet chats.md>)