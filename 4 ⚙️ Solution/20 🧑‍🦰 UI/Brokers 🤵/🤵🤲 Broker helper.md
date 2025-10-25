🤵 Broker domains
===


1. **What is a Broker domain in NLWeb?**
    
    A [Broker 🤵 domain](<🤵🤲 Broker helper.md>)
    * is any [Helper 🤲 domain](<../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) 
    * that helps [Notifier 📣 domains](<../Notifiers 📣/📣👥 Notifier domain.md>) 
    * to orchestrate [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) with [Host 🤗 domains](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)
    * by parsing [Locators 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    * and working as the database of the [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

    ---
    <br/>

1. **How do Brokers work?**

    ![](<.📎 Assets/🤵 Broker.png>)

    | # | Category  | Step
    |-|-|-
    |1| `Hi`     | The user initiates an interaction with their [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) - e.g., by scanning a QR and sending the [QR Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to the their [Broker 🤵 domain](<🤵🤲 Broker helper.md>).
    |2| `Hi-A`   | The [user's Broker 🤵 domain](<🤵🤲 Broker helper.md>) opens a new [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) with the [Locator's Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>), obfuscating the user (e.g., ABC).
    |3| `Bye-A`  | The [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) runs its workflow for the anonymous user (e.g., ABC), and finishes it with a goodbye [Message 📨](<../../30 🧩 Data/Messages 📨/📨 Message.md>).
    |4| `Bye`    | The [user's Broker 🤵 domain](<🤵🤲 Broker helper.md>) forwards the [Messages 📨](<../../30 🧩 Data/Messages 📨/📨 Message.md>) to the [user's Notifier 📣 domain](<../Notifiers 📣/📣👥 Notifier domain.md>), to be pushed to the [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).
    |A| `Hi`     | The user initiates a second interaction with the same [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>).
    |B| `Hi-X`   | The [user's Broker 🤵 domain](<🤵🤲 Broker helper.md>) opens a new [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) with the same [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>), obfuscating again the user (e.g., XYZ).
    |C| `Bye-X` | The [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) runs its workflow for the new anonymous user (e.g., XYZ), without realizing that it's the same user as before.
    |D| `Bye`   | The [user's Broker 🤵 domain](<🤵🤲 Broker helper.md>) forwards the [Messages 📨](<../../30 🧩 Data/Messages 📨/📨 Message.md>) again.

    ---
    <br/>

1. **How do Brokers protect users from Hosts?**
 
    [Broker 🤵 domains](<🤵🤲 Broker helper.md>) give users the right to be forgotten by defaulting to anonymous browsing; 
    * i.e., whenever a user returns to a [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>), the [Broker 🤵 domain](<🤵🤲 Broker helper.md>) connects them using a different untraceable ID. 
    
    * For a [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) to identity a user across sessions, the user needs to explicitly accept a [Bind 🔗](<../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) from the [Host's Vault 🗄️ role](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) or a [Token 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) from the [Host's Issuer 🎴 role](<../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>).

    ---
    <br/>

1. **Who migrates users between phones - Brokers or Notifiers?**

    Given that [Wallet 🧑‍🦰 apps](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) and [Notifier 📣 domains](<../Notifiers 📣/📣👥 Notifier domain.md>) contain only minimum-to-no data, the migration of a user between and old and a new phone needs to be done by [Broker 🤵 domains](<🤵🤲 Broker helper.md>).

    ---
    <br/>


1. **Why aren't Brokers and Notifiers the same domain?**
    
    Separating the responsibilities of [Broker 🤵 domains](<🤵🤲 Broker helper.md>) and [Notifier 📣 domains](<../Notifiers 📣/📣👥 Notifier domain.md>) allows cloud providers (e.g., AWS, Azure, GCP) and independent software vendors (ISVs) to offload from mobile startups the undifferentiated heavy lifting of implementing the NLWeb protocol in the most robust, secure, and compliant way. 
    
    * These startups can then focus on the [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) and [Notifier 📣 domain](<../Notifiers 📣/📣👥 Notifier domain.md>) to create great frontend user experiences.

    * [Broker 🤵 domains](<🤵🤲 Broker helper.md>) are responsible for validating if the [Notifier 📣 domains](<../Notifiers 📣/📣👥 Notifier domain.md>) they serve are compliant with NLWeb protocol, blocking them if necessary.

    * The NLWeb organization is responsible for verifying and onboarding [Broker 🤵 domains](<🤵🤲 Broker helper.md>), listing them as [trustworthy 🫡](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) on its public [domain Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest.md>), so that other [domains 👥](<../../40 👥 Domains/👥 Domain.md>) can inherit that [trust 🫡](<../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>).

    ---
    <br/>

1. **How can Wallet startups connect to a Broker?**

    For startups and others to build a [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>), they need to:
    - Build a [Notifier 📣 domain](<../Notifiers 📣/📣👥 Notifier domain.md>) and register it on a [Broker 🤵 domain](<🤵🤲 Broker helper.md>);
    - Build a [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) and pass the acceptance tests of the [Broker 🤵 domain](<🤵🤲 Broker helper.md>);
    - Release the [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) to onboard users into the [Broker 🤵 domain](<🤵🤲 Broker helper.md>).

    ---
    <br/>

1. **How do Brokers ensure Wallets are NLWeb compliant?**

    [Broker 🤵 domains](<🤵🤲 Broker helper.md>) are responsible for testing the compliance of [Wallet 🧑‍🦰 apps](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) and [Notifier 📣 domains](<../Notifiers 📣/📣👥 Notifier domain.md>) by performing a set of automated tests before allowing new Wallet versions to be used.

    * [Notifier 📣 domains](<../Notifiers 📣/📣👥 Notifier domain.md>) are responsible for informing [Broker 🤵 domains](<🤵🤲 Broker helper.md>) about changes in the software version, allowing [Broker 🤵 domains](<🤵🤲 Broker helper.md>) to manage the test and release lifecycle of new versions 
    * Failure to inform may force the [Broker 🤵 domain](<🤵🤲 Broker helper.md>) to cut the Wallet's communication to NLWeb by blocking its [Notifier 📣 domain](<../Notifiers 📣/📣👥 Notifier domain.md>).

    ---
    <br/>

1. **What API methods does a Broker expose?**

    Group |  Method | Purpose
    |-|-|-
    |[`🧑‍🦰 Setup`](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)| [📣🚀 Onboard](<🤵🅰️ Broker methods/...for Wallets 🧑‍🦰/Onboard/📣🚀🤵 Onboard.md>) | Onboard a [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    |  | [🧑‍🦰🐌 Translate](<🤵🅰️ Broker methods/...for Wallets 🧑‍🦰/Language/🧑‍🦰🐌🤵 Language.md>) | Change the language of a [Wallet 🧑‍🦰](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | [`💬 Chats`](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)  | [🧑‍🦰🚀 Assess](<🤵🅰️ Broker methods/...for Locators 🔆/Assess/🧑‍🦰🐌🤵 Assess.md>) | Parse the [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) on the [Broker 🤵](<🤵🤲 Broker helper.md>)
    | | [🧑‍🦰🚀 Chats](<🤵🅰️ Broker methods/...for Chats 💬/Chats 🧑‍🦰🚀🤵/Chats 🚀 request.md>) | Fetch [Chats 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) from the [Broker 🤵](<🤵🤲 Broker helper.md>)
    | | [🤗🐌 Prompt](<🤵🅰️ Broker methods/...for Chats 💬/Prompt 🤗🐌🤵/🤗🐌🤵 Prompt.md>) |   [Prompt 🤔](<../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) intent from [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
    | |[🔎🐌 Introduced](<🤵🅰️ Broker methods/...for Chats 💬/Introduced 🔎🐌🤵/Introduced 🐌 msg.md>) | A [Finder 🔎 domain](<../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) finished the intro
    | |[🤗🐌 Goodbye](<🤵🅰️ Broker methods/...for Chats 💬/Goodbye 🤗🐌🤵/Goodbye 🐌 msg.md>) | A [Host 🤗 domain](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) ended the [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>)
    | | [👀🐌 Promote](<🤵🅰️ Broker methods/...for Locators 🔆/Promote/👀🐌🤵 Promote.md>) |  Check-in into the selected [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    | | [🧑‍🦰🐌 Join](<🤵🅰️ Broker methods/...for Chats 💬/Join 🧑‍🦰🐌🤵/Join 🐌 msg.md>) | Ask for the [Broker 🤵](<🤵🤲 Broker helper.md>) to join a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
    |[`🔗 Binds`](<../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)| [🧑‍🦰🚀 Binds](<🤵🅰️ Broker methods/...for Binds 🔗/Binds 🧑‍🦰🚀🤵/Binds 🚀 request.md>) | List the [Binds 🔗](<../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) of a [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    || [🗄️🐌 Bindable](<🤵🅰️ Broker methods/...for Binds 🔗/Bindable 🗄️🐌🤵/🗄️🐌🤵 Bindable.md>) | [Vaults 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) offer to bind [Schema Codes 🧩](<../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    | [`🎫 Tokens`](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) | [🧑‍🦰🚀 Tokens](<🤵🅰️ Broker methods/...for Tokens 🎫/Tokens/🧑‍🦰🚀🤵 Tokens.md>) | List of [Tokens 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) of a [Wallet 🧑‍🦰 app](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    || [🎴🐌 Offer](<🤵🅰️ Broker methods/...for Tokens 🎫/Offer 🎴🐌🤵/Offer 🐌 msg.md>) | [Issuers 🎴](<../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) offer an issued [Token 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) 
    || [🧑‍🦰🐌 Saved](<🤵🅰️ Broker methods/...for Tokens 🎫/Saved 🧑‍🦰🐌🤵/🧑‍🦰🐌🤵 Saved.md>) | A [Wallet 🧑‍🦰](<../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) saved a [Token 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) locally
    || [🎴🐌 Revise](<🤵🅰️ Broker methods/...for Tokens 🎫/Revise 🐌/🎴🐌🤵 Revise.md>) | Update the status of a [Token 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
    | [`💼 Share`](<../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | [💼🐌 Query](<🤵🅰️ Broker methods/...for Share 💼/Query/💼🐌🤵 Query.md>) | Return user [Binds 🔗](<../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) and [Tokens 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)
    || [💼🚀 Status](<🤵🅰️ Broker methods/...for Share 💼/Status/💼🚀🤵 Status.md>) | Return the status of a [Token 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)

    <!--
    |Pay| [💵🐌🤵 Charge](<🤵🅰️ Broker methods/...for Pay/💵🐌🤵 Charge.md>)
    -->
    
    ---
    <br/>