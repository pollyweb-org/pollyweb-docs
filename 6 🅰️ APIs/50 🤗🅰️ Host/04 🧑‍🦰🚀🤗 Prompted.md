# 🧑‍🦰🚀🤗 Prompted @ Host

> Downloads the content of a [Prompt 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>).

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) flow


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
|           | `To`          | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `ChatID` | uuid | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
|| `PromptID`    | uuid      | [Prompt 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) ID from [`Prompt@Broker`](<../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>)
|

<br/>


## Sync Response


```yaml
Format: ONE
Message: Which credit card to use?
MinLength: 1
MaxLength: 5
MinValue: 10000
MaxValue: 99999
Emoji: 😕
Attachment: <attachment-uuid>
Details: |
    **Note**: each cards has its own fees.
    * Check the fees for the transaction.
Options: 
    - ID: 1
      Translation: Personal
```

|Object |Property|Type|Description
|-|-|-|-
|Top| `Format`  | string | One format supported by [Prompts 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>)
|| `Message` | string | Main message,  to display in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|| `MinLength` | int | Optional minimum length
|| `MaxLength` | int | Optional maximum length
|| `MinValue` | int | Optional minimum value
|| `MaxValue` | int | Optional maximum value
|| `Emoji` | string | Optional emoji for [Input Prompts 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 Blocking input prompts.md>)
|| `Attachment`| uuid   | File to download via [Download@Host 🚀](<06 🧑‍🦰🚀🤗 Download.md>)
|| `Details` | string | Extended details in Markdown format,<br/> - typically hidden by an expand [+] sign
|| `Options` | object[]   | List of `Option` objects
|Option | `ID`          | string  | ID of the option, <br/> - for replies via [Reply@Host 🐌](<05 🧑‍🦰🐌🤗 Reply.md>)
|       | `Translation` | string  | Text of the option, <br/>- to display in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|

<br/>

