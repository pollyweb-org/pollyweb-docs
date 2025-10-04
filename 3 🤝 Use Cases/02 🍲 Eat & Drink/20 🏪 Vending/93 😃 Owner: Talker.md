# 😃 Vending Machine: Talker

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

* [Talker 😃](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/01 😃 Talker.md>) for:
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
- FLOW|Buy

# Ask for the item number.
- INT|What's the item number? >> number

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
- MAP|Locators|{.ChatKey} >> locator

# Relay the Open command to the vending machine.
- RELAY|Machines|{$locator.MachineKey} >> relayed
    Message: Open({$item.Number})
    OnFailure: Failure
    OnSuccess: Success

# Show error.
fail:
- FAILURE|It didn't work!   # Inform the user
- REFUND|{$item.Price}      # Refund the value
- EVAL >> error:            # Create the report
    Machine: .ChatKey
    Item: $item.Number
    Relay: $relayed
- EVAL|{.Log($error)}       # Send the report

# Show success.
Success:
- SUCCESS|Pick up the item. # Inform the user
- GOODBYE                   # Show review, ads
- EVAL >> sold:             # Create the sell
    Machine: .ChatKey
    Item: $item.Number
- EVAL|{Deduct($sold)}      # Deduct the stock
```

<br/>

## Dependencies

| Dependencies | Purpose
|-|-
| [🧩 `//IDENTITY/OVER21`](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/IDENTITY/🧩 IdentityOver21.md>) | Verify minimum age to drink
| [🪣 `Items`](<94 🪣 Owner: Items.md>) | List of items to [`MAP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/31 🪣 MAP item.md>)
| [🪣 `Locators`](<95 🪣 Owner: Locators.md>) | List of machines to [`MAP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/31 🪣 MAP item.md>)
|

<br/>

## Functions

[Functions](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/12 {Function}.md>)| Type | Purpose
|-|-|-
| `.ChatKey` | Built-in | Get machine's [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) key.
| [`.Log`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/13 {.Log} function.md>) | Built-in | Raise an internal ticket.
| `Deduct` | Custom | Deduct the stock from the ERP.
|

<br/>

## Commands

|Type|[Command](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/10 Command.md>)|Purpose
|-|-|-
|Data| 🪣 [`MAP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/31 🪣 MAP item.md>) | Look up items and machines
|Input | 🔢 [`INT`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/21 🔢 INT prompt.md>) | Ask for item number
|| 👍 [`CONFIRM`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/24 👍 CONFIRM prompt.md>) | Confirm item name
|Status| ⏳ [`TEMP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/12 ⏳ TEMP prompt.md>) | Show delivering status
|| ✅ [`SUCCESS`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/13 ✅ SUCCESS prompt.md>) | Ask to pick the item
|| ❌ [`FAILURE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/14 ❌ FAILURE prompt.md>) | To show in case of error
|Message| 💼 [`SHARE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/46 💼 SHARE msg.md>) | Ask for proof of over 21
|| 💳 [`CHARGE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/43 💳 CHARGE msg.md>) | Charge the item price
|| 🏦 [`REFUND`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/44 🏦 REFUND.md>) | Refund the payment on failure
|| 👋 [`GOODBYE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/47 👋 GOODBYE.md>) | Show ads on success
|| 🛰️ [`RELAY`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/32 🛰️ RELAY msg.md>) | Relay messages to vending machines
|

