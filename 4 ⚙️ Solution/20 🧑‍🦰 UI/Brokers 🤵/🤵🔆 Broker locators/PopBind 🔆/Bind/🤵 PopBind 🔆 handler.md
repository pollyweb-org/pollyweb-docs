# 🤵 OnPopBind 🔔 handler

> About
* Part of the [`Broker.Pops` 🪣 table](<../../../🤵🪣 Broker tables/Pops 🎈 table/🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
* Asks the user if they want do remove the [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>).


<br/>

## Script

```yaml
📃 OnPopBind:

# Get the Bind
- READ >> $bind:
    Set: Broker.Binds
    Key: $.Chat.Inputs.Bind
    Assert: 
        Wallet: $.Chat.Wallet

# Verify the inputs
- ASSERT|$.Inputs:
    AllOf: Bind

# Ask for confirmation 🤔
- CONFIRM: Unbind ´{$Bind.Title}´?

# Remove the bind
- DELETE|$bind
```