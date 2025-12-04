# 🎫 ISSUE 📃 script

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`ISSUE`](<🎫 ISSUE ⌘ cmd.md>) command.
* Part of the [🧑‍🦰 `Save Token` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>)
* Part of the [🎴 `Issuer.Tokens.Issue` ⏩ flow](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🪣 Issuer tables/Tokens 🎫 table/🪣⏩ Issued flow/🎴 Issuer.Tokens.Issued ⏩ flow.md>)

<br/>

## Flow

![alt text](<🎫 ISSUE ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN|.ISSUE:
    Schema: any-authority.dom/ANY-SCHEMA
    Starts: 2018-12-10T13:45:00.000Z
    Expires: 2018-12-10T13:45:00.000Z
    Properties: {properties} # Part of the Token 🎫
    Internals: {internals}   # Internal Issuer 🎴 notes
```

<br/>


## Script

```yaml
📃 .ISSUE:

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Schema
    Texts: Schema
    Times: Starts, Expires

# Save the hook
- SAVE|Issuer.Tokens >> $token:
    Broker: $.Chat.Broker
    Chat: $.Chat.Chat
    PublicKey: $.Chat.PublicKey
    Schema: $Schema
    Starts: $Starts
    Expires: $Expires
    Properties: $Properties
    Internals: $Internals

# Wait for the shared data
- WAIT >> $accepted:
    Hook: $token.ID

# Return the token
- IF|$accepted:
    RETURN|$token
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)  [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Issuer.Tokens`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🪣 Issuer tables/Tokens 🎫 table/🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)  [`$.Inputs`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Issue@Broker` 🐌 msg](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) 
|