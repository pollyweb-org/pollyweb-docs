<!-- TODO: -->

# 🫡 Talker `TRUSTS` command

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

> Implemented by the [`.TRUSTS` 📃 script](<🫡 TRUSTS 📃 script.md>)


<br/>


1. **What's the TRUSTS command?**

    A `TRUSTS`
    * is a handler [Command ⌘](<../../📃 basics/Command ⌘/⌘ Command.md>) 
    * to assert the [domain Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) between [domains 👥](<../../../../40 👥 Domains/👥 Domain.md>)
    * by call the [`Trusts@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>).
  
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

    | Input| Purpose | Example
    |-|-|-
    | `Trusted` | [Domain 👥](<../../../../40 👥 Domains/👥 Domain.md>) to [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) | `any-domain.dom`
    | `Schema` | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to assert | `.HOST/HELLO`
    | `Role`| Optional role to assert | `VAULT` `CONSUMER`

    ---
    <br/>

