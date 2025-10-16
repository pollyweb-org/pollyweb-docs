# 🛠️ Talker INVITE command

> Relates to [Invite ⏩ flow](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🛠️.md>)

> Used by [Helper 🛠️ domain](<../../4 ⚙️ Solution/45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>)

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
    | `<invitee>` | The invitee [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/👥 Domain.md>) for [`Invite@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>) 
    | `<code>` | The [Schema Codes 🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) to query for data
    | `{params}` | Parameters dictionary for [`Invite@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>) 
    | `$output` | Returned data matching the code's schema
    |