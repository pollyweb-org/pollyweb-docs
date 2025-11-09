<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDD828d0b17f0fa414ba67fa5eab -->

# 🧑‍🦰🚀🤗 Download @ Host

> Purpose
* Downloads the content of an [Appendix 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>).

> Flow
* Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow.

> Signature 
* signed with the `PrivateKey` from [`Converse@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
* verified with the `PublicKey` from [`Hello@Host`](<../Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)


<br/>

## Sync Request 🚀


```yaml
Header: 
    From: Anonymous
    To: any-host.dom
    Subject: Download@Host

Body:
    Appendix: <appendix-uuid>
```

|Object|Property|Type|Description | Origin
|-|-|-|-|-
| Header    |`From`|domain| `Anonymous`
|           |`To`|domain| [Sender 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) | [`Prompt@`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Prompt 🤵🐌📣/📣 Prompt 🐌 msg.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `Appendix`    | uuid      | [Appendix 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | [`Prompted@`](<../Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>)
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
    | `PDF` | [Show the bill on vending machine payments 🏪](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `PNG` | [Show an image of a recovered item in a taxi 🚕](<../../../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)

    ---
    <br/>