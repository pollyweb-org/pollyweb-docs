<!-- #TODO -->

⏳📇 Mingler vault domains
===

1. **What is a Mingler?**

    A Mingler 📇 is a user [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) that networks with other [🧑‍🦰Wallets](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) via their Minglers?

    ---

1. **What are the responsibilities of Mingler?**

    Mingler responsibilities include:
    - Keep a list of connected [🧑‍🦰Wallets](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) and send them messages;
    - Fan out incoming interactions to the user's desired communication channels:
        - e.g., email, phones, WhatsApp, phone recording;
        - this allows users to control how to receive messages and calls.
    - Forward requests from services to connected users:
        - e.g., IDs for [invitation letters 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/09 🧳 Travel by air 💺/12 💺 Invitation letter/01 Send letter.md>), ride hailing payments;
        - this allows connected users to control how their tokens are used.
    - Save tokens from connected users: 
        - e.g., elder's [discount tickets 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/02 🚎 Traveler @ Stop/21 Buy smart tickets.md>), shared car documents;
        - this allows care givers to represent their care takers.
    
    
    ---

1. **Couldn't these responsibilities be handled by a Broker?**

    [Brokers 🤵](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) see [Wallet apps 🧑‍🦰](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) as unique entities;
    - while Minglers 📇 can associate and disassociate multiple entry points to the same [Wallet app 🧑‍🦰](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>);
    - this allows users to be forgotten and be perceived differently by different groups.

    ---

<!-- 
Notes
- hides email addresses also, forwarding channel numbers
- each shared contact generates a channel associated with the recipient
- when the recipient replies, the user knows who's calling (or the origin of the spam)
- users defines how they want to be reached out (phones, emails, messaging apps)
- users can change the inbound targets without notifying the senders

minglers connect between each other in the following ways: 
- text message
- audio message
- video message
- audio call
- video call
- forwarding broker requests: share, save

Privacy:
- messages are encrypted end-to-end 
    - mingler A has phone X's public key
    - mingler B has phone Y's public key
    - phone X encrypts with their private key and sends to mingler A
    - mingler A informs mingler B
    - mingler B informs phone Y
    - phone Y pulls from mingler A
    - somehow, mingler B needs to verify phone Y
    - each mingler only has the info sent.
    - to rebuild a dialog history, wallets need to pull from both A and B minglers
    - this allows senders to delete their history of messages sent

-->