⌚ Tapband device
===

![](<00 📎 Assets/⌚ Tapband.png>)

1. **What is a Tapband?**

    In NLWeb, Tapbands are smart bands with the following features:

    - **Semi-online**: is able to periodically connect to the internet (e.g., Bluetooth, eSim); 
    
    - 💍 **Userable**: emulates a passive NFC [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) representing a [Userable 💍](<../74 💍 Brand Userables/01 💍 Userable thing.md>) [Thing 💠](<../71 💠 Brand Things/01 💠 Thing.md>);
    
    - 🔒 **Keyholder**: has an active NFC scanner to interact with [Padlocks 🔒](<../75 🔒 Brand Padlocks/01 🔒 Padlock device.md>);
    
    - 💖 **Health monitoring**: optionally, collects metrics from the user's device to send to a [Timeline 🕓](<../../30 🫥 Agents/90 🕓 Timeline/01 🕓🗄️ Timeline agent.md>).

    ---

1. **How do Tapbands save battery on NFC?**

    Tapbands use an active NFC scanner with a standby mode - that saves the scanner's energy until it comes into contact with a passive NFC. 

    ---

1. **How do Tapbands connect to the internet?**

    Typically, Tapbands connect to internet via Bluetooth or a mobile internet (e.g., 5G).

    ---

1. **How do Tapbands save battery on internet connections?**

    Tapbands cache the key rotations periodically, so they don't need to be constantly connected to the internet:
    - **on Bluetooth**: the Tapband syncs on connecting, then periodically every hour while connected;
    - **on mobile internet**: the Tapband uses an eSim (i.e., electronic virtual SIM card) that is disconnected most of time, waking up every one hour to synchronize then going disconnecting again.

    ---
