# 🔆 Hosted `Locators` file

> Part of [Hosted 🧑‍💻 domain](<01 🧑‍💻 Hosted domain.md>)

<br/>

1. **What is the Locators file?**

    The `🔆 Locators.yaml` file 
    * contains the mapping 
    * of [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) resource keys
    * to [Talker 😃 files](<15 😃📄 Talkers folder.md>)
    
    ---
    <br/>

1. **What does the Locators file looks like?**

    ```yaml
    # 🔆 Locators.yaml

    Locators:
        $: $resource-1 # default
        resource-1: talker-1
        resource-2: talker-2
    ```  

    | Property | Type | Description
    |-|-|-
    | `Locators` | map | Resource keys to [Talker 😃 files](<15 😃📄 Talkers folder.md>).

    ---
    <br/>