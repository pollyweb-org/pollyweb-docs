# 😃 Vending Machine [Talker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/01 😃 Talker.md>)

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)


| Dependencies | Purpose
|-|-
| [🧩 //IDENTITY/OVER21](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/IDENTITY/🧩 IdentityOver21.md>) | Verify minimum age to drink.
| [🪣 Items](<94 🪣 Owner: Items.md>) | List of items to [`MAP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/31 🪣 MAP item.md>).


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
- SUCCESS|Pick your item.   # Inform the user
- GOODBYE                   # Show review, ads
- EVAL >> sold:             # Create the sell
    Machine: .ChatKey
    Item: $item.Number
- EVAL|{Deduct($sold)}      # Deduct the stock


```



[Commands](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/10 Command.md>)|Purpose
|-|-
| 🔢 [`INT`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/21 🔢 INT prompt.md>) | Ask for item number.
| 🪣 [`MAP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/31 🪣 MAP item.md>) | Map item number to item name.
| 👍 [`CONFIRM`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/24 👍 CONFIRM prompt.md>) | Confirm item name.
| 💼 [`SHARE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/46 💼 SHARE msg.md>) | Ask for proof of over 21.
| 💳 [`CHARGE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/43 💳 CHARGE msg.md>) | Charge the item price.
| ⏳ [`TEMP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/12 ⏳ TEMP prompt.md>) | Show delivering status.
| 🛰️ [`RELAY`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/32 🛰️ RELAY msg.md>) | Relay messages to vending machines.
|

[Functions](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/12 {Function}.md>)| Type | Purpose
|-|-|-
| `.ChatKey` | Built-in | Get machine's [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) key.
| `.Log` | Built-in | Raise an internal ticket.
| `Deduct` | Custom | Deduct the stock from the ERP.
|