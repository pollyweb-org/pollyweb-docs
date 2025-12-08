 # 😃💳 Talker `CHARGE` command

> Automatically calls [FREEZE ❄️](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/FREEZE ❄️/❄️ FREEZE ⌘ cmd.md>)
 

1. **What's the syntax?**

    ```yaml
    CHARGE:
       Amount: <amount>
       Bill: <bill-id>
    ```

    ```yaml
    CHARGE|<amount>|<bill-id>
    ```

   * Calls [💵🐌🤵 Charge @ Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Payments 💵 Charge 💵🐌🤵/🤵 Charge 🐌 msg.md>)
   * May have a [Biller 🤝](<../../../../45 🤲 Helper domains/Billers 🤝/🤝 Biller/🤝 Biller 🤲 helper.md>) ID for multiple [Collectors 🏦](<../../../../45 🤲 Helper domains/Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>).


1. **What's happening?**

   ```yaml
   # Block all previous edits
   - FREEZE          

   # Create a bill
   - BILL >> $bill:
      Form: MyForm
      Items: {object}

   # Create a collection
   - COLLECT >> $collection:
      Bill: $bill

   # Charge the collection
   - SHARE >> $shared:
      Schema: .PAYER/CHARGE
      Context: 
         Bill: $bill
         Collection: $collection
   ```