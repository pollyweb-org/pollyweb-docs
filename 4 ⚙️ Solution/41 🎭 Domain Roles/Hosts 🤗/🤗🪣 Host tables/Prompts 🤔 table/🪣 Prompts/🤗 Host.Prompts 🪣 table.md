<!-- TODO -->

# 🤗 Host.Prompts 🪣 table

> About
* Part of [Host 🤗 domains](<../../../🤗 Host role/🤗🎭 Host role.md>)
* Stores [Prompts 🤔](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) sent to [Wallets 🧑‍🦰](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) via [Brokers 🤵](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>)

<br/>

## Lifecycle

![alt text](<🤗 Host.Prompts ⚙️ uml.png>)

<br/>

## Schema

Here's the [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml
Prefix: Host
Table: Prompts
```

<br/>

Here's the [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) definition, referencing [`Host.Chats`](<../../Chats 💬 table/🪣 Chats/🤗 Host.Chats 🪣 table.md>)

```yaml
Parents: Chat
```

<br/>

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>): [`Inserted`](<../🪣🔔 11 Inserted/🤗 OnHostPromptInserted 🔔 handler.md>) [`Translated`](<../🪣🔔 12 Translated/🤗 OnHostPromptTranslated 🔔 handler.md>) [`Replied`](<../🪣🔔 13 Replied/🤗 OnHostPromptReplied 🔔 handler.md>)

```yaml
Handlers:
    INSERT     >> OnPromptInserted
    TRANSLATED >> OnPromptTranslated
    REPLIED    >> OnPromptReplied
```

<br/>

## Example

```yaml
# Automatic, on INSERT
ID: <prompt-uuid>

# From the Talker
Broker: any-broker.dom
Chat: <chat-uuid>
```
