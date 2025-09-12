🛜 Wi-Fier device feature FAQ
===

1. **What is a Wi-Fier device feature in NLWeb?**

    In NLWeb, a Wi-Fier 🛜 is a device feature that enable access to a Wi-Fi network.

    ---

2. **What are examples of Wi-Fiers?**

    |Example|Description
    |-|-
    |[🛜 Wi-Fier](<.📎 Assets/🔌🛜 Wi-Fier.png>)| A stand-alone ethernet hub, with RJ45 entries to connect other devices.
    |[🤖 Robot](<../../70 🌳 Ambient/72 🤖 Brand Robots/01 🤖💠 Robot thing.md>)| A home appliance (e.g., fridge, dishwasher) that connects to the Internet.
    |[📡 Antenna](<02 📡🔀 Antenna router.md>)| An integrated [Matter 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) hub for smart homes (e.g., Amazon Alexa).

    ---


3. **How does it work?**

    ![](<.📎 Assets/🔌🛜 Wi-Fier.png>)

    |#|Category|Step
    |-|-|-
    |0| `Bundle`| A [Brand 🍏 domain](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>) selling an Internet-enabled product: <br/>- integrates a Wi-Fier 🛜 feature into the product; <br/>- registers the Wi-Fier 🛜 feature on a [Wand 🪄 helper domain](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>); <br/>- prints the [registration Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) into an NFC/QR tag on the product.
    |1| `Tap/Scan`| The user taps or scans the [Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) of the Wi-Fier 🛜 enabled product with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    |2| `Translate`| That opens a [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) with the [Wi-Fier's Wand 🪄 helper domain](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>): <br/>- the [Wand 🪄 domain](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) offers a set of options (e.g., connect, support); <br/>- the user chooses the option to connect the device to a Wi-Fi network.
    |3| `Credentials` | The [Wand 🪄 domain](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) asks the user to share their Wi-Fi credentials: <br/> - the [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) delegates to the [user's Persona 🧢 agent](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>); <br/>- the [user's Persona 🧢 agent](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) shares the Wi-Fi Credentials; <br/>- the [Wand 🪄 domain](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) subscribes to Wi-Fi credential updates.
    |4| `BLE` | The [Wand 🪄 domain](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) asks the [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to onboard: <br/>- the [user's Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) pulls the encrypted credentials from the [Wand 🪄](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>); <br/>- the [user's Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) opens a [Matter 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) BLE connection to the Wi-Fier 🛜; <br/>- the Wi-Fier 🛜 receives the encrypted credentials and decrypts them;
    |5| `Connect`| The Wi-Fier 🛜 connects to the Wi-Fi network with the given credentials: <br/>- the Wi-Fier 🛜 sends a successful confirmation to the [Wand 🪄 domain](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>); <br/> - the [Wand 🪄 domain](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) informs the success to the user on the [Chat 💬](<../../20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>).
    |6| `Update` | Before updating the password of an on-premises Wi-Fi router: <br/>- users add the new password to their [Persona 🧢 agent](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>); <br/> - the [Persona 🧢](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>)publishes the change to all subscribed [Wands 🪄](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>).
    |7| `Migrate` | The subscribed [Wand 🪄 domains](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) then inform the Wi-Fier 🛜 devices of the new password (assuming they still have a internet connection), for them to be prepared to reconnect automatically when the password is rotated on the on-premises Wi-Fi router.

    ---


4. **What are the advantages of Wi-Fiers?**

    |Problem|Solution
    |-|-
    |`No-app` | Users onboard with a single [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), and not with device-specific apps.
    |`Bundle` | There's a single [NFC/QR Locator 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) for onboarding and other [Wand 🪄](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) features.
    |`Fleets`| Users inform about password changes only once on their [Persona 🧢 agent](<../../30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>).
    

    ---

1. **Why BLE instead of Wi-Fi Direct?**

    Wi-Fi Direct onboarding is a mechanism where an app has disconnect temporary from the current Wi-Fi network:
    * the Wi-Fier 🛜 broadcasts a Wi-Fi Direct network;
    * the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) temporarily disconnects from the current on-premises Wi-Fi router;
    * the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) connects to the Wi-Fi direct network of the Wi-Fier 🛜 to pass the credential;
    * the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) re-connects to the current on-premises Wi-Fi router.

    With Bluetooth Low Energy (BLE), the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) can have a second parallel communication channel;
    * thus, it does not need to disconnect from the current on-premises Wi-Fi router.

---

1. **Why not use only the Matter protocol?**

    A Wi-Fier 🛜 feature uses the [Matter protocol 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) for the Bluetooth Low Energy (BLE) step, taking advantage of the SDKs available for a range of devices.
    - However, while a Wi-Fier 🛜 is a generic feature, [Matter 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) is still focused on smart homes, and by 2025 is not yet broadly applied to all possible internet-connected devices and configurations.
    - Furthermore, [Matter 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) is focused on the technical communication and not on the user experience, so users still have to navigate the apps of the multiple vendors supporting the [Matter protocol 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) - instead, a Wi-Fier 🛜 brings a seamless experience in the [user's Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
  
    ---