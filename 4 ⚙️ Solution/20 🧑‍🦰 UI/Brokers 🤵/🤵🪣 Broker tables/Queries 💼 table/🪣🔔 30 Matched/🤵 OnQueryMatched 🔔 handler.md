# 🤵 OnQueryMatched 🔔 handler


> About
* Part of the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQueryMatched ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryMatched:

# Verify the trust of each match
- PARALLEL $Query.Matches >> $match:

    # Ask if the Consumer trusts the Vault
    - TRUSTS >> $trustedVault:
        Truster: $Query.Consumer
        Trusted: $match.Domain
        Schema: $match.Schema
        Role: VAULT

    # Ask the Vault trusts the Consumer
    - TRUSTS >> $trustedConsumer:
        Truster: $match.Domain
        Trusted: $Query.Consumer
        Schema: $match.Schema
        Role: CONSUMER

    # If trusted, add to the trusted list
    - IF:
        .AllOf: $trustedVault, $trustedConsumer
    - THEN:
        PUT $match +> $trusted:

# Set the trusted matches to the Query item
- SAVE $Query:
    Trusted: $trusted
    STATE: .If($trusted, TRUSTED, UNTRUSTED)
```

Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRUSTS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>)  |
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.If`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/If ⓕ.md>) 
|