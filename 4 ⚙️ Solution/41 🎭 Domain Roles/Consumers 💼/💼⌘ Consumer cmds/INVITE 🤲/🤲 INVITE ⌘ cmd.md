# 😃🤲 Talker `INVITE` command

> About
* Part of the [Invite ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>)
* Used by [Helper 🤲 domains](<../../../Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>)
* Implemented by the [`INVITE` 📃 script](<🤲 INVITE 📃 script.md>)

## FAQ

1. **What's the syntax for `INVITE`?**

    ```yaml
    INVITE >> $output:
        Broker: <broker>   # Defaults to $.Chat.Broker
        Chat: <chat-uuid>  # Defaults to $.Chat.ID
        Helper: <helper>
        Schema: <code>
        Context: {params}
    ```

    | Input| Purpose 
    |-|-
    | `Broker` | The [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) name, defaults to [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)`.Broker`
    | `Chat` | The [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID, defaults to [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)`.ID`
    | `Helper` | The invitee [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) for [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) 
    | `Schema` | The [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to query for data
    | `Context` | Input [map](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) for [`Invited@Consumer`](<../../💼📨 Consumer msgs/Invited 🤲🚀💼/💼 Invited 🚀 call.md>) 
    | `$output` | Returned data matching the code's schema
    |