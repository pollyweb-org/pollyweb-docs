# 💼⏩🧑‍🦰 Share an Identity Token @ Consumer

> Mentioned in [🆔 Verify Tokens](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/3 🆔⏩🎫 Verify Tokens.md>)


<br/> 

## Flow diagram

![alt text](<🧑‍🦰 Share Token+ID ⚙️ uml.png>)

|#| Step | Purpose
|-|-|-
|1|[💼⏩🧑‍🦰 Share Token 🎫](<../Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>) | Receive an [Identity-bound Token 🎫](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/3 🆔⏩🎫 Verify Tokens.md>)
|2|[👥🚀🕸 `Trusts@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>) | Verify if the [Identity 🆔](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) is [Trustworthy 🫡](<../../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) | 
|3|[💼🐌🤵 `Invite@Broker`](<../../../../Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)|Invite the [Identity 🆔](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) to the [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|4| [🤵🐌🛠️ `Help@Helper`](<../../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>) | Proxy the invite to the [Identity 🆔](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) 
|5|[🆔⏩🧑‍🦰 Take Selfie 📸](<../../../../../../5 ⏩ Flows/55 🆔⏩ Identities/04 🆔⏩🧑‍🦰 Selfie.md>) | Do a [face scan 😶](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/6 🆔⏩😶 Face scan.md>) with liveness check
|6|[🗄️⏩💼 Consume 🧩](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⏩ Vault flows/Consume 🗄️⏩💼/🗄️ Consume ⏩ flow.md>) | Confirm the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ownership
|

<br/>

## FAQ

1. **Why do we need to get the user's approval?**

    Users expect to have only their own [Vaults 🗄️ domains](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) on the [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>), apart from the [Host 🤗 domain](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) and the [Broker 🤵 domain](<../../../../Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>).
    * If the [Identity 🆔 vault](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) referenced by the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) is listed as a user [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>), then no approval is required.
    * However, if it is an unknown [Identity 🆔 vault](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>), then the user needs to approve to clearly understand that it's not their bounded [Identity 🆔 agent](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>).
    * The later is the case when a user is trying to interact with a [Userable 💍](<../../../../../25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>) from another person in the [Confused senior user 👴🏻](<../../../../../25 🔆 Locators/Userables 💍/💍⏩ Userable flows/💍📱 Senior user.md>) scenario.

    ---
    <br/>

1. **What does the Invite@Broker call look like?**

    Consider the following example payload to  [`Invite@Broker`](<../../../../Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>).

    ```yaml
    Header:
        From: any-consumer.dom
        To: any-broker.dom
        Subject: Invite@Broker

    Body:
        Chat: <chat-uuid>
        Invitee: any-identity.dom
        Callback: <callback-uuid>
        Schema: nlweb.dom/IDENTITY/VERIFY
        Parameters:
            IdentityKey: <token-identity-key>
    ```