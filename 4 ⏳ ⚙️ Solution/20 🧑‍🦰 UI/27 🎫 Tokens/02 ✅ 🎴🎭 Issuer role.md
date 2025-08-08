🎴 Issuer domain role FAQ
===

![](<./📎 Assets/🎫 Issuer.png>)

1. **What is an Issuer domain role in NLWeb?**

    An Issuer is a [Vault 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>) that allows users to download [Tokens 🎫](<01 ✅ 🎫 Token.md>).
    
    ---
    
1. **How much data should Issuers add to a Token?**

    The less data, the better. 
    * [Tokens 🎫](<01 ✅ 🎫 Token.md>) are signed but not encrypted - thus, all data in a token can be read by an attacker. 
    * When sharing a Token, users implicitly allow domains to contact the Issuer for additional data about the Token - domains can leverage this direct channel to do an online verification, synchronously or asynchronously.

    ---
    
1. **Can an Issuer revoke a Token?**

    Yes. 
    * [Tokens 🎫](<01 ✅ 🎫 Token.md>) are issued with the help of a [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) that orchestrates the relationship between the Issuer and the user. 
    * Issuers can request the [Broker 🤵](<../03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>) to invalidate Tokens, and Brokers will handle the propagation up to the user's [Wallet 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>).
    * In cases where the user is holding an offline image of the Token's QR (e.g., printed or screenshot), [💼 Consumers](<../25 ✅ 💼 Consumers/04 ✅ 💼🎭 Consumer role.md>) may ask for a synchronous status check of a Token directly with the Issuer (e.g., while validating a passport token at the border, the airport may try to reach the Issuer to verify if the passport hasn't been revoked).

    ---
    