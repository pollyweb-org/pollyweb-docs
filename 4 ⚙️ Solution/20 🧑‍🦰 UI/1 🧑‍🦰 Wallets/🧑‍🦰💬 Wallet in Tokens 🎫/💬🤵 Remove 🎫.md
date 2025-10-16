# 🧑‍🦰💬🤵 Remove token @ Wallet


> Implements a [Wallet 🧑‍🦰 app](<../🧑‍🦰🛠️ Wallet app.md>)


* When users ask their [Broker 🤵](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) to remove a [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>),
  - it first does a soft delete only, hiding the [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>)
  - the removal only happens after a period of time (e.g., 30 days);
  - this allows users to undo the removal for a short period.

<br/>

## Chat 💬

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| | | > [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>)
| | | > [Broker 🤵](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) 
| 🤵 [Broker](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>)  | 😃 What do you need? <br/> - [ Remove ] token | > Remove
| 🤵 [Broker](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>)  | ✅ Token removed. <br/> - [ Undo ] removal
||

<br/>

## Flow diagram ⏩

![alt text](<../.📎 Assets/Tokens 📎/⚙️🎫 Remove.png>)



| # | API | Description
|-|-|-
| 1 | [🧑‍🦰🐌🤗 `Home@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Home.md>) | The user calls the [Broker 🤵](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) from the [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>)
| 2 | [🤗⏩🧑‍🦰 Prompt 🤔](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Then tells the [Broker 🤵](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) to remove the [Token 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) 
| 3 | [🤵⏩🧑‍🦰 Update Tokens 🎫](<../../3 🤵 Brokers/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Tokens 🎫.md>) | The [Broker 🤵](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) tells the [Wallet 🧑‍🦰](<../🧑‍🦰🛠️ Wallet app.md>) to update the list
| 4 | [🤵🐌📣 `Remove@Notifier`](<../../2 📣 Notifiers/📣🅰️ Notifier methods/4 🎫 Tokens/3 🤵🐌📣 Remove.md>) | The [Broker 🤵](<../../3 🤵 Brokers/🤵🤲 Broker helper.md>) tells the [Wallet 🧑‍🦰](<../🧑‍🦰🛠️ Wallet app.md>) to remove it
||

<br/>

## Talker handler 😃 

```yaml
💬 Handler:

# Get the Wallet 🧑‍🦰
- MAP|Wallets|$.Msg.Header.From >> $wallet

# Verify the Message.
- VERIFY|$.Msg|$wallet.PublicKey

# Get the Token 🎫
- MAP|$wallet.Tokens|$.Msg.Body.Key >> $token

# Ask for an actions.
- ONE|What do you need?:
    - /Remove token

# Execute the action.
- CASE:
    Remove: RUN|RemoveToken
```

```yaml
RemoveToken:

# Ask for confirmation 🤔
- CONFIRM|Remove token {$token.Title}?

# Remove the Token 🎫
- DELETE|$token >> $delete:
    Soft: 30 days

    OnSoft: 
        # Update the Token 🎫 list
        - MSG|Updated@Notifier|$wallet.Notifier:
            WalletID: $wallet.ID
            Updates: [ TOKENS ]

    OnHard:
        # Remove from Wallet
        - MSG|Remove@Notifier|$wallet.Notifier:
            WalletID: $wallet.ID
            Path: $token.Path

# Inform the user 🤔
- SUCCESS|Token removed.:
    Options: 
        - /Undo removal

# Undo the removal.
- CASE:
    Undo: RUN|UndoRemoval
```

```yaml
UndoRemoval:

# Cancel the soft delete.
- UNDO|$delete

# Inform the user 🤔
- SUCCESS|Token restored.
```
