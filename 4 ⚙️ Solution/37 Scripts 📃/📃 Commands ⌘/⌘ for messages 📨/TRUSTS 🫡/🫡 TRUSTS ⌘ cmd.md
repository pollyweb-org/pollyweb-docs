<!-- TODO: -->

# 🫡 Talker `TRUSTS` command

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Implemented by the [`.TRUSTS` 📃 script](<🫡 TRUSTS 📃 script.md>)


<br/>

## FAQ

1. **What's the TRUSTS command?**

    A `TRUSTS`
    * is a handler [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * to assert the [domain Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) between [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
    * by call the [`Trusts@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>).
  
    ---
    <br/>

1. **What's the TRUSTS syntax?**

    ```yaml
    # Comprehensive
    TRUSTS >> $trusts:
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
    |`$trusts`| Trusts result [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | 
    |         | If omitted, fails if not trusted | 
    | `Trusted` | [Domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) to [Trust 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) | `any-domain.dom`
    | `Truster` | Optional [Domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) trusting | `my-domain.dom` 
    ||Defaults to [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>).`Domain`
    | `Schema` | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to assert | `.HOST/HELLO`
    | `Role`| Optional role to assert | `VAULT` `CONSUMER`


    ---
    <br/>

