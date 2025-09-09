🎴 Issuer domain role FAQ
===

1. **What is an Issuer domain role in NLWeb?**

    An Issuer is any [Host 🤗 domain](<../23 💬 Chats/03 🤗🎭 Host role.md>) that allows users to download [Tokens 🎫](<01 🎫 Token.md>).
    
    ---

2. **How do Issuers work?**

    ![](<.📎 Assets/🎫 Issuer.png>)

    | # | Step 
    |-|-
    |1| A user engages in a [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>) with a [Host 🤗 domain](<../23 💬 Chats/03 🤗🎭 Host role.md>) with an Issuer 🎴 role.
    |2| The Issuer 🎴 issues a [Token 🎫](<01 🎫 Token.md>) for the user, and the user's [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) asks the user to confirm if they want to save the [Token 🎫](<01 🎫 Token.md>) offline in the [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    
3. **How much data should Issuers add to a Token?**

    The less data, the better. 

    * [Tokens 🎫](<01 🎫 Token.md>) are signed but not encrypted - thus, all data in a [Token 🎫](<01 🎫 Token.md>) can be read by an attacker. 
    
    * When sharing a [Token 🎫](<01 🎫 Token.md>), users implicitly allow domains to contact the Issuer 🎴 for additional data about the Token - domains can leverage this direct channel to do an online verification, synchronously or asynchronously.

    ---
    
4. **Can an Issuer revoke a Token?**

    Yes. 

    * [Tokens 🎫](<01 🎫 Token.md>) are issued with the help of a [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) that orchestrates the relationship between the Issuer 🎴 and the user. 
    
    * Issuers 🎴 can request the [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) to invalidate [Tokens 🎫](<01 🎫 Token.md>), and [Broker 🤵 domains](<../03 🤵 Brokers/03 🤵 Broker domain.md>) will handle the propagation up to the user's [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    
    * In cases where the user is holding an offline image of the Token's QR (e.g., printed or screenshot), [Consumer 💼 domains](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) may ask for a synchronous status check of a [Token 🎫](<01 🎫 Token.md>) directly with the Issuer 🎴 - e.g., while validating a passport [Token 🎫](<01 🎫 Token.md>) at the border, the airport may try to reach the Issuer 🎴 to verify if the passport hasn't been revoked.

    ---
    