# 😃 Vending Machine: Talker

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

* [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>) for:
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
- FORM|Buy

# Ask for the item number.
- DIGITS|What's the item number? >> number

# Confirm using the item's name.
- MAP|Items|{$number} >> item
- CONFIRM|A {$item.Name}?     

# Ask proof of over 21 if needed.
- IF|{$item.21+}:
    Then: SHARE|nlweb.org/IDENTITY/OVER-21

# Charge the item price.
- CHARGE|{$item.Price}     

# Deliver the item.
- TEMP|Delivering...   

# Find the MachineKey from the Chat Locator
- MAP|Locators|{.Chat.Key} >> locator

# Relay the Open command to the vending machine.
- RELAY|Machines|{$locator.MachineKey} >> relayed
    Message: Open({$item.Number})
    OnFailure: Failure
    OnSuccess: Success

# Show error.
fail:
- FAILURE|It didn't work!   # Inform the user
- REFUND|{$item.Price}      # Refund the value
- LOG:
    Machine: {.Chat.Key}
    Item: $item.Number
    Relay: $relayed

# Show success.
Success:
- SUCCESS|Pick up the item. # Inform the user
- GOODBYE                   # Show review, ads
- EVAL >> sold:             # Create the sell
    Machine: {.Chat.Key}
    Item: $item.Number
- EVAL|{Deduct($sold)}      # Deduct the stock
```

<br/>

## Dependencies

| Dependencies | Purpose
|-|-
| [🧩 `//IDENTITY/OVER21`](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/IDENTITY/🧩 IdentityOver21.md>) | Verify minimum age to drink
| [🪣 `Items`](<94 🪣 Owner: Items.md>) | List of items to [`MAP`](<../../../9 😃 Talkers/30 💾 Talker data/61 🪣 MAP item.md>)
| [🪣 `Locators`](<95 🪣 Owner: Locators.md>) | List of machines to [`MAP`](<../../../9 😃 Talkers/30 💾 Talker data/61 🪣 MAP item.md>)
|

<br/>

## Functions

[Functions](<../../../9 😃 Talkers/30 💾 Talker data/12 🐍 {Function}.md>)| Type | Purpose
|-|-|-
| [`.Chat.Key`](<../../../9 😃 Talkers/30 💾 Talker data/13 💬 {.Chat} function.md>) | Built-in | Get machine's [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) key.
| `Deduct` | Custom | Deduct the stock from the ERP.
|

<br/>

## Commands

|Type|[Command ⌘](<../../../9 😃 Talkers/20 🌊 Talker flows/10 ⌘ Command.md>)|Purpose
|-|-|-
|Data| 🪣 [`MAP`](<../../../9 😃 Talkers/30 💾 Talker data/61 🪣 MAP item.md>) | Look up items and machines
|Input | 🔢 [`DIGITS`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/44 🔢 DIGITS prompt.md>) | Ask for item number
|| 👍 [`CONFIRM`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/31 👍 CONFIRM prompt.md>) | Confirm item name
|Status| ⏳ [`TEMP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/25 ⏳ TEMP prompt.md>) | Show delivering status
|| ✅ [`SUCCESS`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/23 ✅ SUCCESS prompt.md>) | Ask to pick the item
|| ❌ [`FAILURE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/24 ❌ FAILURE prompt.md>) | To show in case of error
|Flow| ⤵️ [`IF`](<../../../9 😃 Talkers/20 🌊 Talker flows/21 ⤵️ IF flow.md>)
||⬇️ [`EVAL`](<../../../9 😃 Talkers/30 💾 Talker data/20 ⬇️ EVAL flow.md>)
||🪵 [`LOG`](<../../../9 😃 Talkers/30 💾 Talker data/15 🪵 LOG flow.md>)
|Message| 💼 [`SHARE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/45 💼 SHARE msg.md>) | Ask for proof of over 21
|| 💳 [`CHARGE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/47 💳 CHARGE msg.md>) | Charge the item price
|| 🏦 [`REFUND`](<../../../9 😃 Talkers/60 ⏩ Msg flows/48 🏦 REFUND.md>) | Refund the payment on failure
|| 👋 [`GOODBYE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/50 👋 GOODBYE.md>) | Show ads on success
|| 🛰️ [`RELAY`](<../../../9 😃 Talkers/60 ⏩ Msg flows/51 🛰️ RELAY msg.md>) | Relay messages to vending machines
|

