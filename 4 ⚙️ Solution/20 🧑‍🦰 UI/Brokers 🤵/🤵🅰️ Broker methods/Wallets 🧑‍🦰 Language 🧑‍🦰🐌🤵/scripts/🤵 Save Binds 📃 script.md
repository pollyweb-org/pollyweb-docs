# 🤵📃 Save Binds


## Script

```yaml
📃 Save-Binds:

# Verify the required inputs
- ASSERT:
    AllOf: $wallet, $translated

# Save the Binds
- PARALLEL|$wallet.Binds|$bind:

    # Set the Vault title
    - SELECT >> $bind.Vault$:
        First: Translation
        From: $translated.Domains
        Where: Domain.Is($bind.Vault)

    # Save the bind
    - SAVE|$bind
```


|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PARALLEL`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SAVE`](<../../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) {{SELECT}}
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Function 🐍.md>) | [`.Is`](<../../../../../35 💬 Chats/Scripts 📃/📃 functions 🐍/🔩 {.Is}.md>)
|
