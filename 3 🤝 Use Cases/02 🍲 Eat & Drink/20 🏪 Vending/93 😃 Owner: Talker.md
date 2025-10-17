# 😃 Vending Machine: Talker

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

* [Talker 😃](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃 Talker.md>) for:
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
- CHARGE >> $charge
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
- REFUND|$charge            # Refund the value
- LOG:
    Machine: $.Chat.Key
    Item: $item.Number
    Charge: $charge
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
| [🪣 `Items`](<94 🪣 Owner: Items.md>) | List of items to [`MAP`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃💾 Talker data/MAP 🗺️ item.md>)
| [🪣 `Locators`](<95 🪣 Owner: Locators.md>) | List of machines to [`MAP`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃💾 Talker data/MAP 🗺️ item.md>)
| 💬 [`$.Chat.Key`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃💾 Talker data/$.Chat 💬 holder.md>) | Get the machine's [Locator 🔆](<../../../4 ⚙️ Solution/25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key
|

<br/>

## Functions

[Functions](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃💾 Talker data/{Function} 🐍.md>)| Type | Purpose
|-|-|-
| `Deduct` | Custom | Deduct the stock from the ERP.
|

<br/>

## Commands

|Type|[Command ⌘](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/⌘ Command.md>)|Purpose
|-|-|-
|Data| 🪣 [`MAP`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃💾 Talker data/MAP 🗺️ item.md>) | Look up items and machines
|Input | 🔢 [`DIGITS`](<../../../4 ⚙️ Solution/35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/44 🔢 DIGITS prompt.md>) | Ask for item number
|| 👍 [`CONFIRM`](<../../../4 ⚙️ Solution/35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) | Confirm item name
|Status| ⏳ [`TEMP`](<../../../4 ⚙️ Solution/35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/TEMP ⏳ prompt.md>) | Show delivering status
|| ✅ [`SUCCESS`](<../../../4 ⚙️ Solution/35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>) | Ask to pick the item
|| ❌ [`FAILURE`](<../../../4 ⚙️ Solution/35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/FAILURE ❌ prompt.md>) | To show in case of error
|Flow| ⤵️ [`IF`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/IF ⤵️.md>) | To see if 21+ check is needed
||⬇️ [`EVAL`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃💾 Talker data/EVAL ⬇️ flow.md>) | To deduct the value on errors
||🪵 [`LOG`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃💾 Talker data/LOG 🪵 flow.md>) | To log eventual errors
|Message| 💼 [`SHARE`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃📨 Talker msgs/SHARE 💼 msg.md>) | Ask for proof of over 21
|| 💳 [`CHARGE`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃📨 Talker msgs/CHARGE 💳 msg.md>) | Charge the item price
|| 🏦 [`REFUND`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃📨 Talker msgs/REFUND 🏦 msg.md>) | Refund the payment on failure
|| 👋 [`GOODBYE`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃📨 Talker msgs/GOODBYE 👋 msg.md>) | Show ads on success
|| 🛰️ [`RELAY`](<../../../4 ⚙️ Solution/35 💬 Chats/😃 Talkers/😃📨 Talker msgs/RELAY 🛰️ msg.md>) | Relay messages to  machines
|

