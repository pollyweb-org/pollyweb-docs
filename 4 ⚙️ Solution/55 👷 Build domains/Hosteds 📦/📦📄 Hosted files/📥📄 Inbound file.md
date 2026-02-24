# 📥 Hosted `Inbound` file

> Part of [Hosted 📦 domain](<../📦👥 Hosted domain.md>)

<br/>

1. **What is the Inbound file?**

    The `📥 Inbound.yaml` file 
    * tells the [Hoster ☁️ domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster helper/☁️ Hoster 🤲 helper.md>) 
    * where to forward [Messages 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) to.

    ---
    <br/>

1. **What does the Inbound.yaml file look like?**

    ```yaml
    # 📥 Inbound.yaml

    Handlers: # where to forward messages to.
        dev: https://quiet-lane-3168.grok.app 
        prod: https://my-domain.dom/pollyweb/prod/inbox
        $: $prod # if no key is provided, run prod.
    ```

    | Property | Type | Description
    |-|-|-
    | `Handlers` | dict | URLs with handlers.
    

    ---
    <br/>

1. **How to run a handler server locally?**

    To run a handler server locally,
    * e.g., `http://localhost:7070`
    * domain admins can leverage a reverse proxy service like ngrok.

    ---
    <br/>

1. **How is traffic processed over HTTP?**

    Using the [`PublicKey.txt`](<🔑📄 PublicKey file.md>) file,
    * [Hosted 📦 domains](<../📦👥 Hosted domain.md>) decrypt the messages received from [Hoster ☁️ domains](<../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster helper/☁️ Hoster 🤲 helper.md>), 
    * and encrypt the replies and outbound messages.

    ---
    <br/>