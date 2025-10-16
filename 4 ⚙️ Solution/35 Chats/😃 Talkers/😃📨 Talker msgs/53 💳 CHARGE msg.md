 # 💳 Talker `CHARGE` command

> Automatically calls [FREEZE ❄️](<42 ❄️ FREEZE msg.md>)
 

1. **What's the syntax?**

    ```yaml
    CHARGE:
       Amount: <amount>
       Bill: <bill-id>
    ```

    ```yaml
    CHARGE|<amount>|<bill-id>
    ```

   * Calls [💵🐌🤵 Charge @ Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/7 🤵🅰️ Pay/💵🐌🤵 Charge.md>)
   * May have a [Biller 🤝](<../../../45 🤲 Helper domains/20 🤝 Billers/🤝🤲 Biller helper.md>) ID for multiple [Collectors 🏦](<../../../45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>).


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
      Code: .PAYER/CHARGE
      Context: 
         Bill: $bill
         Collection: $collection
   ```