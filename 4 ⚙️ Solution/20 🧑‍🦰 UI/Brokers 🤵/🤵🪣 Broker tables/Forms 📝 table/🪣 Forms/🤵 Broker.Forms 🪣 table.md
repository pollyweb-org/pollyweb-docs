# 🤵 Broker.Informs 🪣 table

> About
* Implements the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>)
* Part of the [`Inform` ⏩ flow](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)


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
    AllOf: Chat, Wait, Consumer, Form
    UUIDs: Chat, Wait
    Texts: Form, Consumer
    Consumer.IsDomain:
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <inform-uuid>   
```

From [`Inform@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Share 💼 Inform 💼🐌🤵/🤵 Inform 📃 handler.md>)

```yaml
Chat: <chat-uuid>           # Chat where the inform was created
Wait: <wait-uuid>           # Consumer wait to notify
Name: AnyForm               # Form name being informed about
Consumer: any-consumer.dom  # Consumer being informed
```

From [`OnFormInform` 📃 handler](<../🪣🧱 1 Inform 🔔/🤵 OnFormInform 🔔 handler.md>)

```yaml
Schemas: 
  - .CURATOR/CURATE
  - .PAYER/CHARGE
```