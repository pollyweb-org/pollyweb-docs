🤗 Host domain role
===

1. **What is a Host domain role in NLWeb?**

    A [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) with a [Host 🤗 domain role](<🤗🎭 Host role.md>) is any [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) that
    * hosts a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) with [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) 
    * via a [Broker 🤵 domain](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>). 

    ---
    <br/>

1. **How do Host domains work?**

    ![](<../../35 💬 Chats/💬 Chats/.📎 Assets/💬🤗 Host.png>)

    |#|Category|Step
    |-|-|-
    |1| `Hello`| The [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) checks-in into a [Host 🤗 domain](<🤗🎭 Host role.md>), passing it context parameters, [Binds 🔗](<../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>), and [Tokens 🎫](<../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>).
    |2| `Chat` | The [Host 🤗 domain](<🤗🎭 Host role.md>) sets a new [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) context.
    |3| `Interact` | The [Host 🤗 domain](<🤗🎭 Host role.md>) starts interacting with prompts.

    ---
    <br/>



1. **How are users protected from stalking from Hosts?**

    NLWeb sees [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) as temporary sessions, always initiated by users; 
    - i.e., the [Host 🤗 domain](<🤗🎭 Host role.md>) receives a temporary ID from the [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) when the [Chat 💬 session](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)  is open, but no other ID to track the user across sessions;
    - although [Host 🤗 domains](<🤗🎭 Host role.md>) can proactively send messages on an open [Chat 💬 session](<../../35 💬 Chats/💬 Chats/💬 Chat.md>), users can close the session at any time. 

    ---
    <br/>

1. **What incentives do Hosts have to close sessions?**

    [Advertising 👀](<../../../2 🏔️ Landscape/1 💼 Business landscape/04 👀 Advertising landscape/00 👀 Advertising index.md>) is triggered at the end of a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) for next-best actions.
    - Thus, [Host 🤗 domains](<🤗🎭 Host role.md>) willing to monetize via cross-domain advertising are incentivized to close [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>). 
    - See the [Advertiser 👀 helper domains](<../../45 🤲 Helper domains/12 👀 Advertisers/👀🤲 Advertiser helper.md>) for details.

    ---
    <br/>

1. **Do Hosts send messages to users via web sockets?**

    No. 
    - [Host 🤗 domains](<🤗🎭 Host role.md>) send [Messages 📨](<../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) via HTTPS POST to a proxy [Broker 🤵 domain](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) that then communicate with the user's [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) with real-time protocols (e.g., web sockets, MQTT). 

    ---
    <br/>

1. **What proxy services are involved in the flow?**

    [Messages 📨](<../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) sent from [Host 🤗 domains](<🤗🎭 Host role.md>) first reach the user's [Broker 🤵 domain](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) via HTTPS POST:
    - these [Broker 🤵 domains](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) are responsible for orchestrating [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) between users and [Host 🤗 domains](<🤗🎭 Host role.md>) using the NLWeb protocol, 
    - and they are typically implemented by a main cloud provider that is able to ensure high availability and low latency communication between globally dispersed entities. 
    
    The [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) then sends the message to a [user's Notifier 📣 domain](<../../20 🧑‍🦰 UI/2 📣 Notifiers/📣👥 Notifier domain.md>), also via HTTPS POST:
    - the [user's Notifier 📣 domain](<../../20 🧑‍🦰 UI/2 📣 Notifiers/📣👥 Notifier domain.md>) is responsible for pushing the message to the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) via whatever real-time mechanisms the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) supports (e.g., web sockets, MQTT);
    - because of this technical dependency, a [Notifier 📣 domain](<../../20 🧑‍🦰 UI/2 📣 Notifiers/📣👥 Notifier domain.md>) is typically implemented by the same team that implemented the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).

    ---
    <br/>


1. **Are chat prompt messages encrypted from Hosts to Wallets?**

    Not applicable - [Host 🤗 domains](<🤗🎭 Host role.md>) don't send [Messages 📨](<../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) to [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>). 

    * [Host 🤗 domains](<🤗🎭 Host role.md>) only send asynchronous HTTPS intents to the [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>), who then sends it to the [user's Notifier 📣 domain](<../../20 🧑‍🦰 UI/2 📣 Notifiers/📣👥 Notifier domain.md>) also via asynchronous HTTPS. 

    * When the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) app receives the intent from the [Notifier 📣 domain](<../../20 🧑‍🦰 UI/2 📣 Notifiers/📣👥 Notifier domain.md>), it pulls the [Message 📨](<../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) content directly from the [Host 🤗 domain](<🤗🎭 Host role.md>) with a synchronous HTTPS call. 

    * This keeps the [Broker 🤵 domain](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) and the [Notifier 📣 domain](<../../20 🧑‍🦰 UI/2 📣 Notifiers/📣👥 Notifier domain.md>) in the dark regarding the content of the [Message 📨](<../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) (even in the event of a cryptography attack) because no content actually passes by these proxy services.

    ---
    <br/>

1. **Are chat reply messages encrypted from Wallets to Hosts?**

    Yes. 

    - Although the user's [Messages 📨](<../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) content is JSON not encrypted, it is sent over HTTPS POST directly from the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to the [Host 🤗 domain](<🤗🎭 Host role.md>).

    - The HTTPS channel ensures the message is encrypted between the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) and the [Host 🤗 domain](<🤗🎭 Host role.md>) . 

    - Unencrypted JSON requests sent over HTTPS are a standard practice in the service APIs of the major cloud providers (e.g., AWS, GCP), and are widely viewed as secure.

    - NLWeb relies on the HTTPS ability to continue to evolve has [post-quantum 📺](<../../../2 🏔️ Landscape/2 🧑‍🦰 User landscape/08 🔐 Passwordless ID landscape/10 📺 Post-quantum keys.md>) cryptography attacks become more sophisticated.

    ---
    <br/>



1. **What flows are initiated by Host domains?**

    | Flow ⏩ | Description
    |-|-
    | [🤔 `Prompt`](<🤗⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) | Sends a [Prompt 🤔](<../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) to a user [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    | [🛠️ `Invite`](<🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🤲.md>) | Invites a [Helper 🤲 domain](<../../45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>) to a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    | [📝 `Form`](<../27 💼 Consumers/💼⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>) | Informs a user on upcoming [Inputs ✏️](<../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/9 ✏️ as Input.md>)
    | [❄️ `Freeze`](<🤗⏩ Host flows/🤗⏩🧑‍🦰 Freeze ❄️.md>) | Blocks changes on all previous [Inputs ✏️](<../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/9 ✏️ as Input.md>)
    | [👋 `Goodbye`](<🤗⏩ Host flows/🤗⏩🧑‍🦰 Goodbye 👋.md>) | Triggers the [advertising 👀](<../../45 🤲 Helper domains/12 👀 Advertisers/👀🤲 Advertiser helper.md>) flow
    

    ---
    <br/>

1. **What API methods are exposed by a Host domain?**

    | [From 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Subject 📨](<../../40 👥 Domains/👥📨 Domain Messages/📨 Message.md>) | Description
    |-|-|-
    |[🤵 Broker](<../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | [`Hello`](<🤗🅰️ Host methods/🤵🐌🤗 Hello.md>) | The user started a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    | | [`Home`](<🤗🅰️ Host methods/🤵🐌🤗 Home.md>) | Show the top menu on the [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    | | [`Abandoned`](<🤗🅰️ Host methods/🤵🐌🤗 Abandoned.md>) |  The user abandoned a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    | | [`Summarize`](<🤗🅰️ Host methods/🤵🐌🤗 Summarize.md>) | Return a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) advertising summary
    |[🧑‍🦰 Wallet](<../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) | [`Prompted`](<🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>) | Return a [Prompt's 🤔](<../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) content
    | | [`Reply`](<🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>) | Accept the reply to a [Prompt 🤔](<../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>)
    | | [`Download`](<🤗🅰️ Host methods/🧑‍🦰🚀🤗 Download.md>) | Download an [Appendix 📎](<../../35 💬 Chats/🤔 Prompts/🤔⚙️ Prompt features/5 📎 with Appendix.md>)
    [🖐️ Palmist](<../../60 🧰 Edge/63 🖐️ Palmists/01 🖐️🔌 Palmist device.md>) | [`Found`](<🤗🅰️ Host methods/🖐️🐌🤗 Found.md>) | A [Palmist 🖐️](<../../60 🧰 Edge/63 🖐️ Palmists/01 🖐️🔌 Palmist device.md>) found the Chat's user
    [⭐ Reviewer](<../../50 🫥 Agent domains/73 ⭐ Reviewers/⭐🫥 Reviewer agent.md>) | [`Rated`](<🤗🅰️ Host methods/⭐🐌🤗 Rated.md>) | The [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) received user reviews
    

    ---
    <br/>
