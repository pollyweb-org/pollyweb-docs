# 😃🤲 Talker `INVITE` command

> Relates to [Invite ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>)

> Used by [Helper 🤲 domain](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲 Helper/🤲👥 Helper domain.md>)

<br/>

1. **What's the syntax for `INVITE`?**

    ```yaml
    INVITE >> $output:
        Invitee: <invitee>
        Schema: <code>
        Parameters: {params}
    ```

    | Input| Purpose 
    |-|-
    | `<invitee>` | The invitee [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) for [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) 
    | `<code>` | The [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) to query for data
    | `{params}` | Parameters dictionary for [`Invite@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) 
    | `$output` | Returned data matching the code's schema
    |