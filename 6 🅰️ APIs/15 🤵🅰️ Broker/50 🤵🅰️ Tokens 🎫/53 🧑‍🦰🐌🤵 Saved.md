<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTe327e788ccd54eefbe5f7e844 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L88 -->

# 🧑‍🦰🐌🤵 Saved @ Broker

> [Wallet 🧑‍🦰 apps](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) inform [Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) where the file with the [Token 🎫](<../../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) details was stored locally on the device.

> Part of the [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/02 🧑‍🦰👉🎴 Save token.md>) flow:
> <br>• triggered by [`Save@Notifier`](<../../65 📣🅰️ Notifier/04 📣🎫🅰️ Tokens/41 🤵🐌📣 Save.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Saved@Broker

Body:
    ChatID: <chat-uuid>
    TokenID: <token-uuid>
    Issuer: any-host.com
    Path: /storage/nlweb/tokens/<issuer>/<token-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
||`To`|string| [Broker 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
||`Subject`|string|`Saved@Broker`
|Body  |`ChatID` |uuid  | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Save@Notifier`](<../../65 📣🅰️ Notifier/04 📣🎫🅰️ Tokens/41 🤵🐌📣 Save.md>)
|      |`TokenID` |uuid  | [Token 🎫](<../../../4 ⚙️ Solution/30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) ID from [`Save@Notifier`](<../../65 📣🅰️ Notifier/04 📣🎫🅰️ Tokens/41 🤵🐌📣 Save.md>)
|      |`Issuer`  |string| [Issuer 🎴](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>) from [`Save@Notifier`](<../../65 📣🅰️ Notifier/04 📣🎫🅰️ Tokens/41 🤵🐌📣 Save.md>)
|      |`Path`    |string| Path to the local file
|