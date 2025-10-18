<!-- TODO: -->

# 🔐 Talker `CALLBACK` command

> Part of [Talker 😃](<../../😃 Talker.md>)


> Used in [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)

<br/>

1. **What's the syntax of CALLBACK?**

    ```yaml
    CALLBACK|<callback-object>:
        <response-data>
    ```

    ---
    <br/>

1. **What's an example of CALLBACK?**

    ```yaml
    # Talker 😃
    - BIND|$bindable >> $bound
    - IF|$bound:
        Then: SUCCESS|Your wallet is bound.
        Else: FAILURE|Not bounded.
    ```

    ```yaml
    # Handler
    - GET|Callbacks|$.Msg.Callback >> $callback
    - CALLBACK|$callback
    ```

    ---
    <br/>
