🆔 Identity palm vein scans FAQ
===

1. **Why use palm vein scanners instead of cameras?**

    [🖐️ Palm scanners](<../../60 ⏳ 🧰 Edge/63 ✅ 🖐️ Palmists/01 ✅ 🖐️🔌 Palmist device.md>) have the following advantages:
    - **Legal restrictions:** some jurisdictions don't allow for the collection of users' photos, except when done by public services.
    - **Privacy protection:** palm scanners prevent [💼 Consumers](<../../20 ✅ 🧑‍🦰 UI/25 ✅ 💼 Consumers/04 ✅ 💼🎭 Consumer role.md>) from cross referencing the user's selfie with photos on the internet (e.g., social media).
    - **Anonymity choice:** a public figure may chose to keep their glasses, scarf, or hat on to avoid being recognized in public.
    - **Cultural and religious choices:** some clothing may cover the face (e.g., niqab, balaclava, burqa).
    - **Technical practicality:** it's easier to install a fixed palm scanner, then a moving camera that needs to adjust to the person's height.

    ---
    
1. **How to implement palm vein scanners on AWS?**

    ![](<./00 ✅ 📎 Assets/🆔 Palm Scan @AWS.png>)

    Identity domains rely on the following components for domain [📨 Messaging](<../../40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>):
    - 📨 **Inbox**: the combination of the Distributer plus the Endpoint;
    - 📮 **Async Post**: an async message outbound that signs messages.

    ---
    