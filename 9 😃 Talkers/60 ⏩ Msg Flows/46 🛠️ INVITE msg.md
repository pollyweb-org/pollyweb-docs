# 🛠️ Talker INVITE command

> Relates to [Invite ⏩ flow](<../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>)

> Used by [Helper 🛠️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)

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
    | `<invitee>` | The invitee [domain 👥](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/00 👥 Domain.md>) for [`Invite@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>) 
    | `<code>` | The [Schema Codes 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) to query for data
    | `{params}` | Parameters dictionary for [`Invite@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>) 
    | `$output` | Returned data matching the code's schema
    |