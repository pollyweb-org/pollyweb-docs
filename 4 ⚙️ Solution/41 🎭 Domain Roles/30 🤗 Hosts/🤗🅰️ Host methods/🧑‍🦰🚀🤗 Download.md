<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDD828d0b17f0fa414ba67fa5eab -->

# 🧑‍🦰🚀🤗 Download @ Host


> Downloads the content of an [Appendix 📎](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/5 📎 with Appendix.md>).


> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow.

> Signature of the [Message 📨](<../../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>):
> <br>• signed with the `PrivateKey` from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
> <br>• verified with the `PublicKey` from [`Hello@Host`](<🤵🐌🤗 Hello.md>)


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
|           | `To`          | string    | [Sender 🤗](<../🤗🎭 Host role.md>) from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `ChatID` | uuid | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Prompt@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/2 💬 Chats/2 🤵🐌📣 Prompt.md>)
|| `FileID`    | uuid      | [Appendix 📎](<../../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/5 📎 with Appendix.md>) from [`Prompted@Host`](<🧑‍🦰🚀🤗 Prompted.md>)
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
    | `PDF` | [Show the bill on vending machine payments 🏪](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `PNG` | [Show an image of a recovered item in a taxi 🚕](<../../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)

    ---
    <br/>