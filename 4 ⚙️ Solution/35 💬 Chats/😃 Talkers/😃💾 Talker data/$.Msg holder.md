<!-- TODO: detail -->

> Example: [Pop Vault 🔆](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🔆 Broker locators/Pop Vault 🔆.md>)

```yaml
# Get the Wallet 🧑‍🦰
- MAP|Wallets|$.Msg.Header.From >> $wallet

# Verify the Message.
- VERIFY|$.Msg|$wallet.PublicKey
```