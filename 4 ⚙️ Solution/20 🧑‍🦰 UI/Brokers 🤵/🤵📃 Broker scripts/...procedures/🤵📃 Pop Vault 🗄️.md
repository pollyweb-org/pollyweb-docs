<!-- TODO: Add lists of commands. -->
<!-- TODO: Add initial parser. -->

# 🤵📃 Pop Vault 🗄️

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Unbind Vault` 💬 flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Vaults 🗄️/💬🤵 Unbind 🗄️.md>) 

> Called by the [`Pop@Broker` 📃 script](<../...handlers/🤵📃 Pop 💬 handler.md>)


<br/>


## Script



> Assumes a `$wallet` placeholder from the [`Pop@Broker` 📃 script](<../...handlers/🤵📃 Pop 💬 handler.md>)


```yaml
📃 PopVault:

# Verify the inputs
- ASSERT:
    - $wallet

# Get the Vault 
- GET >> $vault:
    Set: $wallet.Vaults
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

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`CONFIRM`](<../../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) [`FILTER`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/FILTER 🔽 msg.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>)  [`PARALLEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/PARALLEL *️⃣.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) [`SUCCESS`](<../../../../35 💬 Chats/🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Hook` 🪣](<../../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/$Placeholder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) 
|

| [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 🔽 [`FILTER`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/FILTER 🔽 msg.md>) | Filter the [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to remove
| ⏬ [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [`Hook` 🪣](<../../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) from [`Bindable@Broker`](<../../🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)  
| 📬 [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) | Call [`Updated@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)
|