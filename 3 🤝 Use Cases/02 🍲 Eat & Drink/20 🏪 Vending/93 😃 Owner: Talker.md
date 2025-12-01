# 😃 Vending Machine: Talker

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

> [Script 📃](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/Script 📃.md>) for:
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
- READ|Items|$number >> $item
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
- READ|Locators|$.Chat.Key >> $locator

# Relay the Open command to the vending machine.
- RELAY|Machines|$locator.MachineKey >> relayed
    Script: Open({$item.Number})
    OnFailure: Failure
    OnSuccess: Success
````

```yaml
# Show error.
📃 fail:
- FAIL|It didn't work!   # Inform the user
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
- DONE|Pick up the item. # Inform the user
- GOODBYE                   # Show review, ads
- CALL|Deduct:              # Deduct the stock
    Machine: $.Chat.Key
    Item: $item.Number    
```

<br/>

## Dependencies

| Dependencies | Purpose
|-|-
| [🧩 `//IDENTITY/OVER21`](<../../../7 🧩 Codes/IDENTITY/🧩 IdentityOver21.md>) | Verify minimum age to drink
| [🪣 `Items`](<94 🪣 Owner: Items.md>) | List of items to [`READ`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)
| [🪣 `Locators`](<95 🪣 Owner: Locators.md>) | List of machines to [`READ`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)
| 💬 [`$.Chat.Key`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) | Get the machine's [Locator 🔆](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key
|

<br/>

## Functions

[Functions](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/Function 🐍.md>)| Type | Purpose
|-|-|-
| `Deduct` | Custom | Deduct the stock from the ERP.
|

<br/>

## Commands

|Type|[Command ⌘](<../../../4 ⚙️ Solution/35 💬 Chats/Scripts 📃/Command ⌘.md>)|Purpose
|-|-|-
|Data| 🧲 [`READ`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | Look up items and machines
|Input | 🔢 [`DIGITS`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/DIGITS 🔢 prompt.md>) | Ask for item number
|| 👍 [`CONFIRM`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) | Confirm item name
|Status| ⏳ [`TEMP`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) | Show delivering status
|| ✅ [`DONE`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) | Ask to pick the item
|| ❌ [`FAIL`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) | To show in case of error
|Flow| ⤵️ [`IF`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) | To see if 21+ check is needed
||🧮 [`CALL`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) | To deduct the value on errors
||🪵 [`LOG`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/LOG 🪵/🪵 LOG ⌘ cmd.md>) | To log eventual errors
|Message| 💼 [`SHARE`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/SHARE 💼/💼 SHARE ⌘ cmd.md>) | Ask for proof of over 21
|| 💳 [`CHARGE`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/CHARGE 💳/💳 CHARGE ⌘ cmd.md>) | Charge the item price
|| 🏦 [`REFUND`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/REFUND 🏦/🏦 REFUND ⌘ cmd.md>) | Refund the payment on failure
|| 👋 [`GOODBYE`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) | Show ads on success
|| 🛰️ [`RELAY`](<../../../4 ⚙️ Solution/37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/RELAY 🛰️/🛰️ RELAY ⌘ cmd.md>) | Relay messages to  machines
|

