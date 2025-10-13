# 🔆 Hosted `Locators` file

> Part of [Hosted 🧑‍💻 domain](<01 🧑‍💻 Hosted domain.md>)

<br/>


1. **What does the Locators file looks like?**

    The `🔆 Locators.yaml` file contains the mapping of [Locator 🔆 resources](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) to [Talkers 😃](<../10 📘 Talker specs/10 😃 Talker.md>).

    * Note: only the `resource` part of each [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) is required.

    ```yaml
    🤝: nlweb.org/HOSTER/LOCATORS

    Locators:
        _default: # if no Host Locator is provided.
            Talker: talker-1
        resource-1:
            Talker: talker-1
        resource-2:
            Talker: talker-2
    ```  

