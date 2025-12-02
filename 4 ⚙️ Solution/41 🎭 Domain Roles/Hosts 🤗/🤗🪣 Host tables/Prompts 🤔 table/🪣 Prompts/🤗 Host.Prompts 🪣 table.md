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

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition uses: [`Inserted`](<../🪣🔔 11 Inserted/🤗 OnHostPromptInserted 🔔 handler.md>) [`Translated`](<../🪣🔔 12 Translated/🤗 OnHostPromptTranslated 🔔 handler.md>) [`Asserted`](<../🪣🔔 13 Asserted/🤗 OnHostPromptAsserted 🔔 handler.md>) [`Replied`](<../🪣🔔 14 Replied/🤗 OnHostPromptReplied 🔔 handler.md>)

```yaml
Handlers:
    INSERT     >> OnPromptInserted
    TRANSLATED >> OnPromptTranslated
    ASSERTED   >> OnPromptAsserted
    REPLIED    >> OnPromptReplied
```

<br/>

```yaml
Asserts:
    AllOf: Text, Format
    Texts: Text, Format, Details, Emoji
    Lists: Options
    UUIDs: Appendix  
    Nums: MinValue, MaxValue
    Emoji.Length: 1
    MinValue.IsBelow: MaxValue
    Text.Length.IsBelow: 250
    Details.Length.IsBelow: 2500
    
    # Options validation
    Options.Each.AllOf: ID, Title
    Options.Each.AreTexts: ID, Title, Locator
```

<br/>

## Example

Automatic, from [Item 🛢 Keys](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Keys.md>).

```yaml
ID: <prompt-uuid>
```

From [`Prompts` 📃 script](<../../../../../35 💬 Chats/Talkers 😃/😃⏩ Talker flows/Send Prompts 😃⏩🧑‍🦰/😃 Prompts 📃 script.md>)

```yaml
Broker: any-broker.dom
Chat: <chat-uuid>
Language: en-us
```

From [`OnPromptInserted` 🔔 handler](<../🪣🔔 11 Inserted/🤗 OnHostPromptInserted 🔔 handler.md>)

```yaml
PublicKey: any-public-key
Expires: 2024-12-31T23:59:59Z
```