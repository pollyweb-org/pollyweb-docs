# 🤲 Hosted `Helpers` file

> Part of [Hosted 📦 domain](<../📦👥 Hosted domain.md>)

<br/>


1. **What is the Helpers file?**

    The `🤲 Helpers.yaml` file 
    * contains the configuration
    * of required [Helper 🤲 domains](<../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>).
    
    ---
    <br/>

1. **What does the Helpers file look like?**

    ```yaml
    # 🤲 Helpers.yaml
    
    Listeners: # to send Manifest 📜 updates.
        - listeners.pollyweb.org
        - any-listener.dom

    Graphs: # to verify Trust 🫡 chains.
        - any-graph.dom

    Collector: # To receive payments.
        - any-collector.dom
    ```

    ---
    <br/>
