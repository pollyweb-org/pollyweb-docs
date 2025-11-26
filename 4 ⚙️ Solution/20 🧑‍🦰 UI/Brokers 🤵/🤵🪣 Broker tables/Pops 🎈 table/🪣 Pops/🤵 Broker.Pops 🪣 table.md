# 🤵🪣 Pops @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

<br/>

## Lifecycle

![alt text](<🤵 Broker.Pops ⚙️ uml.png>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Pops.yaml

Prefix: Broker
Table: Pops
Item: Pop

Parents:
    Wallet: { Wallets.ID: Pops.Wallet }
    Chat: { Chats.ID: Pops.Chat }
    Token: 
        Tokens.Token: Pops.Inputs.Key.Token
        Tokens.Issuer: Pops.Inputs.Key.Issuer 

Handlers:

    OnPopInserted: # Open a Chat 💬
        Events: INSERTED

    OnPopWallet: # Wallet 🧑‍🦰 pop-up menu
        Events: POPPED
        Assert: Context.Is(WALLET)
        
    OnPopChat: # Chat 💬 pop-up menu
        Events: POPPED
        Assert: Context.Is(CHAT)

    OnPopBind: # Bind 🔗 pop-up menu
        Events: POPPED
        Assert: Context.Is(BIND)
    
    OnPopToken: # Token 🎫 pop-up menu
        Events: POPPED
        Assert: Context.Is(TOKEN)

    OnPopTokenRevised: # Notify the user
        Events: POPPED
        Assert: Context.Is(TOKEN.REVISED)
```

## Links

| Link | Table | Contains
|-|-|-
| Parents   | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) | [Wallets 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <pop-uuid> 

# From Pop@Broker 
Hook: <hook-uuid>       # Hook for the Wallet to map the Chat ID
Wallet: <wallet-uuid>   # Wallet owning the pop
Context: BIND
Key: <context-uuid>
```

Property|Type|Details|Origin|Purpose
|-|-|-|-|-
|`ID`|uuid | Pop ID | (auto)
|`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID | [`Pop@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [`Open@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
| `Hook` | uuid | Event ID on [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | [`Pop@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [`Open@Notifier`](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
| `Context` | text | `BIND` `TOKEN` ... | [`Pop@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | Select handler
|