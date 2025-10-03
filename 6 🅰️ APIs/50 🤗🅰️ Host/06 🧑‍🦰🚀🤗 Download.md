<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDD828d0b17f0fa414ba67fa5eab -->

# 🧑‍🦰🚀🤗 Download @ Host


> Downloads the content of a [Prompt 🤔](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/01 🤔 Prompt.md>) attachment.


> Part of the [🤗⏩🧑‍🦰 Prompt @ Host](<../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>) flow.


<br/>

## Sync Request 🚀


```yaml
Header: 
    From: Anonymous
    To: any-host.com
    Subject: Download@Host

Body:
    ChatID: <prompt-uuid>
    FileID: <file-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | `Anonymous`
|           | `To`          | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `ChatID` | uuid | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
|| `FileID`    | uuid      | Attachment from [Prompted @ Host](<04 🧑‍🦰🚀🤗 Prompted.md>)
|

<br/>


## Sync Response


```yaml
Name: menu.pdf
Format: PDF
Content: KFJASON...
```

|Object |Property|Type|Description
|-|-|-|-
|Top| `Name`  | string | Name of the file, for saving
|| `Format` | enum | `PDF` `PNG` `JPEG`
|| `Content` | string | Bytes serialized to base64
|

<br/>


## FAQ

1. **What are examples of Download usage?**

    | Format | Example | 
    |-|-
    | `PDF` | [Show the bill on vending machine payments 🏪](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `PNG` | [Show an image of a recovered item in a taxi 🚕](<../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)

    ---
    <br/>