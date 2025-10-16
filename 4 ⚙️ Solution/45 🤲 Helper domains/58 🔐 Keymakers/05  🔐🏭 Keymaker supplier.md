🔐 Keymaker domain
===

![](<../../70 🌳 Ambient/75 🔒 Padlocks/. 📎 Assets/🔒 Keymaker.png>)

1. **What is a Keymaker domain helper?**

    Keymakers 🔐 are [Suppliers 🏭](<../../41 🎭 Domain Roles/78 🏭 Suppliers/$ 🏭🎭 Supplier role.md>) that supply and manage the lifecycle of [Padlocks 🔒](<../../70 🌳 Ambient/75 🔒 Padlocks/$ 🔒 Padlock device.md>) on behalf of [Brands 🍏](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>).

    ---

1. **What is the commitment of Keymakers to Brands?**

    When supplying [Padlocks 🔒](<../../70 🌳 Ambient/75 🔒 Padlocks/$ 🔒 Padlock device.md>) to [Brands 🍏](<../../41 🎭 Domain Roles/20 🍏 Brands/$ 🍏🎭 Brand role.md>), Keymakers 🔐 commit to manage the following features for an agreed time period (e.g., 10 years, forever):
    - accept registrations from [🌼 Keyboxes](<../../50 🫥 Agents/48 🌼 Keyboxes/$ 🌼🫥 Keybox agent.md>);
    - continuously rotate the Padlock's key;
    - continuously propagate the Padlock's battery status.

    ---

1. **What happens when a Keymaker's commitment ends?**

    The [Padlock 🔒](<../../70 🌳 Ambient/75 🔒 Padlocks/$ 🔒 Padlock device.md>) won't unlock anymore, unless the a physical backup key is used.

    ---

1. **Are Padlock's key rotations encrypted in transit?**

    Yes.
    * Both the sequence and the passkey are encrypted using the [Padlock 🔒](<../../70 🌳 Ambient/75 🔒 Padlocks/$ 🔒 Padlock device.md>)'s public key, so that only the [Padlock 🔒](<../../70 🌳 Ambient/75 🔒 Padlocks/$ 🔒 Padlock device.md>) is able to read them using its private key. 
    * Only the Keymaker 🔐 has the public key of the Padlock.

    ---
