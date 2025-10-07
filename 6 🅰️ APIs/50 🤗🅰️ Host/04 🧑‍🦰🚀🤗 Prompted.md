# 🧑‍🦰🚀🤗 Prompted @ Host

> Downloads the content of a [Prompt 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>).

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) flow


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
MinValue: 10000                     # Optional
MaxValue: 99999                     # Optional
Appendix: <attachment-uuid>       # Optional
Details: |                          # Optional
    **Note**: each cards has its own fees.
    * Check the fees for the transaction.
Options:                            # Optional
    - ID: 1                     
      Translation: Personal     
```

||Property|Type|Description
|-|-|-|-
|| [`Format`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>)  | string | One format supported by [Prompts 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>)
|| `Message` | string | Main message,  to display in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|| [`MinValue`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/13 ✏️📋 Input validation.md>) | int | Optional minimum value
|| [`MaxValue`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/13 ✏️📋 Input validation.md>) | int | Optional maximum value
|| [`Appendix`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/05 🤔📎 with Attachments.md>)| uuid   | File to download via [`Download@Host`](<06 🧑‍🦰🚀🤗 Download.md>)
|| [`Details`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 🤔⊕ with Details.md>) | string | Extended [details](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 🤔⊕ with Details.md>) in Markdown format
|| [`Options`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/04 🤔🔘 with Options.md>) | object[]   | List of `Option` objects
|Option | `ID`          | string  | ID of the [option](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/04 🤔🔘 with Options.md>) for [`Reply@Host`](<05 🧑‍🦰🐌🤗 Reply.md>)
|       | `Translation` | string  | Text of the [option](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/04 🤔🔘 with Options.md>) to display in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|

<br/>

