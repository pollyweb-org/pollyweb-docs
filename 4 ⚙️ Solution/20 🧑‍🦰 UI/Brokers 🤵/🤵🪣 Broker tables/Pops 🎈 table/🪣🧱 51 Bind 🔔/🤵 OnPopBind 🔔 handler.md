# 🤵 OnPopBind 🔔 handler

> About
* Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
* Asks the user if they want do remove the {{Binds}}.


<br/>

## Script

```yaml
📃 OnPopBind:

# Verify the inputs
- ASSERT|$.Inputs:
    AllOf: Bind

# Ask for confirmation 🤔
- CONFIRM: Unbind ´{$Bind.Title}´?

# Remove the bind
- DELETE|$bind
```