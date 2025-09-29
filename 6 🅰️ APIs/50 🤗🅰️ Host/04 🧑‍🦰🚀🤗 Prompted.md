# 🧑‍🦰🚀🤗 Prompted @ Host

> Downloads the content of a [Prompt 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/02 🤔 Prompt.md>).

> Part of the [🤗⏩🧑‍🦰 Prompt @ Host](<../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) workflow

> Referenced by the [🤗🐌🤵 Prompt @ Broker](<../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>) method

<br/>

## Sync Request 🚀


```yaml
Header: 
    From: Anonymous
    To: any-host.com
    Subject: Prompted@Host

Body:
    PromptID: <prompt-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | `Anonymous`
|           | `To`          | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `PromptID`    | uuid      | [Prompt 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/02 🤔 Prompt.md>) ID sent on [Prompt@Broker](<../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>)
|

<br/>


## Sync Response


```yaml
Format: ONE
Message: Which credit card to use?
Options: 
    - ID: 1
      Translation: Personal
Appendix: <appendix-uuid>
Details: |
    **Note**: each cards has its own fees.
    * Check the fees for the transaction.
```

|Object |Property|Type|Description
|-|-|-|-
|Top| `Format`  | string | One format supported by [Prompts 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/02 🤔 Prompt.md>)
|| `Message` | string | Main message, <br/>- to display in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
|| `Options` | object[]   | List of Option objects
|| `Appendix`| uuid   | PDF or PNG appendix, <br/>- to download via [Download@Host](<06 🧑‍🦰🚀🤗 Download.md>)
|| `Details` | string | Extended details in Markdown format,<br/> - typically hidden by an expand [+] sign
|Option | `ID`          | string  | ID of the option, <br/> - for replies via [Reply@Host](<05 🧑‍🦰🐌🤗 Reply.md>)
|       | `Translation` | string  | Text of the option, <br/>- to display in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
|

<br/>

