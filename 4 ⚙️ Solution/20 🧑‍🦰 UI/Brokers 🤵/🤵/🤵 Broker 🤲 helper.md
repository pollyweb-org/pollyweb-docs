🤵 Broker domains
===


1. **What is a Broker domain in PollyWeb?**
    
    A [Broker 🤵 domain](<🤵 Broker 🤲 helper.md>)
    * is any [Helper 🤲 domain](<../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) 
    * that helps [Notifier 📣 domains](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) 
    * to orchestrate [Chats 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)
    * by parsing [Locators 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    * and working as the database of the [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

    ---
    <br/>

1. **How do Brokers work?**

    ![](<🤵🏞️ Broker img.png>)

    | # | Category  | Step
    |-|-|-
    |1| `Hi`     | The user initiates an interaction with their [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) - e.g., by scanning a QR and sending the [QR Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to the their [Broker 🤵 domain](<🤵 Broker 🤲 helper.md>).
    |2| `Hi-A`   | The [user's Broker 🤵 domain](<🤵 Broker 🤲 helper.md>) opens a new [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the [Locator's Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>), obfuscating the user (e.g., ABC).
    |3| `Bye-A`  | The [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) runs its workflow for the anonymous user (e.g., ABC), and finishes it with a goodbye [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>).
    |4| `Bye`    | The [user's Broker 🤵 domain](<🤵 Broker 🤲 helper.md>) forwards the [Messages 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) to the [user's Notifier 📣 domain](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>), to be pushed to the [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    |A| `Hi`     | The user initiates a second interaction with the same [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).
    |B| `Hi-X`   | The [user's Broker 🤵 domain](<🤵 Broker 🤲 helper.md>) opens a new [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the same [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>), obfuscating again the user (e.g., XYZ).
    |C| `Bye-X` | The [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) runs its workflow for the new anonymous user (e.g., XYZ), without realizing that it's the same user as before.
    |D| `Bye`   | The [user's Broker 🤵 domain](<🤵 Broker 🤲 helper.md>) forwards the [Messages 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) again.

    ---
    <br/>

1. **How do Brokers protect users from Hosts?**
 
    [Broker 🤵 domains](<🤵 Broker 🤲 helper.md>) give users the right to be forgotten by defaulting to anonymous browsing; 
    * i.e., whenever a user returns to a [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>), the [Broker 🤵 domain](<🤵 Broker 🤲 helper.md>) connects them using a different untraceable ID. 
    
    * For a [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) to identity a user across sessions, the user needs to explicitly accept a [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) from the [Host's Vault 🗄️ role](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) or a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) from the [Host's Issuer 🎴 role](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>).

    ---
    <br/>

1. **Who migrates users between phones - Brokers or Notifiers?**

    Given that [Wallet 🧑‍🦰 apps](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) and [Notifier 📣 domains](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) contain only minimum-to-no data, the migration of a user between and old and a new phone needs to be done by [Broker 🤵 domains](<🤵 Broker 🤲 helper.md>).

    ---
    <br/>


1. **Why aren't Brokers and Notifiers the same domain?**
    
    Separating the responsibilities of [Broker 🤵 domains](<🤵 Broker 🤲 helper.md>) and [Notifier 📣 domains](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) allows cloud providers (e.g., AWS, Azure, GCP) and independent software vendors (ISVs) to offload from mobile startups the undifferentiated heavy lifting of implementing the PollyWeb protocol in the most robust, secure, and compliant way. 
    
    * These startups can then focus on the [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) and [Notifier 📣 domain](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) to create great frontend user experiences.

    * [Broker 🤵 domains](<🤵 Broker 🤲 helper.md>) are responsible for validating if the [Notifier 📣 domains](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) they serve are compliant with PollyWeb protocol, blocking them if necessary.

    * The PollyWeb organization is responsible for verifying and onboarding [Broker 🤵 domains](<🤵 Broker 🤲 helper.md>), listing them as [trustworthy 🫡](<../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) on its public [domain Manifest 📜](<../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>), so that other [domains 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) can inherit that [trust 🫡](<../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>).

    ---
    <br/>

1. **How can Wallet startups connect to a Broker?**

    For startups and others to build a [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>), they need to:
    - Build a [Notifier 📣 domain](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) and register it on a [Broker 🤵 domain](<🤵 Broker 🤲 helper.md>);
    - Build a [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) and pass the acceptance tests of the [Broker 🤵 domain](<🤵 Broker 🤲 helper.md>);
    - Release the [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) to onboard users into the [Broker 🤵 domain](<🤵 Broker 🤲 helper.md>).

    ---
    <br/>

1. **How do Brokers ensure Wallets are PollyWeb compliant?**

    [Broker 🤵 domains](<🤵 Broker 🤲 helper.md>) are responsible for testing the compliance of [Wallet 🧑‍🦰 apps](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) and [Notifier 📣 domains](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) by performing a set of automated tests before allowing new Wallet versions to be used.

    * [Notifier 📣 domains](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>) are responsible for informing [Broker 🤵 domains](<🤵 Broker 🤲 helper.md>) about changes in the software version, allowing [Broker 🤵 domains](<🤵 Broker 🤲 helper.md>) to manage the test and release lifecycle of new versions 
    * Failure to inform may force the [Broker 🤵 domain](<🤵 Broker 🤲 helper.md>) to cut the Wallet's communication to PollyWeb by blocking its [Notifier 📣 domain](<../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>).

    ---
    <br/>

1. **What API methods does a Broker expose?**

    Group |  Method | Purpose
    |-|-|-
    |[`🧑‍🦰 Wallet`](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)| [📣🚀 Onboard](<../🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 call.md>) | Onboard a [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | [`💬 Chats`](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)  | [🧑‍🦰🐌 Locate](<../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | Parse the [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) on the [Broker 🤵](<🤵 Broker 🤲 helper.md>)
    | | [🧑‍🦰🚀 Frontend](<../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>) | Fetch [Chats 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) from the [Broker 🤵](<🤵 Broker 🤲 helper.md>)
    | | [🤗🐌 Prompt](<../🤵📨 Broker msgs/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>) |   [Prompt 🤔](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) intent from [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
    | |[🤗🐌 Goodbye](<../🤵📨 Broker msgs/Chats 💬 Goodbye 🤗🐌🤵/🤵 Goodbye 🐌 msg.md>) | A [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) ended the [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
    | | [👀🐌 Promote](<../🤵📨 Broker msgs/Locators 🔆 Promote 👀🐌🤵/🤵 Promote 🐌 msg.md>) |  Check-in into the selected [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
    |[`🔗 Binds`](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)|  [🗄️🐌 Bind](<../🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>) | [Vaults 🗄️](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) offer to bind [Schema Codes 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    | [`🎫 Tokens`](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) |  [🎴🐌 Offer](<../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [Issuers 🎴](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) offer an issued [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) 
    || [🧑‍🦰🐌 Saved](<../🤵📨 Broker msgs/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) | A [Wallet 🧑‍🦰](<../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) saved a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) locally
    || [🎴🐌 Revise](<../🤵📨 Broker msgs/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>) | Update the status of a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    | [`💼 Share`](<../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | [💼🐌 Query](<../🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | Return user [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) and [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    || [💼🚀 Status](<../🤵📨 Broker msgs/Share 💼 Status 💼🚀🤵/🤵 Status 🚀 call.md>) | Return the status of a [Token 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)

    <!--
    |Pay| [💵🐌🤵 Charge](<../🤵📨 Broker msgs/Payments 💵 Charge 💵🐌🤵/🤵 Charge 🐌 msg.md>)
    -->
    
    ---
    <br/>