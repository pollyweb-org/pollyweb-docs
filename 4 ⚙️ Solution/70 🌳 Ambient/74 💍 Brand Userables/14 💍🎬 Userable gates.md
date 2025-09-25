💍 Userables to cross gates FAQ
===


1. **How can users pass airport border controls with Userables?**

    Users can tell their [Custodian 🧳 agents](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) which [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) should be available on their [Userable 💍 things](<01 💍 Userable thing.md>) for automatic sharing on request. 
    
    - When a [Consumer 💼 domain](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) asks for expected [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) of a given [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) (e.g., an airport gate expects passport [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>)), the [Custodian 🧳 agent](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) can immediately share it without having to be in the context of a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>). 

    ---
    <br/>

1. **How does it work?**

    ![](<00 📎 Assets/💍 Userable Cross Gates.png>)

    |#|Category|Step|
    |-|-|-
    |1| `Tap` | A user [taps 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/04 🧑‍🦰🔆 Wallet NFC tap.md>) their [Userable 💍 thing](<01 💍 Userable thing.md>) on the [Scanner ✨ device](<../../60 🧰 Edge/66 ✨ Scanners/06 ✨🔌 Scanner device.md>) of a [Consumer 💼 domain](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) (e.g., a gate at an airport border control).
    |2| `Translate` | The [Consumer 💼 domain](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) asks the [Userable's Wand 🪄 domain](<../71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) to translate the [Userable's Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) into the [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) of the [owner's Custodian 🧳 vault](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>).
    |3| `Tokens?` | The [Consumer 💼 domain](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) asks the [owner's Custodian 🧳 vault](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) for any user-authorized sharable [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) that match a list of given [Schema Codes 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>).
    |4| `{Tokens}` | The [owner's Custodian 🧳 vault](<../71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) returns the matching [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) to the [Consumer 💼 domain](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>).
    |5| `Selfie` | The user looks at the [Selfie 📸 device](<../../60 🧰 Edge/64 📸 Selfies/01 📸🔌 Selfie device.md>) of the [Consumer 💼 domain](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) to collect face images.
    |6| `Owner?` | The [Consumer 💼 domain](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) asks the [Identity 🆔 vaults](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) of the received [identity-bound Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) if the person on the images is the owner of the [Tokens 🎫](<../../20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).
    |7| `Match` | The [Identity 🆔 vaults](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) perform a comparison between the images sent by the [Consumer 💼 domain](<../../20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) and the user's face biometrics stored on the [Identity 🆔 vault](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>).

    ---
    <br/>
