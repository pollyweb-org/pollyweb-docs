# 😃💬 Talker `CHAT` Command

> Implemented by the [`.CHAT script`](<💬 CHAT 📃 script.md>)

## FAQ

1. **What's the CHAT command for?**

    The `CHAT` command
    * sets the [`$.Chat` 🧠 holder](<../../../📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) holder
    * with a new or existing [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    * to provide language and format context for [Prompts 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>).

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    CHAT:
        Broker: <broker-name>
        Chat: <chat-uuid>
    ```

    Input|Purpose
    |-|-
    |`Broker`| [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) name
    |`Chat`| [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID

    ---
    <br/>

<!--
1. **When is the CHAT command used?**

    [Role 🎭](<../../../../40 👥 Domains/👥 Domain/👥🎭 Domain Role.md>) | 
    |-|-
    |[Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 
    |[Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Helper@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
    |[Helper 🤲 domain](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | [`Invited@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
    
    ---
    <br/>
-->