# 😃 Vending Machine [Talker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/01 😃 Talker.md>)


| Dependencies | Purpose
|-|-
| [🧩 //IDENTITY/OVER21](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/IDENTITY/🧩 IdentityOver21.md>) | Verify minimum age to drink.
| [🪣 Items](<92 🪣 Owner: Items.md>) | List of items to [`MAP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/31 🪣 MAP item.md>).



```yaml
# 😃 Talker
💬|[Buy] an item:

# Ask for the item number
- INT|What's the item number? >> number

# Map item number to name.
- MAP|Items|{$number} >> item
- CONFIRM|A {$item.Name}?     

# Ask proof of over 21 if needed.
- IF|{$item.21+}:
    Then: SHARE|nlweb.org/IDENTITY/OVER-21

# Charge the item price.
- CHARGE|{$item.Price}     

# Deliver the item.
- TEMP|Delivering...    
- RELAY|Machines|{$$locator.key}
    Command: Open({$item.Number})
    OnFailure: failure
    OnSignal: success

# Show success.
success:
- SUCCESS|Thanks! Pick up your item.
- GOODBYE

# Show error.
fail:
- FAILURE|It didn't work, sorry!
- REFUND|{$item.Price}
```



Commands|Purpose
|-|-
| 🔢 [`INT`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/21 🔢 INT prompt.md>) | Ask for item number.
| 🪣 [`MAP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/31 🪣 MAP item.md>) | Map item number to item name.
| 👍 [`CONFIRM`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/24 👍 CONFIRM prompt.md>) | Confirm item name.
| 💼 [`SHARE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/46 💼 SHARE msg.md>) | Ask for proof of over 21.
| 💳 [`CHARGE`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/43 💳 CHARGE msg.md>) | Charge the item price.
| ⏳ [`TEMP`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/12 ⏳ TEMP prompt.md>) | Show delivering status.
| 🛰️ [`RELAY`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/14 😃 Talkers/32 🛰️ RELAY msg.md>) | Relay command to vending machine.
|