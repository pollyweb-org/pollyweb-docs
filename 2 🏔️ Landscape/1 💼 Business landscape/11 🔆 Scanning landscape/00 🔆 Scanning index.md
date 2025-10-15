🔆 Scanning landscape
===

## 🎯 Target

QR codes and NFC cards have become an ubiquitous ways for users to pay for transactions (specially during the pandemic).

- However, other use cases have not gain traction (e.g., menus in restaurants). 
- Several reasons may have contributed to the lack of traction, e.g.:
    - QR/NFC payments speeds up checkouts, while digital menus make it slower;
    - QR/NFC payments don't need screen interactions, so there's no digital fatigue;
    - menus are typically long, making them hard to see on phone screens;
    - due to images, poor infrastructure, or bad network, pages may load slowly;
    - implementing a digital solution can be overwhelming for small businesses;
    - and the FBI reported bad actors replacing QR codes to perform phishing scams.


To address fraud with URL redirect by replacing real QR codes with fake ones:
- in 🇨🇳 China, WeChat and AliPay use in-app QR scan, with URL redirect blocked;
- in 🇷🇺 Russia, Kaspersky uses a QR scanner app with pre-redirect URL verification;
- and in the 🇺🇸 U.S., Apple created App Clip Codes, a rounded QR alternative.


---

## 💬 Proposed solution

NLWeb advocates QR/NFC usage with the following improvements.

|Component|Objective
|-|-
| [🫥 Agents](<../../../4 ⚙️ Solution/30 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) | To reduce the duration of user workflows when compared to traditional methods.
| [🪄 Wands](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/90 🪄 Wands/$ 🪄🛠️ Wand helper.md>) | To cognify interaction points with businesses (e.g., products, places, things).
| [🍏 Brands](<../../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>) | Easy and affordable to set up and maintain by businesses.
| [💬 Chats](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) | Consuming as little network bandwidth as a natural language chat.
| [💠 Things](<../../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>) | Using ubiquitous non-proprietary QR and NFC standards.
| [🔆 Locators](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) | With safety validation of the QR/NFC landing page.

---


## 📺 Enablement resources

In this chapter, you will learn:

- What [digital product IDs 📺](<01 📺 Product IDs.md>) are,
    - and how they enable [personalized experiences 📺](<02 📺 Personalization.md>).

- What [QR codes 📺](<03 📺 QR codes.md>) are, 
    - how to change a QR code [dynamically 📺](<04 📺 QR dynamic url.md>);
    - what are the FBI [safety 📺](<05 📺 QR safety.md>) concerns with QR codes;
    - what is [quishing 📺](<06 📺 QR phishing.md>), the QR equivalent of phishing;
    - how [Kaspersky 📺](<07 📺 QR scanner.md>)'s QR scanner protects users by verifying QR codes;
    - and how developers can [verify URLs 📺](<08 📺 Google's Risk API.md>) using Google's Web Risk API.

- What [NFC tags 📺](<09 📺 NFC tags.md>) are,
    - how [RFID 📺](<10 📺 NFC vs RFID.md>) relates to NFC,
    - what are [authenticated 📺](<11 📺 NFC authentication.md>) NFC tags, 
    - what are [temper-aware 📺](<12 📺 NFC tamper aware.md>) NFC tags, 
    - from [how far 📺](<13 📺 NFC tap distance.md>) an NFC tag can be tapped,
    - how to use NFC tags in [clothing 📺](<14 📺 NFC in clothing.md>),
    - how to use NFC tags on [metal 📺](<15 📺 NFC on metal.md>),
    - and how to change an NFC tag [dynamically 📺](<16 📺 NFC dynamic url.md>).

- What Apple's [App Clips 📺](<17 📺 Apple's App Clips.md>) are,
    - and what are App Clip [Codes 📺](<18 📺 App Clip Codes.md>), Apple's QR/NFC alternative.

---



<!--1. How to use the iPhone Tag Reader to read NFC tags in iOS 14
    2020
    Seritag NFC Tags (a UK-based NFC tag provider)
    published the following video, titled *"
    https://youtu.be/siEksdUEn9o
    https://github.com/user-attachments/assets/39084f14-e65b-4fa1-a472-4baa73af7a01


    ---
-->    




<!-- 1. How to order full color NFC tags for your project

    In 2024, Seritag NFC Tags (a UK-based NFC tag provider) published the following video, titled *"Custom Printed NFC Stickers - How to order full color NFC tags for your project"*.

    - The video describes how to order custom printed NFC labels from Seritag. 
    - It explains the different materials, finishes, and chip options available, as well as the production process and turnaround times.

    -- https://youtu.be/SwfBla2vw7E --<br/>
    https://github.com/user-attachments/assets/cbed4a39-7773-4de1-bf57-921d7a5cac48
    


    -->

<!-- 1. How to encode/write an NFC tag with an Android phone

    In 2019, Seritag NFC Tags (a UK-based NFC tag provider) published the following video, titled *"How to encode/write an NFC tag with an Android phone"*.
    
    - The video demonstrates how to encode a web address onto an NFC tag using an Android phone and the NXP TagWriter app. 
    - It covers the encoding process, checking the encoded data, and locking the tag to prevent future modifications.


    !-- https://youtu.be/TPMsXAtGGZ8 --<br/>
    https://github.com/user-attachments/assets/d12d417b-b93b-41a7-a231-9a2a4e925229


    -->
