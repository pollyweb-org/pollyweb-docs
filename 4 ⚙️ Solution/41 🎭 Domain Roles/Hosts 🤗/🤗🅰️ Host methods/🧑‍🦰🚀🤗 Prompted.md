# 🧑‍🦰🚀🤗 Prompted @ Host

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow

> Signature of the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>):
> <br>• signed with the `PrivateKey` from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
> <br>• verified with the `PublicKey` from [`Hello@Host`](<🤵🐌🤗 Hello.md>)

* Downloads the content of a [Prompt 🤔](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>).

<br/>

## Sync Request 🚀


```yaml
Header: 
    From: Anonymous
    To: any-host.dom
    Subject: Prompted@Host

Body:
    Chat: <chat-uuid>
    Prompt: <prompt-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | `Anonymous`
|           | `To`          | string    | [Sender 🤗](<../🤗🎭 Host role.md>) from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `Chat` | uuid | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|| `Prompt`    | uuid      | [Prompt 🤔](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) ID from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
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
      Title: Personal     
      Locator: .HOST,any-host.dom,7V8KD3G
```

|Property|Type|Description
|-|-|-
| [`Format`](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>)  | string | One format supported by [Prompts 🤔](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>)
| [`Statement`](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/2 🪧 Statement.md>) | string | Main message,  to display in the [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>)
| [`MinValue`](<../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt input features/13 📋 Input validation.md>) | int | Optional minimum value
| [`MaxValue`](<../../../35 💬 Chats/🤔 Prompts/🤔✏️ Prompt input features/13 📋 Input validation.md>) | int | Optional maximum value
| [`Appendix`](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/5 📎 with Appendix.md>)| uuid   | File to download via [`Download@Host`](<🧑‍🦰🚀🤗 Download.md>)
| [`Details`](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | string | Extended [details](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/3 ⊕ with Details.md>) in Markdown format
| [`Options`](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/4 🔘 with Options.md>) | object[]   | List of `Option` objects
|

### Option object

|Property|Type|Description
|-|-|-
| `ID`          | string  | ID of the [option](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/4 🔘 with Options.md>) for [`Reply@Host`](<🧑‍🦰🐌🤗 Reply.md>)
| `Title` | string  | Text of the [option](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/4 🔘 with Options.md>) to be displayed
| `Locator` | string | Optional [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to [Assess ⏩](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🤗 Click locator 🔆.md>)
|

<br/>

