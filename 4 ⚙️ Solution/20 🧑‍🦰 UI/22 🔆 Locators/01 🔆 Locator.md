🔆 NLWeb NFC/QR Locators FAQ
===

1. **What are NLWeb Locators?**

    In NLWeb, non-humans (e.g., organizations, places, objects, animals) are represented by a [Locator 🔆](<01 🔆 Locator.md>). 
    * An NLWeb [Locator 🔆](<01 🔆 Locator.md>) is a string contained in a [QR code ✨](<03 🧑‍🦰✨ Wallet QR scan.md>), [NFC tag 🔆](<04 🧑‍🦰🔆 Wallet NFC tap.md>), [Web link 🌐](<02 🧑‍🦰🌐 Wallet URLs.md>), or [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>) option.
    * Users can [tap 🔆](<04 🧑‍🦰🔆 Wallet NFC tap.md>), [scan ✨](<03 🧑‍🦰✨ Wallet QR scan.md>), [select 💬](<../23 💬 Chats/01 💬 Chat.md>), or [click 🌐](<02 🧑‍🦰🌐 Wallet URLs.md>) Locators 🔆 to open a [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>) with the [Locator's Host 🤗 domain](<../23 💬 Chats/04 🤗🎭 Host role.md>).

    ---
    <br/>
    

3. **What data is contained in a Locator?**

    A [Locator 🔆](<01 🔆 Locator.md>) is a string 
    * formatted as `{schema code},{host domain},{resource}[,{parameters}]`
    * e.g.: `nlweb.org/HOST:1.0,any-domain.com,ANY-RESOURCE`

    |Component| Example | Purpose
    |-|-|-
    | [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) | `nlweb.org/HOST:1.0` | To validate the schema with a [Graph 🕸 helper domain](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>).
    | [Host 🤗 domain](<../23 💬 Chats/04 🤗🎭 Host role.md>) | `any-host.com` | For the user's [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to open a [Chat 💬](<../23 💬 Chats/01 💬 Chat.md>).
    | Resource | `product-1234` | The resource key in the Host's domain |  `product-1234` |
    | Parameters | `A=1,B=2` | any optional data fields.

    ---
    <br/>

4. **How can users interact with Locators?**

    ![](<.📎 Assets/🔆 Locators.png>)
    

    To interact with a [Locator 🔆](<01 🔆 Locator.md>), users use their [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) with one of the following.
    
    | [Locator 🔆](<01 🔆 Locator.md>) | Method 
    |-|-
    | [✨ Physical QR code](<03 🧑‍🦰✨ Wallet QR scan.md>) | Scan an NLWeb-compatible physical [QR code ✨](<03 🧑‍🦰✨ Wallet QR scan.md>) printed by anyone.
    | [🔆 Physical NFC tag](<04 🧑‍🦰🔆 Wallet NFC tap.md>) | Tap a NLWeb-compatible physical [NFC tag 🔆](<04 🧑‍🦰🔆 Wallet NFC tap.md>) written by anyone.
    | [✨ Digital QR code](<03 🧑‍🦰✨ Wallet QR scan.md>)  | Scan an image of a [QR code ✨](<03 🧑‍🦰✨ Wallet QR scan.md>) rendered by a webpage.
    | [🌐 Web page link](<02 🧑‍🦰🌐 Wallet URLs.md>)  |  Click on an NLWeb-compatible [URL link 🌐](<02 🧑‍🦰🌐 Wallet URLs.md>) on a webpage.
    | [🖨️ Printer domains](<../../70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) | Tap/scan a static NFC/QR issue by any [Printer 🖨️ helper domain](<../../70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>).
    | [🦋 Ephemeral devices](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) | Tap/scan a dynamic NFC/QR rendered by an [Ephemeral 🦋 device](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>).
    | [🛜 Wi-Fier devices](<../../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>) | Tap/scan a [Wi-Fier 🛜 device](<../../60 🧰 Edge/61 🔌 Pluggables/03 🛜🔀 Wi-Fier router.md>) to connect it to the internet.
    | [💍 Userable things](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) | Tap a [Userable 💍 thing](<../../70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>) that a user is wearing or holding.
    | [🔒 Padlock devices](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>)  | Tap a [Padlock 🔒 device](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>) to open it.
    | [💬 Chat prompts](<../23 💬 Chats/01 💬 Chat.md>) | Select a [Host 🤗 domain](<../23 💬 Chats/04 🤗🎭 Host role.md>) option - e.g., [Finder 🔎](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>), [Advertiser 👀](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>).

    
    ---
    <br/>



2. **Can Locators be forged?**

    Yes. 
    
    - Thread agents may replace authentic Locators 🔆 fake ones for a number of reasons, e.g.:
        - in **business impersonation attacks**, an attacker replaces the QR/NFC/URL of a business, impersonating it to drive users into [data phishing 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/06 📺 QR phishing.md>) and/or fraudulent transactions using a credible brand; 
        - in **misplacement attacks**, an attacker may want access to door A, so it moves the NFC/QR of door A to door B and then waits by door A - a user trying to open door B will actually open door A instead. 
  

    - Forging Locators 🔆 may be done in multiple ways, e.g.:
        - [QR codes ✨](<03 🧑‍🦰✨ Wallet QR scan.md>) are typically forged with an overlay on top of the original code;
        - [NFC tags 🔆](<04 🧑‍🦰🔆 Wallet NFC tap.md>) are typically forged with a replacement of the original tag;
        - [URL links 🌐](<02 🧑‍🦰🌐 Wallet URLs.md>) are typically forged with malicious javascript on the browser;
        - new fake NFC/QR Locators 🔆 may placed strategically near the target services (e.g., in pillars of a parking lot).

    ---
    <br/>

1. **How can users detect business impersonation attacks?**

    User's best option to detect whether a [Locator 🔆](<01 🔆 Locator.md>) is genuine or fake, is to see if it opens their [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) or if it opens a web page.

    - If it opens their [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>), then they'll know that all messages will safely go through a trustworthy [Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>).
    - Instead, if the [Locator 🔆](<01 🔆 Locator.md>) opens a web page, then it's most probably not an NLWeb [Locator 🔆](<01 🔆 Locator.md>).
    - Exceptionally, users will be directed to the `nlweb.org` website if they do not have a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) installed on their smartphone.

    Given that the [Wallet's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>) serves as a protector, user can trust its mechanism to protect them from [phishing sites 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/06 📺 QR phishing.md>), just like Google Chrome does with [SSL certificate validation 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/08 📺 Google's Risk API.md>) and other phishing detection/blocking features - these mechanisms include:

    - [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) can only flow through encrypted channels with cross-authentication of both sender and receiver domains;
    - Data exchange can only be performed between domains that publicly [Trust 👍](<../../40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) one another or are trusted by mutually trusted [Authority 🏛️ domains](<../../40 👥 Domains/43 👍 Trusts/02 🏛️🛠️ Authority helper.md>), following the principle of least-privilege;
    - User inputs can only be collected if the intention is clearly mentioned in a [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) subject to public scrutiny.
    

    ---    
    <br/>

2. **How can businesses be protected by misplacement attacks?**
    
    Businesses can implement the following security mechanisms for misplacement attacks, where an attacker replaces a genuine [Locator 🔆](<01 🔆 Locator.md>) A for another genuine [Locator 🔆](<01 🔆 Locator.md>) B in order to trick a user to unlock the resource B instead of the resource A:

    - deploy read-only [rotating NFC tags 📺](<../../../2 🏔️ Landscape/1 💼 Business landscape/11 🔆 Scanning landscape/11 📺 NFC authentication.md>) without a QR code;
    - deploy [Ephemeral 🦋 devices](<../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>) that emulates both a [QR code ✨](<03 🧑‍🦰✨ Wallet QR scan.md>) and an [NFC tag 🔆](<04 🧑‍🦰🔆 Wallet NFC tap.md>) with a [Locator 🔆](<01 🔆 Locator.md>) that rotates every X seconds.

    ---
    <br/>