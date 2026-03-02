# 🗄️ Vault.Discloses 🪣 table

> Purpose
* Manages the lifecycle of requests to the [`Disclose@Vault` 🐌 msg](<../../../🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>).

<br/>

## Lifecycle

![alt text](<🗄️ Vault.Discloses ⚙️ uml.png>)

<br/>

## State Transitions

| [State 🛢](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 State.md>) | Blame | Description | Action
|-|-|-|-|
|🗄️ [`ASKED`](<../🪣🔔 1 Asked/🗄️ OnAsked 📃 handler.md>)| [`Disclose@` 🐌](<../../../🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 📃 handler.md>) | Just asked by a [Broker 🤵](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | [`Trusts@Graph` 🚀](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)
|`UNTRUSTED`| [`OnAsked` 🔔](<../🪣🔔 1 Asked/🗄️ OnAsked 📃 handler.md>) | [Consumer 💼](<../../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) is not [Trusted 🫡](<../../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)
|🗄️ [`TRUSTED`](<../🪣🔔 2 Trusted/🗄️ OnTrusted 📃 handler.md>)| [`OnAsked` 🔔](<../🪣🔔 1 Asked/🗄️ OnAsked 📃 handler.md>) | [Consumer 💼](<../../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) is [Trusted 🫡](<../../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) | [`Handle@Hosted` 🐌](<../../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>)
|🗄️ [`READY`](<../🪣🔔 4 Ready/🗄️ OnReady 📃 handler.md>)| [`OnTrusted` 🔔](<../🪣🔔 2 Trusted/🗄️ OnTrusted 📃 handler.md>) | Ready for [`Collect@` 🚀](<../../../🗄️📨 Vault msgs/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>) | [`Consume@Consumer` 🐌](<../../../../Consumers 💼/💼📨 Consumer msgs/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)


<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
Prefix: Vault
Table: Shares
Item: Share
```

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Vault.Binds`](<../../Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>)

```yaml
Parents: 
    Bind  # Bind being disclosed in the share
```

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`OnAsked`](<../🪣🔔 1 Asked/🗄️ OnAsked 📃 handler.md>) [`OnTrusted`](<../🪣🔔 2 Trusted/🗄️ OnTrusted 📃 handler.md>) [`OnReady`](<../🪣🔔 4 Ready/🗄️ OnReady 📃 handler.md>)

```yaml
Handlers:
    ASKED   >> OnShareAsked:     # Calls Trusts@Graph
    TRUSTED >> OnShareTrusted:   # Calls Handle@Hosted
    READY   >> OnShareReady:     # Calls Consume@Consumer
```

Here's [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    # Group assertions
    AllOf: Broker, Chat, Query, Schema
    UUIDs: Chat, Query
       
    # From Disclose@Broker
    Broker.IsDomain:
    Schema.IsSchema:
    Consumer.IsDomain:
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <share-uuid>
```

From the [`Disclose@Vault` 🐌 msg](<../../../🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)

```yaml
Bind: <bind-uuid>           # Vault bind to share
Chat: <chat-uuid>           # Broker chat
Query: <query-uuid>         # Hook for Consume@Consumer
Broker: any-broker.dom      # Broker that sent the request
Consumer: any-consumer.dom  # Data requester
```

From [`OnTrusted` 📃 handler](<../🪣🔔 2 Trusted/🗄️ OnTrusted 📃 handler.md>)

```yaml
Context: {...}
```

From [`OnDetailed` 📃 handler](<../🪣🔔 3 Detailed/🗄️ OnDetailed 📃 handler.md>)

```yaml
Data: {...}
``` 

