💍 Userables to cross gates
===

> Mentioned in [Verify Userables 🆔](<../../../50 🫥 Agent domains/Identities 🆔/15 🆔💍 Verify Userables.md>)

<br/>


1. **How can users pass airport border controls with Userables?**

    Users can tell their [Custodian 🧳 agents](<../../../50 🫥 Agent domains/Custodians 🧳/$ 🧳🫥 Custodian agent.md>) which [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) should be available on their [Userable 💍 things](<../💍💠 Userable thing.md>) for automatic sharing on request. 
    
    - When a [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) asks for expected [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) of a given [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) (e.g., an airport gate expects passport [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>)), the [Custodian 🧳 agent](<../../../50 🫥 Agent domains/Custodians 🧳/$ 🧳🫥 Custodian agent.md>) can immediately share it without having to be in the context of a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>). 

    ---
    <br/>

1. **How does it work?**

    ![](<../. 📎 Assets/💍 Userable Cross Gates.png>)

    |#|Category|Step|
    |-|-|-
    |1| `Tap` | A user [taps 🔆](<../../1 🔆 Locators/🔆⏩ Locator flows/🧑‍🦰🔆 Wallet NFC tap.md>) their [Userable 💍 thing](<../💍💠 Userable thing.md>) on the [Scanner ✨ device](<../../../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>) of a [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) (e.g., a gate at an airport border control).
    |2| `Translate` | The [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) asks the [Userable's Wand 🪄 domain](<../../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) to translate the [Userable's Locator 🔆](<../../1 🔆 Locators/🔆 Locator.md>) into the [Locator 🔆](<../../1 🔆 Locators/🔆 Locator.md>) of the [owner's Custodian 🧳 vault](<../../../50 🫥 Agent domains/Custodians 🧳/$ 🧳🫥 Custodian agent.md>).
    |3| `Tokens?` | The [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) asks the [owner's Custodian 🧳 vault](<../../../50 🫥 Agent domains/Custodians 🧳/$ 🧳🫥 Custodian agent.md>) for any user-authorized sharable [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) that match a list of given [Schema Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>).
    |4| `{Tokens}` | The [owner's Custodian 🧳 vault](<../../../50 🫥 Agent domains/Custodians 🧳/$ 🧳🫥 Custodian agent.md>) returns the matching [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) to the [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>).
    |5| `Selfie` | The user looks at the [Selfie 📸 device](<../../../60 🧰 Edge/64 📸 Selfies/01 📸🔌 Selfie device.md>) of the [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) to collect face images.
    |6| `Owner?` | The [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) asks the [Identity 🆔 vaults](<../../../50 🫥 Agent domains/Identities 🆔/$ 🆔🫥 Identity agent.md>) of the received [identity-bound Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) if the person on the images is the owner of the [Tokens 🎫](<../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>).
    |7| `Match` | The [Identity 🆔 vaults](<../../../50 🫥 Agent domains/Identities 🆔/$ 🆔🫥 Identity agent.md>) perform a comparison between the images sent by the [Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) and the user's face biometrics stored on the [Identity 🆔 vault](<../../../50 🫥 Agent domains/Identities 🆔/$ 🆔🫥 Identity agent.md>).

    ---
    <br/>
