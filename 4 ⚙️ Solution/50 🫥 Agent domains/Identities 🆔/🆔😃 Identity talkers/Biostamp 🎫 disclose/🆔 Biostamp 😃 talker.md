# 🆔 Biostamp 😃 talker

> Part of [Identity 🆔 domain](<../../🆔 Identity agent/🆔 Identity 🫥 agent.md>)

<br/>

## Diagram

![alt text](<🆔 Biostamp ⚙️ uml.png>)

<br/>


## Script

```yaml
📃 Biostamp:

# Require a Bind
- ASSERT $.Inputs:
    AllOf: Consumer, Query, Bind
    UUIDs: Query, Bind
    Consumer.IsDomain:

# Save the biostamp
- SAVE Identity.Stamps >> $stamp:
    Issuer: $Issuer
    Bind: $Bind

# Return the biostamp
- RETURN: $stamp
```

Uses ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) |
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Identity.Stamps` 🪣 table](<../../🆔🪣 Identity tables/Biostamps/🪣 Biostamps/🆔 Identity.Stamps 🪣 table.md>) 
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsDomain`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>)  |

---
<br/>


## FAQ

1. **Why not simplify and have a single ID per bind?**

    Having a single ID on multiple [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) would allow correlation of multiple [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) to same person, which is not desirable for privacy.

    ---
    <br/>

1. **Why not a canonical approach using `Issuer` and `Token`?**

    Using the `Issuer` and `Token` fields from a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>), instead of a Biomarker, would allow an [Identity 🆔 domain](<../../🆔 Identity agent/🆔 Identity 🫥 agent.md>) to track the usage of Tokens an map them to a citizen.
    * Assuming that [Identity 🆔 domains](<../../🆔 Identity agent/🆔 Identity 🫥 agent.md>) will predominantly be implemented by nations or by their agents, this would allow a nation to track their citizens worldwide in daily interactions with businesses.

    ---
    <br/>

1. **Can biostamps be revoked?**

    No, but what for? 
    * An attacker with a Biostamp can only force the user holding the device to confirm that they are holding the device, which is redundant and not a security risk by itself.

    ---
    <br/>
