# 😃 Vending Machine: Talker

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

* [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) for:
  * [Buy water 💧 ](<11 💧 Buy water.md>)
  * [Buy beer 🍺 ](<12 🍺 Buy beer.md>)

## Talker

<!--
TODO: Add the flow to the Manifest
-->

```yaml
# 😃 Talker
💬|[Buy] an item:

# Set the Chat's flow.
- INFORM|Buy

# Ask for the item number.
- DIGITS|What's the item number? >> $number

# Confirm using the item's name.
- MAP|Items|$number >> $item
- CONFIRM|A {$item.Name}?     

# Ask proof of over 21 if needed.
- IF|$item.21+:
    Then: SHARE|.IDENTITY/OVER-21

# Charge the item price.
# * FREEZE is executed automatically.
- CHARGE:
    Items:
      - Price: $item.Price
        Name: $item.Name

# Deliver the item.
- TEMP|Delivering...   

# Find the MachineKey from the Chat Locator
- MAP|Locators|$.Chat.Key >> $locator

# Relay the Open command to the vending machine.
- RELAY|Machines|$locator.MachineKey >> relayed
    Script: Open({$item.Number})
    OnFailure: Failure
    OnSuccess: Success

# Show error.
fail:
- FAILURE|It didn't work!   # Inform the user
- REFUND|$item.Price        # Refund the value
- LOG:
    Machine: $.Chat.Key
    Item: $item.Number
    Relay: $relayed

# Show success.
Success:
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
| [🪣 `Items`](<94 🪣 Owner: Items.md>) | List of items to [`MAP`](<../../../9 😃 Talkers/30 🗃️ Talker data/61 🪣 MAP item.md>)
| [🪣 `Locators`](<95 🪣 Owner: Locators.md>) | List of machines to [`MAP`](<../../../9 😃 Talkers/30 🗃️ Talker data/61 🪣 MAP item.md>)
| 💬 [`$.Chat.Key`](<../../../9 😃 Talkers/30 🗃️ Talker data/11 💬 $.Chat holder.md>) | Get the machine's [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) key
|

<br/>

## Functions

[Functions](<../../../9 😃 Talkers/30 🗃️ Talker data/12 🐍 {Function}.md>)| Type | Purpose
|-|-|-
| `Deduct` | Custom | Deduct the stock from the ERP.
|

<br/>

## Commands

|Type|[Command ⌘](<../../../9 😃 Talkers/40 🌊 Talker flows/10 ⌘ Command.md>)|Purpose
|-|-|-
|Data| 🪣 [`MAP`](<../../../9 😃 Talkers/30 🗃️ Talker data/61 🪣 MAP item.md>) | Look up items and machines
|Input | 🔢 [`DIGITS`](<../../../9 😃 Talkers/20 🤔 Prompts/7 ✏️ Input prompts/44 🔢 DIGITS prompt.md>) | Ask for item number
|| 👍 [`CONFIRM`](<../../../9 😃 Talkers/20 🤔 Prompts/7 ✏️ Input prompts/31 👍 CONFIRM prompt.md>) | Confirm item name
|Status| ⏳ [`TEMP`](<../../../9 😃 Talkers/20 🤔 Prompts/4 ⚠️ Status prompts/25 ⏳ TEMP prompt.md>) | Show delivering status
|| ✅ [`SUCCESS`](<../../../9 😃 Talkers/20 🤔 Prompts/4 ⚠️ Status prompts/23 ✅ SUCCESS prompt.md>) | Ask to pick the item
|| ❌ [`FAILURE`](<../../../9 😃 Talkers/20 🤔 Prompts/4 ⚠️ Status prompts/24 ❌ FAILURE prompt.md>) | To show in case of error
|Flow| ⤵️ [`IF`](<../../../9 😃 Talkers/40 🌊 Talker flows/21 ⤵️ IF flow.md>) | To see if 21+ check is needed
||⬇️ [`EVAL`](<../../../9 😃 Talkers/30 🗃️ Talker data/20 ⬇️ EVAL flow.md>) | To deduct the value on errors
||🪵 [`LOG`](<../../../9 😃 Talkers/30 🗃️ Talker data/15 🪵 LOG flow.md>) | To log eventual errors
|Message| 💼 [`SHARE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/45 💼 SHARE msg.md>) | Ask for proof of over 21
|| 💳 [`CHARGE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/53 💳 CHARGE msg.md>) | Charge the item price
|| 🏦 [`REFUND`](<../../../9 😃 Talkers/60 ⏩ Msg flows/55 🏦 REFUND.md>) | Refund the payment on failure
|| 👋 [`GOODBYE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/50 👋 GOODBYE.md>) | Show ads on success
|| 🛰️ [`RELAY`](<../../../9 😃 Talkers/60 ⏩ Msg flows/51 🛰️ RELAY msg.md>) | Relay messages to  machines
|

