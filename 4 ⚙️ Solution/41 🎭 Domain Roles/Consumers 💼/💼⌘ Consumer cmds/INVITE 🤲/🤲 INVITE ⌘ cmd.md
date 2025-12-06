# 😃🤲 Talker `INVITE` command

> About
* Relates to [Invite ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>)
* Used by [Helper 🤲 domain](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲 Helper/🤲👥 Helper domain.md>)

## FAQ

1. **What's the syntax for `INVITE`?**

    ```yaml
    INVITE >> $output:
        # CHAT must be set
        Helper: <helper>
        Schema: <code>
        Context: {params}
    ```

    | Input| Purpose 
    |-|-
    | `Helper` | The invitee [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) for [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) 
    | `Schema` | The [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to query for data
    | `Context` | Input [map](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) for [`Invited@Consumer`](<../../💼📨 Consumer msgs/Invited 🤲🚀💼/💼 Invited 🚀 call.md>) 
    | `$output` | Returned data matching the code's schema
    |