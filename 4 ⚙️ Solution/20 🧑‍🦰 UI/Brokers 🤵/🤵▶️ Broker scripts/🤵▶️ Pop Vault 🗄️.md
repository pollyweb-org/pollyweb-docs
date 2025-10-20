<!-- TODO: Add lists of commands. -->
<!-- TODO: Add initial parser. -->


# 🔆 Locator: Pop Vault 

> [Script ▶️](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/▶️ Script.md>) that implements the [`Unbind Vault` 💬 flow](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>) 


<br/>


## Script

> Called by [`Pop@Broker` 🅰️ method](<../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)

> Assumes a `$wallet` placeholder from [`Pop@Broker` 🅰️](<../../Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Pop.md>)


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
| 📬 [`SEND`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) | Call [`Updated@Notifier`](<../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/3 🤵🐌📣 Updated.md>)
{{SUCCESS}}||
|