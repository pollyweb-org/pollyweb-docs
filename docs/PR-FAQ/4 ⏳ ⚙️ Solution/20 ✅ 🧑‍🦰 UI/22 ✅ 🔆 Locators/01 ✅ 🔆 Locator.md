🔆 NLWeb NFC/QR Locators FAQ
===

![](<./📎 Assets/🔆 Locators.png>)

1. **How are non-humans identified**

    In NLWeb, non-humans (e.g., organizations, places, objects, animals) are represented by a Locator. 
    * An NLWeb Locator is a string contained in a QR code, NFC tag, web link, or chat option.
    * Users can [tap 🔆](<04 ✅ 🧑‍🦰🔆 Wallet NFC tap.md>), [✨ scan](<03 ✅ 🧑‍🦰✨ Wallet QR scan.md>), select, or click Locators to open a chat with the Locator's [Host 🤗](<../23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>).

    ---

1. **What data is contained in a Locator?**

    A Locator contains:
    * the [Schema Code 🧩](<../24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>) (e.g., `nlweb.org/QR:1.0`)
    * the [🤗 Host domain](<../23 ✅ 💬 Chats/03 ✅ 🤗🎭 Host role.md>) (e.g., `any-host.com`)
    * the **resource key** in the Host's domain (e.g., `product-1234`)
    * any optional data fields.

    ---

1. **How can users interact with Locators?**

    Users can:
    * [tap](<04 ✅ 🧑‍🦰🔆 Wallet NFC tap.md>) or [scan](<03 ✅ 🧑‍🦰✨ Wallet QR scan.md>) an NLWeb-compatible static 🔆 NFC/QR printed by anyone;
    * tap/scan a static NFC/QR issue by any [🖨️ Printer](<../../70 ✅ 🌳 Ambient/71 ✅ 💠 Brand Things/08 ✅ 🖨️🏭 Printer supplier.md>);
    * tap/scan a dynamic NFC/QR rendered by an [🦋 Ephemeral](<../../60 ⏳ 🧰 Edge/62 ⏳ 🦋 Ephemerals/03 ⏳ 🦋🔌 Ephemeral device.md>);
    * tap/scan a [Wi-Fier 🛜](<../../60 ⏳ 🧰 Edge/61 ✅ 🔌 Pluggables/03 ✅ 🛜🔀 Wi-Fier router.md>) to connect it to the internet;
    * tap a [Userable 💍](<../../70 ✅ 🌳 Ambient/74 ✅ 💍 Brand Userables/01 ✅ 💍 Userable thing.md>) that a user is wearing or holding;
    * tap a [Padlock 🔒](<../../70 ✅ 🌳 Ambient/75 ✅ 🔒 Brand Padlocks/01 ✅ 🔒 Padlock device.md>) to open it;
    * select the result of a search in a chat with a [Finder 🔎](<../../30 ⏳ 🫥 Agents/10 ⏳ 🔎 Finders/02 ⏳ 🔎🫥 Finder vault.md>);
    * [scan](<03 ✅ 🧑‍🦰✨ Wallet QR scan.md>) a QR on a webpage;
    * [click](<02 ✅ 🧑‍🦰🌐 Wallet URLs.md>) on an NLWeb-compatible link on a webpage.

    ---

1. **How to ensure an NFC/QR locator was not tempered with?**

    A tempered NFC/QR allows for multiple attacks: 
    - 1/ in impersonation attacks, an attacker replaces the NFC/QR of a domain, impersonating it to drive users into fraudulent transactions using a credible brand; 
    - 2/ in misplacement attacks, an attacker may want access to door A, so it moves the NFC/QR of door A to door B and then waits by door A - a user trying to open door B will actually open door A instead. 
    
    Solutions:
    
    - While impersonation attacks are mitigated by NLWeb [👍 Trusts](<../../40 ✅ 👥 Domains/43 ✅ 👍 Trusts/01 ✅ 👍 Domain Trust.md>) and the principle of least-privilege, these mitigations don't protect users from impersonation attacks. 
    
    - For the misplacement attacks, domains should deploy hard-locked dynamic NFC/QR devices with rotating codes every X seconds - these cannot be misplaced nor copied, because a copy would only be valid until the next rotation. NLWeb supports these dynamic locators via [🦋 Ephemeral](<../../60 ⏳ 🧰 Edge/62 ⏳ 🦋 Ephemerals/03 ⏳ 🦋🔌 Ephemeral device.md>) devices.

    ---
