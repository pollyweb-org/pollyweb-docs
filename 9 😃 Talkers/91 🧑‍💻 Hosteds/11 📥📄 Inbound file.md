# 📥 Hosted `Inbound` file

> Part of [Hosted 🧑‍💻 domain](<01 🧑‍💻 Hosted domain.md>)

<br/>

1. **What does the Inbound file look like?**

    The `📥 Inbound.yaml` file tells the [Hoster ☁️ domain](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) which [Messages 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) to forward, and where to.
    
    * For [💬 Chats](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) started from the workstation's terminal, the CLI will open a proxy connection to receive the messages from the [Hoster ☁️ domain](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) and forward them to the target until the [💬 Chat](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ends, allowing a local web-server at http://localhost to be running as a target.
  
    * [💬 Chats](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) starting with any other way will communicate only via the Internet, and will require the target to expose the WebHook endpoint as HTTPS.

    ```yaml
    🤝: nlweb.org/HOSTER/INBOUND

    Roles: # what messages to forward to the WebHook.
        - Host
        - Vault
        - Issuer
        - Seller
    
    Hook: # where to forward messages to.

        Targets: # test environments.
            dev: http://localhost:7070
            prod: https://my-domain.com/nlweb/prod/inbox
    
        Default: prod # handle live requests.
    ```

    ---
    <br/>

