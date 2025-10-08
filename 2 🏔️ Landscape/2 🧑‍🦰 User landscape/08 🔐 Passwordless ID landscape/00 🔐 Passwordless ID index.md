🔐 Passwordless authentication landscape
===

🎯 Humans typically expect frictionless interactions between entities, both in business-to-consumer (B2C) and business-to-business (B2B) scenarios - e.g.:

- quick and frictionless consumer check-ins (e.g., entering a coffee shop);
- frictionless usage of the premises (e.g., connecting the wi-fi to see the menu);
- quick and frictionless consumer check-outs (e.g., paying for the drink);
- a similar experience for enterprises when performing B2B transactions.

---

🤔 Let's consider the following scenarios:

- When a consumer walks into a business (e.g., a coffee shop ☕):
    - they want to be able to buy a coffee without needing to fill a registration form;
    - they want to be remembered when returning 5 minutes complaining about the coffee;
    - they don't want to be traced when entering other brands of the same owner;
    - NLWeb achieves these consumer expectations by replicating how, since 2022, online users interact with site registrations when [FIDO passkeys](<02 📺 FIDO passkeys.md>) are supported.

- When a consumer is paying for the goods (e.g., the coffee):
    - both the consumer and the business want it to be as fast as possible;
    - NLWeb achieves these expectations by leveraging the ubiquitous [contactless NFC](<05 📺 Financial industry.md>) experiences of payment cards across the entire business interaction.

- When a consumer is using the business premise (e.g., relaxing in table):
    - they want to be able to remain online, even if in an underground facility;
    - for this, NLWeb leverages the passwordless experiences provided by the [Wi-Fi Alliance](<06 📺 Wi-fi easy connect.md>).

- When a business interacts with other businesses (e.g., to buy coffee grains):
    - they want to be able to perform a transaction without needing to fill a registration form;
    - they want to access a given level of service (e.g., net 30 payment terms) by presenting a reputation credential issued by a mutually trusted entity (e.g., a state issued incorporation certificate);
    - they want to be able to affect the credit reputation of the other party if they default;
    - NLWeb achieves these business expectations in part by replicating the authentication and reputation strategies applied by [email servers](<07 📺 Email DKIM.md>) when interacting with other unknown email servers. 

---

💬 NLWeb advocates for:
- a protocol like Chrome's passkey between consumers and businesses;
- and a protocol like email server authentication between businesses. 

---

📺 In this chapter, you will learn:

- Why Google, Apple, and Microsoft are [eliminating passwords](<01 📺 Why drop passwords.md>).
- How [🔑 FIDO passkeys](<02 📺 FIDO passkeys.md>) implement passwordless authentication.
- What [🌐 Google](<03 📺 Google passkeys.md>) and 🌐[Microsoft](<04 📺 Microsoft passkeys.md>) are doing with passkeys.
- Why [🌐 IBM](<08 📺 Global Identity Crisis.md>) considered passwordless authentication a top security priority in 2024.
- What the [💳 financial industry](<05 📺 Financial industry.md>) doing with passwordless payments.
- What the [🛜 Wi-Fi Alliance](<06 📺 Wi-fi easy connect.md>) is doing with passwordless Wi-Fi onboarding.
- How [📨 email servers](<07 📺 Email DKIM.md>) implement passwordless domain authentication.
- How [🌐 web servers](<09 📺 PKI certificates.md>) authenticate with SSL certificates and PKI.
- What NIST recommends regarding the [🔑 post-quantum cryptography](<10 📺 Post-quantum keys.md>). 


---
