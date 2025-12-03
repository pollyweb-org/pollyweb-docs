# 🪣 Shares

> Purpose
* Manages the lifecycle of requests to the [`Disclose@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>).

<br/>

## Lifecycle

![alt text](<🗄️ Vault.Shares ⚙️ uml.png>)

<br/>

## State Transitions

| [State 🛢](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 State.md>) | Blame | Description | Action
|-|-|-|-|
|🗄️ [`ASKED`](<../🪣🔔 1 Asked/🗄️ OnShareAsked 📃 handler.md>)| [`Disclose@` 🐌](<../../../🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 📃 handler.md>) | Just asked by a [Broker 🤵](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Trusts@Graph` 🚀](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)
|`UNTRUSTED`| [`OnAsked` 🔔](<../🪣🔔 1 Asked/🗄️ OnShareAsked 📃 handler.md>) | [Consumer 💼](<../../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) is not [Trusted 🫡](<../../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>)
|🗄️ [`TRUSTED`](<../🪣🔔 2 Trusted/🗄️ OnShareTrusted 📃 handler.md>)| [`OnAsked` 🔔](<../🪣🔔 1 Asked/🗄️ OnShareAsked 📃 handler.md>) | [Consumer 💼](<../../../../Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) is [Trusted 🫡](<../../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) | [`Handle@Hosted` 🐌](<../../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>)
|🗄️ [`READY`](<../🪣🔔 3 Ready/🗄️ OnShareReady 📃 handler.md>)| [`OnTrusted` 🔔](<../🪣🔔 2 Trusted/🗄️ OnShareTrusted 📃 handler.md>) | Ready for [`Collect@` 🚀](<../../../🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>) | [`Consume@Consumer` 🐌](<../../../../Consumers 💼/💼🅰️ Consumer methods/Consume 🗄️🐌💼/💼 Consume 🐌 msg.md>)


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

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`OnAsked`](<../🪣🔔 1 Asked/🗄️ OnShareAsked 📃 handler.md>) [`OnTrusted`](<../🪣🔔 2 Trusted/🗄️ OnShareTrusted 📃 handler.md>) [`OnReady`](<../🪣🔔 3 Ready/🗄️ OnShareReady 📃 handler.md>)

```yaml
Handlers:
    ASKED   >> OnShareAsked:     # Calls Trusts@Graph
    TRUSTED >> OnShareTrusted:   # Calls Handle@Hosted
    READY   >> OnShareReady:     # Calls Consume@Consumer
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <share-uuid>

# From Disclose@Vault
Bind: <bind-uuid>           # Vault bind to share
Chat: <chat-uuid>           # Broker chat
Hook: <hook-uuid>           # Hook for Consume@Consumer
Language: en-us             # Data language
Consumer: any-consumer.dom  # Data requester

# From OnShareTrusted
Data: {...}
```

