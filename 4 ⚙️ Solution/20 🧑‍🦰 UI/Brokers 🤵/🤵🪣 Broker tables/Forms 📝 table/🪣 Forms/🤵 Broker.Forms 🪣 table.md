# 🤵 Broker.Informs 🪣 table

> About
* Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

<br/>

## Lifecycle

![alt text](<🤵 Broker.Forms ⚙️ uml.png>)


<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Informs
Item: Inform
```

<br/>

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

```yaml
Parents: Chats
```

<br/>

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`OnInform`](<../🪣🧱 1 Inform 🔔/🤵 OnFormInform 🔔 handler.md>) [`OnInformed`](<../🪣🧱 1 Informed 🔔/🤵 OnFormInformed 🔔 handler.md>)

```yaml
Handlers:
    INFORM            >> OnFormInform:
    INFORM > INFORMED >> OnFormInformed:
```

The [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition is:

```yaml
Assert: 
    AllOf: Chat, Hook, Consumer, Form
    UUIDs: Chat, Hook
    Texts: Form, Consumer
    Consumer.IsDomain:
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <inform-uuid>   

# From Inform@Host
Chat: <chat-uuid>           # Chat where the inform was created
Hook: <hook-uuid>           # Consumer hook to notify
Form: AnyForm               # Form being informed about
Consumer: any-consumer.dom  # Consumer being informed

# From OnInform handler

```