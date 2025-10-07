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
Optional: True                  # Defaults to False
Hint: 123.123.123.123           # Optional
InputMask: 099.099.099.099      # Optional
OutputMask: 990.990.990.990     # Optional
MinLength: 1                    # Optional
MaxLength: 5                    # Optional
MinValue: 10000                 # Optional
MaxValue: 99999                 # Optional
Emoji: 😕                       # Defaults to 😃🫥
Attachment: <attachment-uuid>   # Optional
Details: |                      # Optional
    **Note**: each cards has its own fees.
    * Check the fees for the transaction.
Options:                        # Optional
    - ID: 1                     # Example format from:
      Translation: Personal     # - str, str[], object
```

||Property|Type|Description
|-|-|-|-
|| [`Format`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>)  | string | One format supported by [Prompts 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>)
|| `Message` | string | Main message,  to display in the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|| [`Optional`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/09 🤔✏️ with Input behavior.md>) | bool | Prompts are [mandatory](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/09 🤔✏️ with Input behavior.md>) by default
|| [`Attachment`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/05 🤔📎 with Attachments.md>)| uuid   | File to download via [`Download@Host`](<06 🧑‍🦰🚀🤗 Download.md>)
|| [`Details`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 🤔⊕ with Details.md>) | string | Extended [details](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/03 🤔⊕ with Details.md>) in Markdown format
|| [`Options`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/04 🤔🔘 with Options.md>) | any   | List of [options](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/04 🤔🔘 with Options.md>): string, string[], object
|| [`Emoji`](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/09 🤔✏️ with Input behavior.md>) | string | Optional emoji for [Input Prompts 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/09 🤔✏️ with Input behavior.md>)
|| `MinLength` | int | Optional minimum length
|| `MaxLength` | int | Optional maximum length
|| `MinValue` | int | Optional minimum value
|| `MaxValue` | int | Optional maximum value
|| `Mask` | string | HTML mask for presentation
|| `Pattern`| string | HTML regular expression for validation
|

<br/>

