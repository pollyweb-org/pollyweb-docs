<!-- TODO: -->

# 🫡 Talker `TRUSTS` command

> Part of [Talker 😃](<../../😃 Talker.md>)


<br/>


1. **What's the TRUSTS command?**

    A `TRUSTS`
    * is a handler [Command ⌘](<../for control/⌘ Command.md>) 
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


1. **What does it do internally?**

    Here's the internal logic.

    ```yaml
    .TRUST_IMPLEMENTATION:

    # Default value for the Truster
    - IF|$1.Truster:
        Then: EVAL|$1.Truster >> $truster
        Else: EVAL|$.Msg.To >> $truster

    # Default value for the Role
    - IF|$1.Role:
        Then: EVAL|$1.Role >> $role
        Else: EVAL|* >> $role

    # Send the request
    - SEND >> $answer:
        To: $.Settings.Graph
        Subject: Trusted@Graph
        Truster: $truster
        Trusted: $1.Trusted
        Role: $role
        Schema: $1.Schema

    # Assert if it's trusted
    - ASSERT:
        $answer.Trusted: True
    ```

    | [Command ⌘](<../for control/⌘ Command.md>) | Purpose
    |-|-
    | 📨 [`$.Msg`](<$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
    | 🎛️ [`$.Settings`](<$.Settings 🎛️.md>) | Get the default [Graph 🕸 domain](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🤲 Graph helper.md>)
    | 🚦 [`ASSERT`](<ASSERT 🚦.md>) | Assert if it's [Trusted 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) 
    | ⤵️ [`IF`](<../for control/IF ⤵️.md>) | Verify the parameters  
    | 📬 [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) | Call [👥🚀🕸 `Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>)
    |