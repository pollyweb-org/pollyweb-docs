# 📤 Hosted `Outbound` file

> Part of [Hosted 📦 domain](<../📦👥 Hosted domain.md>)

<br/>


1. **What is the Outbound file?**

    The `📤 Outbound.yaml` file 
    * is a file managed by the [Hoster ☁️ domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) 
    * that tells [Hosted 📦 domain](<../📦👥 Hosted domain.md>)
    * where to forward [Messages 📨](<../../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) to.

    ---
    <br/>

1. **What does the Outbound file look like?**


    ```yaml
    # 📤 Outbound.yaml

    Proxy: https://{uuid}.proxies.any-hoster.dom
    ```

    | Property | Type | Description
    |-|-|-
    | `Proxy` | string | URL where to send messages to.

    ---
    <br/>

1. **How does the Outbound proxy work?**

    The [Hoster ☁️ domain](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) proxy 
    * receives unsigned [Messages 📨](<../../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) from the [domain 👥](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>), 
    * signs them with the [DKIM 📨](<../../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) private key, 
    * and forwards them downstream without ever disclosing the private key.

    ---
    <br/>

1. **What happens if the Outbound file gets corrupted?**

    It will be fixed automatically on the next sync.

    ---
    <br/>