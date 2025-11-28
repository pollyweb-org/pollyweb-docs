<!-- TODO -->

# 🤗 Host.Prompts 🪣 table

## Lifecycle

![alt text](<🤗 Host.Prompts ⚙️ uml.png>)

<br/>

## Schema

Here's the [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml
Prefix: Host
Table: Prompts
```

Here's the [Item 🪣 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) definition.

```yaml
Parents: Chat
```

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
Handlers:
    INSERT     >> OnPromptInserted
    TRANSLATED >> OnPromptTranslated
    REPLIED    >> OnPromptReplied
```
Handlers: [`OnInserted`](<../🪣🔔 11 Inserted/🤗 OnHostPromptInserted 🔔 handler.md>) [`OnTranslated`](<../🪣🔔 12 Translated/🤗 OnHostPromptTranslated 🔔 handler.md>) [`OnReplied`](<../🪣🔔 13 Replied/🤗 OnHostPromptReplied 🔔 handler.md>)

<br/>

## Example

```yaml
# Automatic, on INSERT
ID: <prompt-uuid>

# From the Talker
Broker: any-broker.dom
Chat: <chat-uuid>
```
