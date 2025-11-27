# 🤵🪣 Prompts @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

## Data access

|Actor|Save|Read
|-|:-:|:-:
| [`Prompt` 📃 handler](<../../../🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 📃 handler.md>) | X | 
| [`OnPromptInserted` 📃 handler](<../🪣🧱 1 Inserted 🔔/🤵 OnPromptInserted 📃 handler.md>) | X | X
| [`OnPromptEmojied` 📃 handler](<../🪣🧱 2 Emojied 🔔/🤵 OnPromptEmojied 📃 handler.md>) | |X 

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Prompts
Item: Prompt

Parents:
    Wallet: { Wallets.ID: Prompt.Wallet }
    Chatter: { Chatter.ID: Prompt.Chatter }
```



## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Prompt@Broker 
ID: <prompt-uuid>       # ID on the Prompt
Chat: <chat-uuid>       # Chat where the Prompt was sent
Hook: <hook-uuid>       # Hook for the Host for replies
Role: VAULT             # Role of the Chatter sending the Prompt
Format: INFO            # Format of the Prompt
Sender: any-host.dom    # Sender of the Prompt
Wallet: <wallet-uuid>   # Wallet to send the Prompt
Expires: 2024-12-31T23:59:59Z  # Cache expiration time 
Notifier: any-notifier.dom  # Notifier to forward the Prompt
ChatEmoji: 🤔           # Emoji of the Chat
PromptEmoji: 🤔         # Emoji of the Prompt

# From OnPromptInserted
Emoji: 🤔               # Final emoji of the Prompt
```

