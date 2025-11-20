# 🤵🪣 Prompts @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)


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
Hook: <hook-uuid>       # Hook for the Host for replies
Format: INFO            # Format of the Prompt
Role: VAULT             # Role of the Chatter sending the Prompt
Wallet: <wallet-uuid>   # Wallet to send the Prompt
```

