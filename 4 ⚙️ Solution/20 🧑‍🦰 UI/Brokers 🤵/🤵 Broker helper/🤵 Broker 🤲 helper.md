🤵 Broker domains
===


1. **What is a Broker domain in NLWeb?**
    
    A [Broker 🤵 domain][Broker]
    * is any [Helper 🤲 domain][Helper] 
    * that helps [Notifier 📣 domains][Notifier] 
    * to orchestrate [Chats 💬][Chat] with [Host 🤗 domains][Host]
    * by parsing [Locators 🔆][Locator]
    * and working as the database of the [Wallet 🧑‍🦰 app][Wallet].

    ---
    <br/>

1. **How do Brokers work?**

    ![](<🤵🏞️ Broker img.png>)

    | # | Category  | Step
    |-|-|-
    |1| `Hi`     | The user initiates an interaction with their [Wallet 🧑‍🦰 app][Wallet] - e.g., by scanning a QR and sending the [QR Locator 🔆][Locator] to the their [Broker 🤵 domain][Broker].
    |2| `Hi-A`   | The [user's Broker 🤵 domain][Broker] opens a new [Chat 💬][Chat] with the [Locator's Host 🤗 domain][Host], obfuscating the user (e.g., ABC).
    |3| `Bye-A`  | The [Host 🤗 domain][Host] runs its workflow for the anonymous user (e.g., ABC), and finishes it with a goodbye [Message 📨][Message].
    |4| `Bye`    | The [user's Broker 🤵 domain][Broker] forwards the [Messages 📨][Message] to the [user's Notifier 📣 domain][Notifier], to be pushed to the [Wallet 🧑‍🦰 app][Wallet].
    |A| `Hi`     | The user initiates a second interaction with the same [Host 🤗 domain][Host].
    |B| `Hi-X`   | The [user's Broker 🤵 domain][Broker] opens a new [Chat 💬][Chat] with the same [Host 🤗 domain][Host], obfuscating again the user (e.g., XYZ).
    |C| `Bye-X` | The [Host 🤗 domain][Host] runs its workflow for the new anonymous user (e.g., XYZ), without realizing that it's the same user as before.
    |D| `Bye`   | The [user's Broker 🤵 domain][Broker] forwards the [Messages 📨][Message] again.

    ---
    <br/>

1. **How do Brokers protect users from Hosts?**
 
    [Broker 🤵 domains][Broker] give users the right to be forgotten by defaulting to anonymous browsing; 
    * i.e., whenever a user returns to a [Host 🤗 domain][Host], the [Broker 🤵 domain][Broker] connects them using a different untraceable ID. 
    
    * For a [Host 🤗 domain][Host] to identity a user across sessions, the user needs to explicitly accept a [Bind 🔗][Bind] from the [Host's Vault 🗄️ role][Vault] or a [Token 🎫][Token] from the [Host's Issuer 🎴 role][Issuer].

    ---
    <br/>

1. **Who migrates users between phones - Brokers or Notifiers?**

    Given that [Wallet 🧑‍🦰 apps][Wallet] and [Notifier 📣 domains][Notifier] contain only minimum-to-no data, the migration of a user between and old and a new phone needs to be done by [Broker 🤵 domains][Broker].

    ---
    <br/>


1. **Why aren't Brokers and Notifiers the same domain?**
    
    Separating the responsibilities of [Broker 🤵 domains][Broker] and [Notifier 📣 domains][Notifier] allows cloud providers (e.g., AWS, Azure, GCP) and independent software vendors (ISVs) to offload from mobile startups the undifferentiated heavy lifting of implementing the NLWeb protocol in the most robust, secure, and compliant way. 
    
    * These startups can then focus on the [Wallet 🧑‍🦰 app][Wallet] and [Notifier 📣 domain][Notifier] to create great frontend user experiences.

    * [Broker 🤵 domains][Broker] are responsible for validating if the [Notifier 📣 domains][Notifier] they serve are compliant with NLWeb protocol, blocking them if necessary.

    * The NLWeb organization is responsible for verifying and onboarding [Broker 🤵 domains][Broker], listing them as [trustworthy 🫡][Trust] on its public [domain Manifest 📜][Manifest], so that other [domains 👥][Domain] can inherit that [trust 🫡][Trust].

    ---
    <br/>

1. **How can Wallet startups connect to a Broker?**

    For startups and others to build a [Wallet 🧑‍🦰 app][Wallet], they need to:
    - Build a [Notifier 📣 domain][Notifier] and register it on a [Broker 🤵 domain][Broker];
    - Build a [Wallet 🧑‍🦰 app][Wallet] and pass the acceptance tests of the [Broker 🤵 domain][Broker];
    - Release the [Wallet 🧑‍🦰 app][Wallet] to onboard users into the [Broker 🤵 domain][Broker].

    ---
    <br/>

1. **How do Brokers ensure Wallets are NLWeb compliant?**

    [Broker 🤵 domains][Broker] are responsible for testing the compliance of [Wallet 🧑‍🦰 apps][Wallet] and [Notifier 📣 domains][Notifier] by performing a set of automated tests before allowing new Wallet versions to be used.

    * [Notifier 📣 domains][Notifier] are responsible for informing [Broker 🤵 domains][Broker] about changes in the software version, allowing [Broker 🤵 domains][Broker] to manage the test and release lifecycle of new versions 
    * Failure to inform may force the [Broker 🤵 domain][Broker] to cut the Wallet's communication to NLWeb by blocking its [Notifier 📣 domain][Notifier].

    ---
    <br/>

1. **What API methods does a Broker expose?**

    Group |  Method | Purpose
    |-|-|-
    |[`🧑‍🦰 Setup`][Wallet]| [📣🚀 Onboard](<../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>) | Onboard a [Wallet 🧑‍🦰 app][Wallet]
    |  | [🧑‍🦰🐌 Translate](<../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Language 🧑‍🦰🐌🤵/🤵 Language 🐌 msg.md>) | Change the language of a [Wallet 🧑‍🦰][Wallet]
    | [`💬 Chats`][Chat]  | [🧑‍🦰🚀 Locate](<../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | Parse the [Locator 🔆][Locator] on the [Broker 🤵][Broker]
    | | [🧑‍🦰🚀 Chats](<../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>) | Fetch [Chats 💬][Chat] from the [Broker 🤵][Broker]
    | | [🤗🐌 Prompt](<../🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>) |   [Prompt 🤔][Prompt] intent from [Host 🤗 domain][Host] 
    | |[🔎🐌 Presented](<../🤵🅰️ Broker methods/Chats 💬 Presented 🔎🐌🤵/🤵 Presented 🐌 msg.md>) | A [Finder 🔎 domain](<../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) finished the intro
    | |[🤗🐌 Goodbye](<../🤵🅰️ Broker methods/Chats 💬 Goodbye 🤗🐌🤵/🤵 Goodbye 🐌 msg.md>) | A [Host 🤗 domain][Host] ended the [Chat 💬][Chat]
    | | [👀🐌 Promote](<../🤵🅰️ Broker methods/Locators 🔆 Promote 👀🐌🤵/🤵 Promote 🐌 msg.md>) |  Check-in into the selected [Locator 🔆][Locator]
    | | [🧑‍🦰🐌 Join](<../🤵🅰️ Broker methods/Chats 💬 Join 🧑‍🦰🐌🤵/🤵 Join 🐌 msg.md>) | Ask for the [Broker 🤵][Broker] to join a [Chat 💬][Chat] 
    |[`🔗 Binds`][Bind]|  [🗄️🐌 Bindable](<../🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>) | [Vaults 🗄️][Vault] offer to bind [Schema Codes 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    | [`🎫 Tokens`][Token] |  [🎴🐌 Offer](<../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [Issuers 🎴][Issuer] offer an issued [Token 🎫][Token] 
    || [🧑‍🦰🐌 Saved][Saved@Broker] | A [Wallet 🧑‍🦰][Wallet] saved a [Token 🎫][Token] locally
    || [🎴🐌 Revise][Revise@Broker] | Update the status of a [Token 🎫][Token]
    | [`💼 Share`](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | [💼🐌 Query](<../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | Return user [Binds 🔗][Bind] and [Tokens 🎫][Token]
    || [💼🚀 Status](<../🤵🅰️ Broker methods/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 call.md>) | Return the status of a [Token 🎫][Token]

    <!--
    |Pay| [💵🐌🤵 Charge](<../🤵🅰️ Broker methods/Payments 💵 Charge 💵🐌🤵/🤵 Charge 🐌 msg.md>)
    -->
    
    ---
    <br/>

[Bind]: <../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>
[Wallet]: <../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>
[Notifier]: <../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>
[Manifest]: <../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>
[Vault]: <../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>
[Token]: <../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>
[Host]: <../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>
[Chat]: <../../../35 💬 Chats/Chats 💬/💬 Chat.md>
[Message]: <../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>
[Broker]: <🤵 Broker 🤲 helper.md>
[Locator]: <../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>
[Helper]: <../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>
[Issuer]: <../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>
[Prompt]: <../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>
[Trust]: <../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>
[Domain]: <../../../40 👥 Domains/👥 Domain/👥 Domain.md>
[Saved@Broker]: <../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>
[Revise@Broker]: <../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>