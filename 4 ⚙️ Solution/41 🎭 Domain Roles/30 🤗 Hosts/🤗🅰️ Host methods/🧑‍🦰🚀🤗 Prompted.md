# 🧑‍🦰🚀🤗 Prompted @ Host

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow

> Signature of the [Message 📨](<../../../40 👥 Domains/41 📨 Messages/📨 Message.md>):
> <br>• signed with the `PrivateKey` from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
> <br>• verified with the `PublicKey` from [`Hello@Host`](<🤵🐌🤗 Hello.md>)

* Downloads the content of a [Prompt 🤔](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>).

<br/>

## Sync Request 🚀


```yaml
Header: 
    From: Anonymous
    To: any-host.com
    Subject: Prompted@Host

Body:
    ChatID: <chat-uuid>
    PromptID: <prompt-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | `Anonymous`
|           | `To`          | string    | [Sender 🤗](<../🤗🎭 Host role.md>) from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `ChatID` | uuid | [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|| `PromptID`    | uuid      | [Prompt 🤔](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) ID from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|

<br/>


## Sync Response


```yaml
Format: ONE
Statement: Which credit card to use? 
MinValue: 10000                     # Optional
MaxValue: 99999                     # Optional
Appendix: <appendix-uuid>           # Optional
Details: |                          # Optional
    **Note**: each cards has its own fees.
    * Check the fees for the transaction.
Options:                            # Optional
    - ID: 1                     
      Translation: Personal     
      Locator: @HOST,any-host.com,7V8KD3G
```

|Property|Type|Description
|-|-|-
| [`Format`](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>)  | string | One format supported by [Prompts 🤔](<../../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>)
| [`Statement`](<../../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/02 🪧 Statement.md>) | string | Main message,  to display in the [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)
| [`MinValue`](<../../../../9 😃 Talkers/20 🤔 Prompts/2 ✏️ Input specs/13 📋 Input validation.md>) | int | Optional minimum value
| [`MaxValue`](<../../../../9 😃 Talkers/20 🤔 Prompts/2 ✏️ Input specs/13 📋 Input validation.md>) | int | Optional maximum value
| [`Appendix`](<../../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/05 📎 with Appendix.md>)| uuid   | File to download via [`Download@Host`](<🧑‍🦰🚀🤗 Download.md>)
| [`Details`](<../../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/03 ⊕ with Details.md>) | string | Extended [details](<../../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/03 ⊕ with Details.md>) in Markdown format
| [`Options`](<../../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/04 🔘 with Options.md>) | object[]   | List of `Option` objects
|

### Option object

|Property|Type|Description
|-|-|-
| `ID`          | string  | ID of the [option](<../../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/04 🔘 with Options.md>) for [`Reply@Host`](<🧑‍🦰🐌🤗 Reply.md>)
| `Translation` | string  | Text of the [option](<../../../../9 😃 Talkers/20 🤔 Prompts/1 📘 Prompt specs/04 🔘 with Options.md>) to be displayed
| `Locator` | string | Optional [Locator 🔆](<../../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) to [Assess ⏩](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/03 🧑‍🦰👉🤗 Prompt option.md>)
|

<br/>

