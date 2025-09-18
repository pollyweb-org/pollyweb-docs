<!-- #TODO -->

# Prompted @ Host

> Download the content of a Prompt.

> Part of the [🤗⏩🧑‍🦰 Prompt](<../../5 ⏩ Flows/03 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) workflow.


## Sync Request


```yaml
Header: 
Body:
    ChatID: <session-uuid>
    PromptID: <prompt-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | Wallet app
|           | `To`          | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `ChatID`      | string    |
|           | `PromptID`    | string    | 
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
|Top| `Format`  | string | One supported by a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
|| `Message` | string | Main message displayed in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
|| `Options` | list   | List of Option objects
|| `Appendix`| UUID   | PDF or PNG appendix to download via [Download@Host](<06 🧑‍🦰🚀🤗 Download.md>)
|| `Details` | string | Extended details in Markdown format, topically hidden by an expand [+] sign
|Option | `ID`          | string  | ID of the option on the Prompt for replies via [Reply@Host](<05 🧑‍🦰🐌🤗 Reply.md>)
|       | `Translation` | string  | Text of the option to display in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>)
|

<br/>


## FAQ

1. **Is the `ChatID` really necessary?**

    The `ChatID` should not be necessary, because the `PromptID` should be enough to index the prompt. 
    * However, the `ChatID` is added to ensure the `PromptID` is from that the expected [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>), 
    * and to allow [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>) to have a top index on the `ChatID` with a secondary index on the `PromptID`.

    ---
    <br/>