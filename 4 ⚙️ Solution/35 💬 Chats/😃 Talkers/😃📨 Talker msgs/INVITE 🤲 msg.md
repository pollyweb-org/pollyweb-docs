# 🤲 Talker INVITE command

> Relates to [Invite ⏩ flow](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🤲.md>)

> Used by [Helper 🤲 domain](<../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>)

<br/>

1. **What's the syntax for `INVITE`?**

    ```yaml
    INVITE >> $output:
        Invitee: <invitee>
        Code: <code>
        Parameters: {params}
    ```

    | Argument| Purpose 
    |-|-
    | `<invitee>` | The invitee [domain 👥](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) for [`Invite@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>) 
    | `<code>` | The [Schema Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) to query for data
    | `{params}` | Parameters dictionary for [`Invite@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>) 
    | `$output` | Returned data matching the code's schema
    |