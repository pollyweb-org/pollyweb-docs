🤵 Broker domains
===


1. **What is a Broker domain in NLWeb?**
    
    A [Broker 🤵 domain](<$ 🤵 Broker domain.md>)
    * is any [Helper 🛠️ domain](<../$ 🛠️ Helpers/🛠️👥 Helper domain.md>) 
    * that helps [Notifier 📣 domains](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) 
    * to orchestrate [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>)
    * by parsing [Locators 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
    * and working as the database of the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).

    ---
    <br/>

1. **How do Brokers work?**

    ![](<.📎 Assets/🤵 Broker.png>)

    | # | Category  | Step
    |-|-|-
    |1| `Hi`     | The user initiates an interaction with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) - e.g., by scanning a QR and sending the [QR Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) to the their [Broker 🤵 domain](<$ 🤵 Broker domain.md>).
    |2| `Hi-A`   | The [user's Broker 🤵 domain](<$ 🤵 Broker domain.md>) opens a new [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with the [Locator's Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>), obfuscating the user (e.g., ABC).
    |3| `Bye-A`  | The [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) runs its workflow for the anonymous user (e.g., ABC), and finishes it with a goodbye [Message 📨](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>).
    |4| `Bye`    | The [user's Broker 🤵 domain](<$ 🤵 Broker domain.md>) forwards the [Messages 📨](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) to the [user's Notifier 📣 domain](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>), to be pushed to the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).
    |A| `Hi`     | The user initiates a second interaction with the same [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>).
    |B| `Hi-X`   | The [user's Broker 🤵 domain](<$ 🤵 Broker domain.md>) opens a new [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with the same [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>), obfuscating again the user (e.g., XYZ).
    |C| `Bye-X` | The [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) runs its workflow for the new anonymous user (e.g., XYZ), without realizing that it's the same user as before.
    |D| `Bye`   | The [user's Broker 🤵 domain](<$ 🤵 Broker domain.md>) forwards the [Messages 📨](<../../40 👥 Domains/41 📨 Messages/$ 📨 Domain Message.md>) again.

    ---
    <br/>

1. **How do Brokers protect users from Hosts?**
 
    [Broker 🤵 domains](<$ 🤵 Broker domain.md>) give users the right to be forgotten by defaulting to anonymous browsing; 
    * i.e., whenever a user returns to a [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>), the [Broker 🤵 domain](<$ 🤵 Broker domain.md>) connects them using a different untraceable ID. 
    
    * For a [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) to identity a user across sessions, the user needs to explicitly accept a [Bind 🔗](<../../30 🧩 Data/20 🔗 Binds/🔗 Bind.md>) from the [Host's Vault 🗄️ role](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) or a [Token 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) from the [Host's Issuer 🎴 role](<../../41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>).

    ---
    <br/>

1. **Who migrates users between phones - Brokers or Notifiers?**

    Given that [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) and [Notifier 📣 domains](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) contain only minimum-to-no data, the migration of a user between and old and a new phone needs to be done by [Broker 🤵 domains](<$ 🤵 Broker domain.md>).

    ---
    <br/>


1. **Why aren't Brokers and Notifiers the same domain?**
    
    Separating the responsibilities of [Broker 🤵 domains](<$ 🤵 Broker domain.md>) and [Notifier 📣 domains](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) allows cloud providers (e.g., AWS, Azure, GCP) and independent software vendors (ISVs) to offload from mobile startups the undifferentiated heavy lifting of implementing the NLWeb protocol in the most robust, secure, and compliant way. 
    
    * These startups can then focus on the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) and [Notifier 📣 domain](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) to create great frontend user experiences.

    * [Broker 🤵 domains](<$ 🤵 Broker domain.md>) are responsible for validating if the [Notifier 📣 domains](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) they serve are compliant with NLWeb protocol, blocking them if necessary.

    * The NLWeb organization is responsible for verifying and onboarding [Broker 🤵 domains](<$ 🤵 Broker domain.md>), listing them as [trustworthy 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) on its public [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>), so that other [domains 👥](<../../40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) can inherit that [trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>).

    ---
    <br/>

1. **How can Wallet startups connect to a Broker?**

    For startups and others to build a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>), they need to:
    - Build a [Notifier 📣 domain](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) and register it on a [Broker 🤵 domain](<$ 🤵 Broker domain.md>);
    - Build a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) and pass the acceptance tests of the [Broker 🤵 domain](<$ 🤵 Broker domain.md>);
    - Release the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) to onboard users into the [Broker 🤵 domain](<$ 🤵 Broker domain.md>).

    ---
    <br/>

1. **How do Brokers ensure Wallets are NLWeb compliant?**

    [Broker 🤵 domains](<$ 🤵 Broker domain.md>) are responsible for testing the compliance of [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) and [Notifier 📣 domains](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) by performing a set of automated tests before allowing new Wallet versions to be used.

    * [Notifier 📣 domains](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>) are responsible for informing [Broker 🤵 domains](<$ 🤵 Broker domain.md>) about changes in the software version, allowing [Broker 🤵 domains](<$ 🤵 Broker domain.md>) to manage the test and release lifecycle of new versions 
    * Failure to inform may force the [Broker 🤵 domain](<$ 🤵 Broker domain.md>) to cut the Wallet's communication to NLWeb by blocking its [Notifier 📣 domain](<../../20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>).

    ---
    <br/>

1. **What API methods does a Broker expose?**

    Group |  Method | Purpose
    |-|-|-
    |[`🧑‍🦰 Setup`](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)| [📣🚀 Onboard](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/11 📣🚀🤵 Onboard.md>) | Onboard a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    |  | [🧑‍🦰🐌 Translate](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/10 🤵🅰️ Wallets 🧑‍🦰/12 🧑‍🦰🐌🤵 Translate.md>) | Change the language of a [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | [`💬 Chats`](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)  | [🧑‍🦰🚀 Assess](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/20 🤵🅰️ Locators/01 🧑‍🦰🐌🤵 Assess.md>) | Parse the [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) on the [Broker 🤵](<$ 🤵 Broker domain.md>)
    | | [🧑‍🦰🚀 Chats](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/02 🧑‍🦰🚀🤵 Chats.md>) | Fetch [Chats 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) from the [Broker 🤵](<$ 🤵 Broker domain.md>)
    | | [🤗🐌 Prompt](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/03 🤗🐌🤵 Prompt.md>) |   [Prompt 🤔](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) intent from [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) 
    | |[🔎🐌 Introduced](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/04 🔎🐌🤵 Introduced.md>) | A [Finder 🔎 domain](<../../50 🫥 Agents/40 🔎 Finders/🔎🫥 Finder agent.md>) finished the intro
    | |[🤗🐌 Goodbye](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/05 🤗🐌🤵 Goodbye.md>) | A [Host 🤗 domain](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) ended the [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)
    | | [👀🐌 Promote](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/20 🤵🅰️ Locators/06 👀🐌🤵 Promote.md>) |  Check-in into the selected [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>)
    | | [🧑‍🦰🐌 Help](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/07 🧑‍🦰🐌🤵 Help.md>) | Ask for the [Broker 🤵](<$ 🤵 Broker domain.md>) to join a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) 
    |[`🔗 Binds`](<../../30 🧩 Data/20 🔗 Binds/🔗 Bind.md>)| [🧑‍🦰🚀 Binds](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/10 🧑‍🦰🚀🤵 Binds.md>) | List the [Binds 🔗](<../../30 🧩 Data/20 🔗 Binds/🔗 Bind.md>) of a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    || [🗄️🐌 Bindable](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/40 🤵🅰️ Binds 🔗/20 🗄️🐌🤵 Bindable.md>) | [Vaults 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) offer to bind [Schema Codes 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
    | [`🎫 Tokens`](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) | [🧑‍🦰🚀 Tokens](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/54 🧑‍🦰🚀🤵 Tokens.md>) | List of [Tokens 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) of a [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    || [🎴🐌 Offer](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/51 🎴🐌🤵 Offer.md>) | [Issuers 🎴](<../../41 🎭 Domain Roles/40 🎴 Issuers/🎴🎭 Issuer role.md>) offer an issued [Token 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) 
    || [🧑‍🦰🐌 Saved](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/53 🧑‍🦰🐌🤵 Saved.md>) | A [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) saved a [Token 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>) locally
    || [🎴🐌 Revise](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/50 🤵🅰️ Tokens 🎫/52 🎴🐌🤵 Revise.md>) | Update the status of a [Token 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>)
    | [`💼 Share`](<../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) | [💼🐌 Query](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) | Return user [Binds 🔗](<../../30 🧩 Data/20 🔗 Binds/🔗 Bind.md>) and [Tokens 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>)
    || [💼🚀 Status](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/62 💼🚀🤵 Status.md>) | Return the status of a [Token 🎫](<../../30 🧩 Data/30 🎫 Tokens/🎫 Token.md>)

    <!--
    |Pay| [💵🐌🤵 Charge](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/70 🤵🅰️ Pay/21 💵🐌🤵 Charge.md>)
    -->
    
    ---
    <br/>