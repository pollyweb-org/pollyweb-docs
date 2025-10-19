# 🧑‍🦰🐌💼 Receive @ Consumer


> Part of the [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Prompts 🤔/👉💼 Share Token 🎫.md>) flow

> Succeeds [`Share@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)


> [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) send [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) to a [Consumer 💼 domain](<../💼🎭 Consumer role.md>).



<br/>

## Async Message 🐌

```yaml
Header:
    From: Anonymous
    To: any-consumer.dom
    Subject: Receive@Consumer

Body: 
    Hook: <hook-uuid>
    Tokens: 
      - Token: <token-uuid>
        ...
```

|Object|Property|Type|Description
|-|-|-|-
| Header| `From`    | string | `Anonymous`
| | `To`| string | [Consumer 💼](<../💼🎭 Consumer role.md>) from [`Share@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)
| | `Subject`| string | `Receive@Consumer`
| Body | `Hook` | uuid | `Hook` from [`Share@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/2 🤵🐌📣 Share.md>)
| | `Tokens`  | array | List of `Token` objects
| Token |  `Token`| string | [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) from [`Save@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/4 🎫 Tokens/1 🤵🐌📣 Save.md>)
| | ... | ... | Other [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) fields
|

<br/>

## Handler

```yaml
# Resolve the callback
- GET|Hooks@Talker|$.Msg.Hook >> $hook

# Get the chat
- GET|Chats@Host|$hook.Chat >> $chat

# Verify the Wallet signature
- VERIFY|$.Msg|$chat.PublicKey

# Process each Bind
- PARALLEL|$.Msg.Binds|$bind:

    # Save each Bind
    - SAVE|Binds@Vault:
        Broker: $.Msg.From
        Bind: $bind.Bind
        Schema: $bind.Schema
        User: $chat.User

# Continue the Chat
- REEL|$hook:
    $.Msg.Binds
```

<br/>

## FAQ

1. **What's in the list of Tokens?**

    The list of [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) contains:
    * the content from the response of [`Issued@Issuer`](<../../Issuers 🎴/🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>)
    * stored in local files during [`Saved@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/5 🤵🅰️ Tokens 🎫/🧑‍🦰🐌🤵 Saved.md>).


    ---
    <br/>