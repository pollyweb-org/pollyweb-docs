# 💼⏩🧑‍🦰 Share an Identity Token @ Consumer

> Mentioned in [🆔 Verify Tokens](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/14 🆔🎫 Verify Tokens.md>)


<br/> 

## Flow diagram

![alt text](<.📎 Assets/⚙️ Share Token+ID.png>)

|#| Step | Purpose
|-|-|-
|1|[💼⏩🧑‍🦰 Share Token 🎫](<04 🧑‍🦰👉💼 Share Token 🎫.md>) | Receive an [Identity-bound Token 🎫](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/14 🆔🎫 Verify Tokens.md>)
|2|[👥🚀🕸 `Trusts@Graph`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>) | Verify if the [Identity 🆔](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) is [Trustworthy 👍](<../../../4 ⚙️ Solution/40 👥 Domains/👥👍 Domain Trusts/👍 Domain Trust.md>) | 
|3|[💼🐌🤵 `Invite@Broker`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>)|Invite the [Identity 🆔](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) to the [Chat 💬](<../../../4 ⚙️ Solution/35 Chats/12 💬 Chats/$ 💬 Chat.md>)
|4| [🤵🐌🛠️ `Invited@Helper`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/$ 🤲 Helpers/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) | Proxy the invite to the [Identity 🆔](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) 
|5|[🆔⏩🧑‍🦰 Take Selfie 📸](<../../55 🆔⏩ Identities/04 🆔⏩🧑‍🦰 Selfie.md>) | Do a [face scan 😶](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/21 🆔😶 Face scan.md>) with liveness check
|6|[🗄️⏩💼 Consume 🧩](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️⏩ Vault flows/🗄️⏩💼 Consume 🔗.md>) | Confirm the [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>) ownership
|

<br/>

## FAQ

1. **Why do we need to get the user's approval?**

    Users expect to have only their own [Vaults 🗄️ domains](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) on the [Chat 💬](<../../../4 ⚙️ Solution/35 Chats/12 💬 Chats/$ 💬 Chat.md>), apart from the [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) and the [Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>).
    * If the [Identity 🆔 vault](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>) referenced by the [Token 🎫](<../../../4 ⚙️ Solution/30 Data/30 🎫 Tokens/🎫 Token.md>) is listed as a user [Bind 🔗](<../../../4 ⚙️ Solution/30 Data/20 🔗 Binds/🔗 Bind.md>), then no approval is required.
    * However, if it is an unknown [Identity 🆔 vault](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>), then the user needs to approve to clearly understand that it's not their bounded [Identity 🆔 agent](<../../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>).
    * The later is the case when a user is trying to interact with a [Userable 💍](<../../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Userables/$ 💍 Userable thing.md>) from another person in the [Confused senior user 👴🏻](<../../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Userables/13 💍📱 Userable senior user.md>) scenario.

    ---
    <br/>

1. **What does the Invite@Broker call look like?**

    Consider the following example payload to  [`Invite@Broker`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>).

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