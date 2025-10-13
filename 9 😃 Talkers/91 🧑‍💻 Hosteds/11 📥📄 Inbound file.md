# 📥 Hosted `Inbound` file

> Part of [Hosted 🧑‍💻 domain](<01 🧑‍💻 Hosted domain.md>)

<br/>

1. **What is the Inbound file?**

    The `📥 Inbound.yaml` file 
    * tells the [Hoster ☁️ domain](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) 
    * where to forward [Messages 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) to.

    ---
    <br/>

1. **What does the Inbound.yaml file look like?**

    ```yaml
    Handlers: # where to forward messages to.
        dev: https://quiet-lane-3168.grok.app 
        prod: https://my-domain.com/nlweb/prod/inbox
        $: prod # handle live requests by default.
    ```

    | Property | Type | Description
    |-|-|-
    | `Handlers` | map | URLs with handlers.
    

    ---
    <br/>

1. **How to run a handler server locally?**

    To run a handler server locally,
    * e.g., `http://localhost:7070`
    * domain admins can leverage a reverse proxy service like ngrok.

    ---
    <br/>

1. **How is traffic processed over HTTP?**

    Using the [`PublicKey.txt`](<10 🔑📄 PublicKey file.md>) file,
    * [Hosted 🧑‍💻 domains](<01 🧑‍💻 Hosted domain.md>) decrypt the messages received from [Hoster ☁️ domains](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>), 
    * and encrypt the replies and outbound messages.

    ---
    <br/>