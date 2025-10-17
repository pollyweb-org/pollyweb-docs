🔒 Padlock device
===

1. **What is a Padlock in NLWeb?**

    Padlocks are offline devices (i.e., internet connectivity) that open locks when users use a [🔑 KeyHolder](<../77 🔑 Keyholders/$ 🔑💠 Keyholder device.md>) device to tap on the Padlock.

    ---

1. **How does a Padlock interact with a user?**

    Padlocks use passive NFC emulation to wait for a contact from an active NFC scanner on a [🔑 KeyHolder](<../77 🔑 Keyholders/$ 🔑💠 Keyholder device.md>).

    ![](<. 📎 Assets/🔒 Padlock.png>)

    ---

1. **How does a Padlock decide when to open a lock?**

    Users' [🔑 KeyHolders](<../77 🔑 Keyholders/$ 🔑💠 Keyholder device.md>) first scan the Padlock, receiving an NFC response with Padlock's [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>), which contains:
    - a fixed Padlock [Schema Code 🧩](<../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) identifier 
    - the domain of the Padlock's [🔐 KeyMaker](<../../45 🤲 Helper domains/Keymakers 🔐/05  🔐🏭 Keymaker supplier.md>) (e.g., `any-keymaker.com`) 
    - the resource key of the PadLock in the KeyMaker (e.g.,`padlock-12345678`)
    
    The Keyholder looks up the the Padlock's [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in its local key cache, and sends a new NFC command with the key details:
    - the encrypted security sequence number for the PadLock (e.g., `1234567890`)
    - the encrypted passkey for that sequence number (e.g., `ABCDEF`)
    - the encrypted sequence expiration interval (e.g., 24 hours)

    When a Padlock reads this data, it takes the following steps:
    - decrypt the encrypted fields using the Padlock's private key;
    - confirm if the received sequence if the same of bigger than the last one stored;
    - if the sequence is the same, confirm that it has not expired;
    - if all steps above were successful, then the Padlock opens the lock;
    - sends an NFC response back to the [🔑 KeyHolder](<../77 🔑 Keyholders/$ 🔑💠 Keyholder device.md>) confirming the success and passing the battery status.

    ---

1. **What are examples of Padlock use cases?**

    Uses cases for Padlocks include:
    - standalone padlocks bought on supermarkets;
    - locks integrated into suitcases (e.g., travel bags, safe boxes);
    - locks integrated into furniture (e.g., gym lockers);
    - all types of doors (e.g., residential main and internal doors, hotel rooms);
    - doors and ignition keys for vehicles (e.g., cars);
    - any other scenario requiring an offline short-range unlock.

    ---

1. **Can Padlocks be unlocked against a Token?**

    No.
    - A typical scenario would be a firefighter needing access to any fire fighting material, regardless of what Padlock would be locking it.
    - These scenarios require a [Token 🎫](<../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) and are not supported because Padlocks have no access to the internet, so they cannot verify Tokens.
    - Padlocks can only be unlock by other individuals when the owner explicitly shares the key to the Padlock via their [🌼 Keybox](<../../50 🫥 Agent domains/Keyboxes 🌼/$ 🌼🫥 Keybox agent.md>).
    - Alternatively, organizations should leverage [🎬 Relays](<../../60 🧰 Edge/65 🎬 Relayers/04 🎬🔌 Relay device.md>) to achieve dynamic access control via Tokens.

    ---

1. **How does a Padlock physically opens a mechanical lock?**

    Padlocks may open locks directly (with its own battery) or indirectly (by sending a signal to an external electrical lock).

    ---

1. **How do Padlocks directly open a physical lock?**

    ![](<. 📎 Assets/🔒 Padlock$Briefcase.png>)

    To directly open a lock: 
    - the Padlock uses its power to mechanically move the lock;
    - typical scenarios include [🍏 Branded](<../../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>) transportation bags and gym lockers;
    - if the lock is in a door, then the power may not be enough to move it.

    ---

1. **How do Padlocks indirectly open an external lock?**

    ![](<. 📎 Assets/🔒 Padlock$Door.png>)

    To indirectly open a lock: 
    - the Padlock acts like a relay by sending a low-voltage signal to an external electrical lock, typically connected to the electric grid;
    - locks powered by battery are discouraged because they miss low-power alerts;
    - typical scenarios include residential or office doors and gates, where a [Brand 🍏](<../../41 🎭 Domain Roles/Brands 🍏/🍏🎭 Brand role.md>) assembles and sells a door kit that is installed by a professional builder.

    ---

1. **When does a Padlock considers a sequence expired?**    

    NLWeb advocates for 24 horas, although [🔐 KeyMakers](<../../45 🤲 Helper domains/Keymakers 🔐/05  🔐🏭 Keymaker supplier.md>) may define different intervals or allow Padlock owners to set their own expiration interval.

    ---

1. **What does a Padlock store?**

    Padlocks keep data in two memories: 
    - 1/ a read only set by the manufacturer, and
    - 2/ a non-volatile writable memory that survives survives power loss (e.g., NVRAM, FRAM).

    In readonly memory, a Padlock stores factory settings set by the [🔐 KeyMaker](<../../45 🤲 Helper domains/Keymakers 🔐/05  🔐🏭 Keymaker supplier.md>):
    - the domain of the KeyMaker (e.g., `any-keymaker.com`)
    - the resource key of the Padlock in the KeyMaker (e.g., `padlock-12345678`)
    - the private certificate of the Padlock.
    - the rotation rules of the Padlock.

    In non-volatile writable memory, a Padlock stores dynamic data sent by [🔑 KeyHolders](<../77 🔑 Keyholders/$ 🔑💠 Keyholder device.md>):
    - the last received sequence,to avoid replay attacks (e.g., `1234567890`);
    - the timestamp of last received sequence, to expire the sequence after a while;
    - the sequence expiration interval (e.g., 24 hours).

    ---

1. **How is a Padlocks powered?**

    Padlocks can use one of the following power sources:
    - a replaceable battery (e.g., LR44, 357, CR2032, AAA);
    - a fixed rechargeable battery (e.g., USB, DC, solar, Qi, inductive)

    ---

1. **How do Padlocks report on low battery ?**

    Padlocks  use the following mechanisms for alerting on low-power:
    - 1/ when opening a lock, Padlocks notify their [🔐 KeyMaker](<../../45 🤲 Helper domains/Keymakers 🔐/05  🔐🏭 Keymaker supplier.md>) via the user's [🔑 KeyHolder](<../77 🔑 Keyholders/$ 🔑💠 Keyholder device.md>) device;
    - 2/ Padlocks can have a led that blinks on low-power, albeit draining faster.

    ---

1. **How to open a Padlock that stopped working?**

    Padlock owners should have a physical key:

    - if the Padlock is a relay to an external lock (e.g., building door), then the external lock should have its own traditional key.

    - if the Padlock has an integrated lock (e.g., gym locker), then it was sold with a traditional key as a backup mechanism - this keys come with an embedded [🔆 NFC Locator](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) that users can scan to ask the key's [🔐 KeyMaker](<../../45 🤲 Helper domains/Keymakers 🔐/05  🔐🏭 Keymaker supplier.md>) what the key is for (e.g., `what's the code written in the Padlock of this key?`).

    ---