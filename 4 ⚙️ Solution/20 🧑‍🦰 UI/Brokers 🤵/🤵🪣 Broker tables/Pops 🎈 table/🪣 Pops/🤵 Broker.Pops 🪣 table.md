# 🤵🪣 Pops @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Data access
* [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by [`OnPopInserted` 🔔](<../🪣🧱 12 Pop 🔔 event/🤵 OnPopInserted 🔔 handler.md>) after [`Pop@Broker` 🅰️](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)
* [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by [`OnTokenRevised` 🔔](<../../Tokens 🎫 table/🪣🧱 71 Revised 🔔 event/🤵 OnTokenRevised 🔔 handler.md>) after [`Revise@Broker` 🅰️](<../../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)

<br/>

## Lifecycle

![alt text](<../🪣🧱 11 Pop ⏩ flow/🤵 Broker.Pops.Pop ⚙️ uml.png>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Pops
Item: Pop
```

<br/>

Here's the [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) definition.

```yaml
Parents:

    Wallet: # Wallet that called Pop@Broker
        Wallets.ID: Pops.Wallet

    Chat: # Chat created for the Pop-up
        Chats.ID: Pops.Chat

    Token: # Token that inserted a Pop on Revise@Broker
        Tokens.Token: Pops.Inputs.Key.Token
        Tokens.Issuer: Pops.Inputs.Key.Issuer 
```
🪣 References: [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Broker.Tokens`](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) [`Broker.Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) 

<br/>

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
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
Calls: 
* [`OnPopInserted` 🔔 handler](<../🪣🧱 12 Pop 🔔 event/🤵 OnPopInserted 🔔 handler.md>) 
* [`OnPopWallet` 🔔 handler](<../🪣🧱 21 Wallet 🔔/🤵 OnPopWallet 🔔 handler.md>) 
* [`OnPopChat` 🔔 handler](<../🪣🧱 31 Chat 🔔/🤵 OnPopChat 🔔 handler.md>) 
* [`OnPopBind` 🔔 handler](<../🪣🧱 51 Bind 🔔/🤵 OnPopBind 🔔 handler.md>) 
* [`OnPopToken` 🔔 handler](<../🪣🧱 61 Token 🔔/🤵 OnPopToken 🔔 handler.md>) 
* [`OnPopTokenRevised` 🔔 handler](<../🪣🧱 65 Token.Revised 🔔/🤵 OnPopTokenRevised 🔔 handler.md>)

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