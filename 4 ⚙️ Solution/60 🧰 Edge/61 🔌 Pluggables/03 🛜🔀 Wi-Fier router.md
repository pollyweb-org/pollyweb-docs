🛜 Wi-Fier device feature
===

1. **What is a Wi-Fier device feature in PollyWeb?**

    A [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>) is a device feature for connecting to the internet on a Wi-Fi network.

    ---
    <br/>

1. **What are examples of Wi-Fiers?**

    |Example|Description
    |-|-
    |[🛜 Wi-Fier](<.📎 Assets/🔌🛜 Wi-Fier.png>)| A stand-alone ethernet hub, with RJ45 entries to connect other devices.
    |[🤖 Robot](<../../25 🔆 Locators/Robots 🤖/🤖💠 Robot thing.md>)| A home appliance (e.g., fridge, dishwasher) that connects to the Internet.
    |[📡 Antenna](<02 📡🔀 Antenna router.md>)| An integrated [Matter 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) hub for smart homes (e.g., Amazon Alexa).

    ---
    <br/>

1. **How is the Chat?**

    The [💬 Chat](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) may look similar to the following.

    | [Domain](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    |-|-|-
    | | | 🔆 [scan](<../../25 🔆 Locators/Locators 🔆/🔆⏩ Locator flows/🧑‍🦰✨ Wallet QR scan.md>)
    | 🔎 [Finder](<../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | ⓘ Any Wand (4.3 ⭐)  [+] || The [Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) informed the user.
    | 🪄 Wand | ℹ️ Device: [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>) || The [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) had a [Host 🤗](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)  callback.
    | 🪄 Wand | 😃 Hi! What do you need? <br/>- Set up [ 🛜 Wi-Fi ] <br/>- Call [Support] <br/>- [ Something else ] | > 🛜 Wi-Fi
    | [🤵 Broker](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | ⓘ Flow: Wi-Fi [+] || The [Host 🤗 role](<../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) changed the context.
    | 🧢 [Persona](<../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | 🫥 Share Wi-Fi? [All, No] <br/> - [ 🏠 home ] <br/> - [ 💼 office ]  | > 🏠 home | The [Consumer 💼 role](<../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) <br/> asked the [🤵 Broker domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to share <br/> the data with [ Schema Code 🧩](<../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) Wi-Fi.
    | 🪄 Wand | ⏳ Get close! [+] | 🚶 walk | 
    | 🪄 Wand | ⏳ Connecting... [+] | | The [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) found the BLE beacon.
    | 🪄 Wand | ✅ Done! [+] || The [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>) connected to the Wi-Fi.
    

    ---
    <br/>

1. **How does it work?**

    ![](<.📎 Assets/🔌🛜 Wi-Fier.png>)

    |#|Category|Step
    |-|-|-
    |0| `Bundle`| A [Brand 🍏 domain](<../../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>) selling an Internet-enabled product: <br/>- integrates a [Wi-Fier 🛜 feature](<03 🛜🔀 Wi-Fier router.md>) into the product; <br/>- registers the [Wi-Fier 🛜 feature](<03 🛜🔀 Wi-Fier router.md>) on a [Wand 🪄 helper domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>); <br/>- prints the [registration Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) into an NFC/QR tag on the product.
    |1| `Tap/Scan`| The user taps or scans the [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) of the [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>) enabled product with their [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    |2| `Translate`| That opens a [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>) with the [Wi-Fier's Wand 🪄 helper domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>): <br/>- the [Wand 🪄 domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) offers a set of options (e.g., connect, support); <br/>- the user chooses the option to connect the device to a Wi-Fi network.
    |3| `Credentials` | The [Wand 🪄 domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) asks the user to share their Wi-Fi credentials: <br/> - the [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) delegates to the [user's Persona 🧢 agent](<../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>); <br/>- the [user's Persona 🧢 agent](<../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) shares the Wi-Fi Credentials; <br/>- the [Wand 🪄 domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) subscribes to Wi-Fi credential updates.
    |4| `BLE` | The [Wand 🪄 domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) asks the [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) to onboard: <br/>- the [user's Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) pulls the encrypted credentials from the [Wand 🪄](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>); <br/>- the [user's Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) opens a [Matter 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) BLE connection to the [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>); <br/>- the [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>) receives the encrypted credentials and decrypts them.
    |5| `Connect`| The [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>) connects to the Wi-Fi network with the given credentials: <br/>- the [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>) sends a successful confirmation to the [Wand 🪄 domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>); <br/> - the [Wand 🪄 domain](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) informs the success to the user on the [Chat 💬](<../../35 💬 Chats/Chats 💬/💬 Chat.md>).
    |6| `Update` | Before updating the password of an on-premises Wi-Fi router: <br/>- users add the new password to their [Persona 🧢 agent](<../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>); <br/> - the [Persona 🧢](<../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>)publishes the change to all subscribed [Wands 🪄](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>).
    |7| `Migrate` | The subscribed [Wand 🪄 domains](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) then inform the [Wi-Fier 🛜](<03 🛜🔀 Wi-Fier router.md>) devices of the new password (assuming they still have a internet connection), for them to be prepared to reconnect automatically when the password is rotated on the on-premises Wi-Fi router.

    ---
    <br/>


1. **What are the advantages of Wi-Fiers?**

    |Problem|Solution
    |-|-
    |`No-app` | Users onboard with a single [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>), and not with device-specific apps.
    |`Bundle` | There's a single [NFC/QR Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) for onboarding and other [Wand 🪄](<../../45 🤲 Helper domains/Wands 🪄/🪄🤲 Wand helper.md>) features.
    |`Fleets`| Users inform about password changes only once on their [Persona 🧢 agent](<../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>).
    

    ---
    <br/>

1. **Why BLE instead of Wi-Fi Direct?**

    Wi-Fi Direct onboarding is a mechanism where an app has disconnect temporary from the current Wi-Fi network:
    * the Wi-Fier 🛜 broadcasts a Wi-Fi Direct network;
    * the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) temporarily disconnects from the current on-premises Wi-Fi router;
    * the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) connects to the Wi-Fi direct network of the Wi-Fier 🛜 to pass the credential;
    * the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) re-connects to the current on-premises Wi-Fi router.

    With Bluetooth Low Energy (BLE), the [Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) can have a second parallel communication channel;
    * thus, it does not need to disconnect from the current on-premises Wi-Fi router.

    ---
    <br/>

1. **Why not use only the Matter protocol?**

    A Wi-Fier 🛜 feature uses the [Matter protocol 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) for the Bluetooth Low Energy (BLE) step, taking advantage of the SDKs available for a range of devices.
    - However, while a Wi-Fier 🛜 is a generic feature, [Matter 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) is still focused on smart homes, and by 2025 is not yet broadly applied to all possible internet-connected devices and configurations.
    - Furthermore, [Matter 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) is focused on the technical communication and not on the user experience, so users still have to navigate the apps of the multiple vendors supporting the [Matter protocol 📺](<../../../2 🏔️ Landscape/3 🌳 Ambient landscape/01 🏡 Smart Homes/14 📺 Matter protocol.md>) - instead, a Wi-Fier 🛜 brings a seamless experience in the [user's Wallet 🧑‍🦰 app](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
  
    ---
    <br/>
