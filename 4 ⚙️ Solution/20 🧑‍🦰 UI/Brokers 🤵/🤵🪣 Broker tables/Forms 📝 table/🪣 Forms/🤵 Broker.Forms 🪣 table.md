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

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

```yaml
Parents: Chats
```

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`OnFormInform` 📃 handler](<../🪣🧱 1 Inform 🔔/🤵 OnFormInform 🔔 handler.md>) [`OnFormInformed` 📃 handler](<../🪣🧱 1 Informed 🔔/🤵 OnFormInformed 🔔 handler.md>).

```yaml