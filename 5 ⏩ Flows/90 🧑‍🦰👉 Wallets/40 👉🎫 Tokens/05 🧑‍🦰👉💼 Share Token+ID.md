# 💼⏩🧑‍🦰 Share an Identity Token @ Consumer

> Mentioned in [🆔 Verify Tokens](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/14 🆔🎫 Verify Tokens.md>)


<br/> 

## Flow diagram

![alt text](<.📎 Assets/⚙️ Share Token+ID.png>)

|#| Step | Purpose
|-|-|-
|1|[💼⏩🧑‍🦰 Share Token 🎫](<04 🧑‍🦰👉💼 Share Token.md>) | Receive an [Identity-bound Token 🎫](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/14 🆔🎫 Verify Tokens.md>)
|2|[👥🚀🕸 Trusts @ Graph](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/03 👥🚀🕸 Trusts.md>) | Verify if the [Identity 🆔](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) is [Trustworthy 👍](<../../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) | 
|3|[💼🐌🤵 Invite @ Broker](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)|Invite the [Identity 🆔](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) to the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
|4| [🤵🐌🤗 Invited @ Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/11 🤵🐌🤗 Invited.md>) | Proxy the invite to the [Identity 🆔](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) 
|5|[🆔⏩🧑‍🦰 Take Selfie 📸](<../../55 🆔⏩ Identities/04 🆔⏩🧑‍🦰 Selfie.md>) | Do a [face scan 😶](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>) with liveness check
|6|[🗄️⏩💼 Consume 🧩](<../../80 🗄️⏩ Vaults/02 🗄️⏩💼 Consume.md>) | Confirm the [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ownership
|

<br/>

## FAQ

1. **Why do we need to get the user's approval?**

    Users expect to have only their own [Vaults 🗄️ domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) on the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>), apart from the [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) and the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).
    * If the [Identity 🆔 vault](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) referenced by the [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) is listed as a user [Bind 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>), then no approval is required.
    * However, if it is an unknown [Identity 🆔 vault](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>), then the user needs to approve to clearly understand that it's not their bounded [Identity 🆔 agent](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>).
    * The later is the case when a user is trying to interact with a [Userable 💍](<../../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) from another person in the [Confused senior user 👴🏻](<../../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Brand Userables/13 💍📱 Userable senior user.md>) scenario.

    ---
    <br/>

2. **What does the Invite@Broker call look like?**

    Consider the following example payload to  [`Invite @ Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>).

    ```yaml
    Header:
        From: any-consumer.com
        To: any-broker.com
        Subject: Invite@Broker
    Body:
        ChatID: <chat-uuid>
        Invitee: any-identity.com
        Callback: <callback-uuid>
        Code: nlweb.org/IDENTITY/VERIFY
        Parameters:
            IdentityKey: <token-identity-key>
    ```