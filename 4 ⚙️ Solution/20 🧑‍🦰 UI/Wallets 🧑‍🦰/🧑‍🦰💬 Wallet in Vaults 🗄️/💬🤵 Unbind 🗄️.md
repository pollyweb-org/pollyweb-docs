<!-- https://quip.com/b8a0AHaXf3C6#temp:C:DPSe1a859381bc449598713c8c71 -->

# 🧑‍🦰💬🤵 Unbind @ Wallet

> Implements a [Wallet 🧑‍🦰 app](<../🧑‍🦰🛠️ Wallet app.md>)


* Scenario: the user wants to unbind from a [Vault 🗄️ domain](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>).

<br/>

## Chat

> Implemented by [Pop Vault 🔆 handler](<../../Brokers 🤵/🤵🔆 Broker locators/🤵🔆 Pop Vault.md>).

| [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
...
| 🗄️ [Vault](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | ✅ Done. Your wallet is bound.
| | | > Broker 🤵 |
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 What do you need? <br/> - [ Unbind ] vault <br/> - [ Something else ] | > Unbind
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Which codes? [All, No] <br/> - [ ] Some schema code 🧩 <br/> - [ ] Some other schema code 🧩 | > All
| 🤵 [Broker](<../../Brokers 🤵/🤵🤲 Broker helper.md>) | ✅ Codes unbound.
||

<br/>


## Flow diagram

![alt text](<../.📎 Assets/Binds 📎/⚙️ Unbind vault.png>)


| # | Call | Notes
|-|-|-
| 1 | [🧑‍🦰🐌🤵 `Pop@Broker`](<../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>) | Call the [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) in a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>)  with a [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
| 2 | [🤗⏩🧑‍🦰 `Prompt@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Ask the [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) to remove the  [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| 3 | [🤵⏩🧑‍🦰 Update Binds 🔗](<../../Brokers 🤵/🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Binds 🔗.md>) | Asks the [Wallet 🧑‍🦰](<../🧑‍🦰🛠️ Wallet app.md>) to update the [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| 4 | [🤵🐌🗄️ `Unbound@Vault`](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Unbound.md>) | The [Broker 🤵](<../../Brokers 🤵/🤵🤲 Broker helper.md>) unbinds and informs the [Vault 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)
|



<br/>

## [Talker 😃](<../../../35 💬 Chats/😃 Talkers/😃 Talker.md>)

> Called by [`Pop@Broker`](<../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)

> Assumes a `$wallet` placeholder from [`Pop@Broker`](<../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)


```yaml
# Get the Vault 
- GET >> $vault:
    Pool: $wallet.Vaults
    Key: $.Msg.Body.Key

# Ask for confirmation 🤔
- CONFIRM|Unbind vault {$vault.Title}?

# Filter the binds.
- FILTER|Which ones? >> $binds:
    Options: $vault.Binds
    ID: Bind
    Title: Schema$

# Remove each bind
- PARALLEL|$vault.Binds|$bind:

    # Delete the Bind
    - DELETE|$bind
    
    # Inform the Vault
    - SEND:
        To: $bind.Vault
        Subject: Unbound@Vault
        Bind: $bind.ID

# Update the bind list
- SEND:
    To: $wallet.Notifier
    Subject: Updated@Notifier
    Wallet: $wallet.ID
    Updates: [ BINDS ]

# Inform the user 🤔
- SUCCESS|Done.
```

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| 👍 [`CONFIRM`](<../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) | To pause for user confirmation
| 🔽 [`FILTER`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/FILTER 🔽 msg.md>) | Filter the [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to remove
| ⏬ [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Hook 🪝](<../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) from [`Bindable@Broker`](<../../Brokers 🤵/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)  
| ️️*️⃣ [`PARALLEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/PARALLEL *️⃣.md>) | Process each [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
|