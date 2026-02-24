# 🧑‍🦰🚀🤗 Download @ Host

> About
* Downloads the content of an [Appendix 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>).
* Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../🤗⏩ Host flows/Prompt 🤗⏩🤔/🤗 Prompt ⏩ flow.md>) flow.

> Signature 
* signed with the `PrivateKey` from [`Open@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
* verified with the `PublicKey` from [`Hello@Host`](<../Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)


<br/>

## Synchronous Call 🚀


```yaml
Header: 
    From: Anonymous
    To: any-host.dom
    Subject: Download@Host

Body:
    Appendix: <appendix-uuid>
    Page: 3         # Optional, only for PDF type
    MaxWidth: 1024  # Optional, only for image types
    MaxHeight: 768  # Optional, only for image types
```

|Object|Property|Type|Description | Origin
|-|-|-|-|-
| Header    |`From`|text| `Anonymous`
|           |`To`|text| [Sender 🤗](<../../🤗 Host role/🤗🎭 Host role.md>) | [`Prompt@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|           | `Subject`     | string    | `Prompted@Host`
| Body      | `Appendix`    | uuid      | [Appendix 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) ID | [`Prompted@`](<../Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>)
|| `Page`        | num       | Specific page only, for `PDF` | 
|| `MaxWidth`   | num       | Max width for images, in pixels |
|| `MaxHeight`  | num       | Max height for images, in pixels |

<br/>


## Sync Response


```yaml
Content: KFJASON...
```

||Property|Type|Description
|-|-|-|-
|| `Content` |text| Bytes serialized to base64

<br/>


## FAQ

1. **What are examples of Download usage?**

    | Format | Example | 
    |-|-
    | `PDF` | [Show the bill on vending machine payments 🏪](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `PNG` | [Show an image of a recovered item in a taxi 🚕](<../../../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)

    ---
    <br/>