# 🤵🐌🎴 Accepted @ Issuer


> Part of the [🧑‍🦰👉🎴 Save Token @ Issuer](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token.md>) flow.

* Tells an [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) if a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) was accepted or rejected.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-issuer.dom
    Subject: Accepted@Issuer

Body:
    Hook: <hook-uuid>
    Token: <token-uuid>
```


|Object |Property |Type|Description
|-|-|-|-
|Header | `From`  | string  | [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) from [`Offer@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)
|       | `To`    | string  | [Issuer 🎴](<../🎴🎭 Issuer role.md>) from [`Offer@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)
||`Subject`|string|`Token@Issuer` 
| Body  | `Hook`| uuid | `Hook` from [`Offer@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)
|| `Token`| string | [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)  from [`Save@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
|


<br/>

## Handler

```yaml
# Get the Hook
- GET >> $hook:
    Set: Hooks@Talker
    Key: $.Msg.Hook

# Assert if it's the right Broker
- ASSERT:
    $.Msg.From: $hook.Broker

# Save the Token
- SAVE|Tokens@Issuer:
    Token: $.Msg.Token
    :$hook.Token:

# Continue the Talker
- REEL|$hook:
    $token
```

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| ⏬ [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/GET ⏬ item.md>) | Get the [Hook 🪣](<../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) from [`Offer@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🎴🐌🤵 Offer.md>)
| 🚦 [`ASSERT`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) | Assert if it's the right [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) 
| ⬇️ [`EVAL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/EVAL ⬇️ flow.md>) | Get the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) data from the hook
| 💾 [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) | Save the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) to the [Tokens 🪣 table](<../🎴🪣 Issuer tables/🗄️🪣 Tokens.md>)
| 🎣 [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) | Continue the [Talker 😃](<../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>)
| 


<br/>

## FAQ

1. **How do Issuers know if the user accepted?**

    An empty `Token` property means that no [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) was saved.

    * This allows the [Issuer 🎴 domain](<../🎴🎭 Issuer role.md>) to force the user to save the [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>), as in the following example from the [Buy entry at a dance club 🤝 use case](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/12 🌐 Web: Buy entry 🎟️.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    |...
    | 🕺 Club       | ℹ️ Entry paid.
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Save entry? [Yes, No]  | > No
    | 🕺 Club       | ℹ️ You need to save the entry.
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Save entry? [Yes, No]  | > Yes
    | 🕺 Club       | ✅ All set.
    |