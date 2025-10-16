# 🧑‍🦰🐌🤗 Reply @ Host

> A [Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) replies to a [Prompt 🤔](<../../../35 Chats/🤔 Prompts/🤔 Prompt.md>) of a [Host 🤗 domain](<../🤗🎭 Host role.md>) in a [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow.

> Signature of the [Message 📨](<../../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>):
> <br>• signed with the `PrivateKey` from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
> <br>• verified with the `PublicKey` from [`Hello@Host`](<🤵🐌🤗 Hello.md>)


<br/>

## Async Message 🐌

```yaml
Header:
    From: Anonymous
    To: any-host.com
    Subject: Reply@Host
Body: 
    ChatID: <chat-uuid>
    PromptID: <prompt-uuid>
    Result: OK # Default
    Answer: [Starter, Main, Coffee]
```


|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | `Anonymous`
|           | `To`          | string    | [Sender 🤗](<../🤗🎭 Host role.md>) from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `ChatID` | uuid | [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) ID from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
||`PromptID`    | uuid      | [Prompt 🤔](<../../../35 Chats/🤔 Prompts/🤔 Prompt.md>) ID from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|| `Result`| enum | `OK` `CANCEL` `YES` `NO` 
|| `Answer` | any | Answer to the [Prompt 🤔](<../../../35 Chats/🤔 Prompts/🤔 Prompt.md>)
|
