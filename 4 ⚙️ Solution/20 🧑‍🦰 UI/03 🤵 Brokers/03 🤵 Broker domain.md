🤵 Broker domains FAQ
===

![](<.📎 Assets/🤵 Broker.png>)

1. **What is a Broker domain in NLWeb?**
    
    Brokers orchestrate the relationship between [Wallets 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [Hosts 🤗](<../23 💬 Chats/03 🤗🎭 Host role.md>), working as the [Wallet's 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) database.

    ---

1. **How do Brokers protect users from Hosts?**
 
    Brokers give users the right to be forgotten by defaulting to anonymous browsing; 
    * i.e., whenever a user returns to a [Host 🤗](<../23 💬 Chats/03 🤗🎭 Host role.md>), the Broker connects them using a different untraceable ID. 
    
    * For a [Host 🤗](<../23 💬 Chats/03 🤗🎭 Host role.md>) to identity a user across sessions, the user needs to explicitly accept a [Bind 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) or [Token 🎫](<../27 🎫 Tokens/01 🎫 Token.md>) offered by the [Host 🤗](<../23 💬 Chats/03 🤗🎭 Host role.md>).

    ---

1. **Who migrates users between phones - Brokers or Notifiers?**

    Given that [Wallets 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [Notifiers 📣](<../02 📣 Notifiers/02 📣 Notifier domain.md>) contain only minimum-to-no data, the migration of a user between and old and a new phone needs to be done by Brokers.

    ---

1. **How do users migrate a Wallet to another phone?**

    To migrate a [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to another phone, a user first needs to bind an [Identity 🆔](<../../30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>) domain on the old phone, and then generate a migration QR [Token 🎫](<../27 🎫 Tokens/01 🎫 Token.md>).
    
    * On the new phone, the user needs to install a Wallet, then scan the migration QR of the old Wallet.
    * The Broker will invoke the Identity domain on the new phone to perform an identity authentication (e.g., face scan), and then will automatically decommission the old Wallet.

    ---

1. **How do users change between Wallet providers?**

    If both the old and the new [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) providers use the same Broker, then changing between Wallet providers in the same phone is very similar to migrating a Wallet to another phone. If they use different Brokers, then these Brokers will need to implement some sort of portability. For simplicity, let's assume they use the same Broker.
    
    * On the old Wallet app, the user generates a migration QR Token and downloads it or sends it to another person. 
    * Then, on the new Wallet app, the user uploads or scans the migration QR and performs an identity authentication (e.g., face scan).

    ---

1. **What if an attacker intercepts a user's recovery QR Token?**

    When a migration QR is used on a new [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), the Broker notifies the old Wallet, allowing legitimate owners to block the attack and destroy the QR. 
    
    For situations where legitimate owners are not aware of notifications, migrations have a small grace period where Brokers inactive both Wallets until the old Wallet accepts the transfer or the grace period expires.

    ---

1. **After destroying a migration QR, how can users migrate?**

    Just generate a new migration QR.

    ---

1. **After losing a phone, how do users recover a wallet on a new phone?**

    If the old phone is not available, then users need an offline migration QR previously printed or saved as an image - without it, it's not possible to recover the wallet. 
    
    * On the new phone, users install a Wallet, scan or upload the QR, perform an identity authentication, and wait for the grace period.

    ---

1. **What if an attacker has the user's old phone and rejects the transfer?**

    After a successful identity authentication on the new phone, blocking the migration from the old phone will also require a successful identity authentication. 

    * This way, an attacker in the possession of the old phone will not be able to stop the migration to the legitimate user.

    ---

1. **Why aren't Brokers and Notifiers the same domain?**
    
    Separating the responsibilities of Brokers and [Notifiers 📣](<../02 📣 Notifiers/02 📣 Notifier domain.md>) allows cloud providers (e.g., AWS, Azure, GCP) and independent software vendors (ISVs) to offload from mobile startups the undifferentiated heavy lifting of implementing the NLWeb protocol in the most robust, secure, and compliant way. 
    
    These startups can then focus on the Wallet and Notifier to create great frontend user experiences.

    ---

1. **How can Wallet startups connect to a Broker?**

    For startups and others to build a [Wallet 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), they need to:
    - Build a [Notifier 📣](<../02 📣 Notifiers/02 📣 Notifier domain.md>) domain and register it on a Broker;
    - Build a Wallet and pass the Broker's acceptance tests
    - Release the Wallet to onboard users into the Broker.

    ---

1. **How do Brokers ensure Wallets are NLWeb compliant?**

    Brokers are responsible for testing the compliance of [Wallets 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [Notifiers 📣](<../02 📣 Notifiers/02 📣 Notifier domain.md>) by performing a set of automated tests before allowing new Wallet versions to be used.

    * Notifiers are responsible for informing Brokers about changes in the software version, allowing Brokers to manage the test and release lifecycle of new versions 
    * Failure to inform may force the Broker to cut the Wallet's communication to NLWeb by blocking its Notifier.

    ---
