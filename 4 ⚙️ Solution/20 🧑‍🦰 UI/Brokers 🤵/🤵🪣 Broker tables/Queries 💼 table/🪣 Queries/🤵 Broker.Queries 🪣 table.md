# 🤵 Broker.Queries 🪣 table

> Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) helper

<br/>

## Lifecycle

![alt text](<🤵 Broker.Queries ⚙️ uml.png>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Queries
Item: Query
```

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Chatters`](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>)


```yaml
Parents: 
  - Chatter  # Chat participant who sent the Query
```

<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    AllOf: Chat, Hook, Schemas, Domain
    UUIDs: Chat, Hook
    Lists: Schemas
    Domain.IsDomain:
    Schemas.Each.IsSchema:
```

Uses: [`.Each`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Each ⓕ.md>) [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>) 


<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Query@Broker 
ID: <query-uuid>        # ID on the Query
Chat: <chat-uuid>       # Chat where the Query was sent
Hook: <hook-uuid>       # Hook to reply to the Consumer 
Domain: any-host.dom    # Sender of the Query
Schemas:                # List of acceptable schemas
  - any-authority.dom/ANY-SCHEMA  # Requested Schema 1
```

