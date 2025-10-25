<!-- TODO -->

# 🗄️📃 Disclose handler

> Part of the [Vault 🗄️ domain](<../../🗄️🎭 Vault role.md>)

> Implements the [`Disclose@Vault` 🅰️ method](<🗄️ Disclose 🐌 msg.md>)

## Script

```yaml
📃 Disclose@Vault:

# Verify the signature
- VERIFY|$.Msg

- EVAL|

# Create the collect
- SAVE|Collects@Vault >> $collect:
    Collect: .UUID()
    Consumer: $.Msg.From
    Data: $data

# Send the Collect message
- SEND:
    Header:
        To: $collect.Consumer
        Subject: Collect@Consumer
    Body:
        Collect: $collect.Collect
```

|Needs||
|-|-
|