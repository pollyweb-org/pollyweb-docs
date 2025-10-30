# 😃📃 `.TRUSTS` 🫡 script

> [Script 📃](<../../📃 basics/📃 Script.md>) that implements the [`TRUSTS`](<🫡 TRUSTS ⌘ cmd.md>) command.

> Calls the [`Trusts@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>)

## How to call

```yaml
- RUN|.TRUSTS:
    Schema: my-schema
    Trusted: trusted-entity.dom
    Truster: optional-truster.dom   # Optional
    Role: CONSUMER                  # Optional
```

## Script 

```yaml
📃 .TRUSTS:

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Schema, Trusted
    Texts: Schema, Trusted, Truster

# Assert the role
- ASSERT|$:Role:
    Enum: VAULT, CONSUMER, *

# Default value for the Truster
- IF|!Truster:
    Then: EVAL|$:Truster >> $truster
    Else: EVAL|$.Msg.To >> $truster

# Default value for the Role
- IF|!Role:
    Then: EVAL|$:Role >> $role
    Else: EVAL|* >> $role

# Send the request
- SEND >> $answer:
    Header:
        To: $.Hosted.Graph
        Subject: Trusted@Graph
    Body:
        Truster: $truster
        Trusted: $:Trusted
        Role: $role
        Schema: $:Schema

# Assert if it's trusted
- ASSERT|$answer:
    Trusted: True
```

Needs||
|-|-
| [Commands ⌘](<../../📃 basics/⌘ Command.md>) | [`ASSERT`](<../../📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`IF`](<../../📃 control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SEND`](<../SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>)
| [Holders 🧠](<../../📃 holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`$.Hosted`](<../../📃 holders 🧠/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|
