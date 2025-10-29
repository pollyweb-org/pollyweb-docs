# 😃 Vending Machine: Talker

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

> [Script 📃](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) for:
  * [Buy water 💧 ](<11 💧 Buy water.md>)
  * [Buy beer 🍺 ](<12 🍺 Buy beer.md>)

## Script

<!--
TODO: Add the flow to the Manifest
-->

```yaml
💬|[Buy] an item:

# Set the Chat's flow.
- INFORM|Buy

# Ask for the item number.
- DIGITS|What's the item number? >> $number

# Confirm using the item's name.
- GET|Items|$number >> $item
- CONFIRM|A {$item.Name}?     

# Ask proof of over 21 if needed.
- IF|$item.21+:
    Then: SHARE|.IDENTITY/OVER-21

# Charge the item price.
# * FREEZE is executed automatically.
- CHARGE >> $charge
    Items:
      - Price: $item.Price
        Name: $item.Name

# Deliver the item.
- TEMP|Delivering...   

# Find the MachineKey from the Chat Locator
- GET|Locators|$.Chat.Key >> $locator

# Relay the Open command to the vending machine.
- RELAY|Machines|$locator.MachineKey >> relayed
    Script: Open({$item.Number})
    OnFailure: Failure
    OnSuccess: Success
````

```yaml
# Show error.
📃 fail:
- FAILURE|It didn't work!   # Inform the user
- REFUND|$charge            # Refund the value
- LOG:
    Machine: $.Chat.Key
    Item: $item.Number
    Charge: $charge
    Relay: $relayed
```

```yaml
# Show success.
📃 Success:
- SUCCESS|Pick up the item. # Inform the user
- GOODBYE                   # Show review, ads
- EVAL|Deduct:              # Deduct the stock
    Machine: $.Chat.Key
    Item: $item.Number    
```

<br/>

## Dependencies

| Dependencies | Purpose
|-|-
| [🧩 `//IDENTITY/OVER21`](<../../../7 🧩 Codes/IDENTITY/🧩 IdentityOver21.md>) | Verify minimum age to drink
| [🪣 `Items`](<94 🪣 Owner: Items.md>) | List of items to [`GET`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>)
| [🪣 `Locators`](<95 🪣 Owner: Locators.md>) | List of machines to [`GET`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>)
| 💬 [`$.Chat.Key`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$.Chat 💬/💬 $.Chat 🧠 holder.md>) | Get the machine's [Locator 🔆](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key
|

<br/>

## Functions

[Functions](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>)| Type | Purpose
|-|-|-
| `Deduct` | Custom | Deduct the stock from the ERP.
|

<br/>

## Commands

|Type|[Command ⌘](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>)|Purpose
|-|-|-
|Data| 🧲 [`GET`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) | Look up items and machines
|Input | 🔢 [`DIGITS`](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/DIGITS 🔢/DIGITS 🔢 prompt.md>) | Ask for item number
|| 👍 [`CONFIRM`](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) | Confirm item name
|Status| ⏳ [`TEMP`](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/TEMP ⏳/TEMP ⏳ prompt.md>) | Show delivering status
|| ✅ [`SUCCESS`](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>) | Ask to pick the item
|| ❌ [`FAILURE`](<../../../4 ⚙️ Solution/35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/FAILURE ❌/FAILURE ❌ prompt.md>) | To show in case of error
|Flow| ⤵️ [`IF`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) | To see if 21+ check is needed
||⬇️ [`EVAL`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) | To deduct the value on errors
||🪵 [`LOG`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...control ▶️/LOG 🪵/🪵 LOG ⌘ cmd.md>) | To log eventual errors
|Message| 💼 [`SHARE`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...methods 🤵/SHARE 💼/💼 SHARE ⌘ cmd.md>) | Ask for proof of over 21
|| 💳 [`CHARGE`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...methods 🤵/CHARGE 💳/💳 CHARGE ⌘ cmd.md>) | Charge the item price
|| 🏦 [`REFUND`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...methods 🤵/REFUND 🏦/🏦 REFUND ⌘ cmd.md>) | Refund the payment on failure
|| 👋 [`GOODBYE`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...methods 🤵/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) | Show ads on success
|| 🛰️ [`RELAY`](<../../../4 ⚙️ Solution/35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...methods 🤵/RELAY 🛰️/🛰️ RELAY ⌘ cmd.md>) | Relay messages to  machines
|

