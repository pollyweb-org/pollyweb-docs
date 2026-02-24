🔑 Smart Keys landscape
===


🎯 While outdoors, humans typical carry a wallet and keys.
- When digitalizing wallets, digitalizing keys seems the obvious next step.
- In 2024, Apple led the race with NFC/UWB emulation and Power Reserve mode.

---

📺 In this chapter, you will learn:

- How safe are keys for physical access, namely:
    - traditional [metal keys](<01 📺 Metal keys.md>),
    - RFID/NFC [fob keys](<02 📺 Fob keys.md>),
    - RFID/NFC [security badges](<03 📺 Security badges.md>),
    - RFID/NFC [smart car keys](<04 📺 Smart car keys.md>),
    - portable [smart padlocks](<05 📺 Smart padlocks.md>),
    - and home [smart locks](<06 📺 Smart lock safety.md>).

- What is the state of the market, namely:
    - what were the [top home smart locks](<07 📺 Top smart locks.md>) in 2024,
    - how to use [biometrics](<08 📺 Biometrics access.md>) for home access,
    - how to use [QR codes](<09 📺 Enterprise access.md>) with biometrics for enterprise access,
    - how Apple's NFC [Smart Keys](<10 📺 Apple Key + BMW.md>) can open and start a BMW,
    - and what is [Ultra Wide Band](<11 📺 Apple Key UWB.md>) (UWB), used by Apple Keys and Tags.
    
---

💬 PollyWeb advocates for a combination of:

- 🔑 Active key holders:
    - run on a semi-connected smart device (e.g., watch, phone);
    - receive pushed key-configuration updates from a server;
    - have an active NFC reader activating a passive bidirectional NFC lock;
    - answer a security challenge back to the lock via an NFC packet;
    - NFC power consumption overhead on a smart watch is ~5% per day.

- 🚙 Passive car locks:
    - authentication: passive bidirectional NFC emulated tag;
    - backup: traditional metal key;
    - key management: via the internet,
        - with a 5G-connected central hub,
        - updated keys store in a central non-volatile memory;
    - power: the car's battery.

- 🔒 Passive padlocks:
    - authentication: passive bidirectional NFC emulated tag;
    - backup: traditional metal key or metallic number combination;
    - key management: with NFC,
        - with an NFC reader app sending sending authenticated updates,
        - authentication based on an factory secret,
        - updated keys store in internal non-volatile memory;
    - power: internal battery,
        - ~100 years of expected lifetime on standby;
        - with power status on an e-ink display updated daily;
        - chargeable via battery sharing from a smart phone.

- 🚪 Passive door locks: 
    - authentication: passive bidirectional NFC emulated tag;
    - backup: metal key and dynamic keypad (attached or detached);
    - key management: via the internet,
        - with Matter mesh indoor (~100 milliseconds, ~10 meters per hop),
        - with LoraWan B/C outdoor (~100 ms to 1 second, ~2 km),
        - with WiFi for wireless Matter/LoraWan (~20 milliseconds, ~30 meters);
    - power: internal battery,
        - chargeable via an USB-C entry,
        - chargeable via RF ambient wireless charging,
        - chargeable via battery sharing from a smart phone.
        

---


<!-- Apple Tag

    2021
    Apple Explained
    published the following video, titled *"
    How AirTags Work
    https://youtu.be/lXxWh2tkKgk
    https://github.com/user-attachments/assets/193b213d-a8fd-4f97-b9d0-6c32978bd268
    
    
    2021
    CNET
    published the following video, titled *"
    Apple AirTags: Hands-on with the tiny tracker
    https://youtu.be/T-qHrr-tW9Y
    https://github.com/user-attachments/assets/2337609a-a49f-4495-b439-4dd729dc661d
    
    

    -->
    
<!-- Google Find My...
    2024
    CNET
    Apple vs Google: Find My Device Challenge
    https://youtu.be/fqng1jegl0U
    https://github.com/user-attachments/assets/60d9f5b6-f164-41c9-860c-5461250cbc1a


    -->

<!-- Samsung Galaxy SmartTag+
    2022
    Samsung Singapore
    Galaxy SmartTag+: Tag it. Find it. Simply smart with AR. | Samsung
    https://youtu.be/BkDIgbzMkQ0
    https://github.com/user-attachments/assets/e69ab0f3-f6e5-46f7-9bab-1ecf86b0ba3e
    

    -->