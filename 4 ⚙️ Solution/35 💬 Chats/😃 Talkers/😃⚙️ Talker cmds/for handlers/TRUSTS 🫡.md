<!-- TODO: -->

# 🫡 Talker `TRUSTS` command

> Part of [Talker 😃](<../../😃 Talker role.md>)

> Implemented by the [`.TRUSTS` 📃 script](<../../😃📃 Talker scripts/😃📃 .TRUSTS 🫡 script.md>)


<br/>


1. **What's the TRUSTS command?**

    A `TRUSTS`
    * is a handler [Command ⌘](<../...commands/⌘ Command.md>) 
    * to assert the [domain Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) between [domains 👥](<../../../../40 👥 Domains/👥 Domain.md>).
  
    ---
    <br/>

1. **What's the TRUSTS syntax?**

    ```yaml
    # Comprehensive
    TRUSTS:
        Trusted: <trusted>
        Truster: <truster> # defaults to current domain
        Schema: <schema>
        Role: <role>
    ```

    ```yaml
    # Simple
    TRUSTS|<trusted>:
        Schema: <schema>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `Trusted` | [Domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) to [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) | `any-domain.dom`
    | `Schema` | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to assert | `.HOST/HELLO`

    ---
    <br/>

