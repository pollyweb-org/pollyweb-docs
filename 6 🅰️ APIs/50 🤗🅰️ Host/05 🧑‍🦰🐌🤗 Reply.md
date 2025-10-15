# 🧑‍🦰🐌🤗 Reply @ Host

> A [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) replies to a [Prompt 🤔](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) of a [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) in a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) flow.

> Signature of the [Message 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>):
> <br>• signed with the `PrivateKey` from [`Converse@Notifier`](<../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Converse.md>)
> <br>• verified with the `PublicKey` from [`Hello@Host`](<01 🤵🐌🤗 Hello.md>)


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
|           | `To`          | string    | [Sender 🤗](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) from [`Prompt@Notifier`](<../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Prompt.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `ChatID` | uuid | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Prompt@Notifier`](<../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Prompt.md>)
||`PromptID`    | uuid      | [Prompt 🤔](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) ID from [`Prompt@Notifier`](<../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Prompt.md>)
|| `Result`| enum | `OK` `CANCEL` `YES` `NO` 
|| `Answer` | any | Answer to the [Prompt 🤔](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>)
|
