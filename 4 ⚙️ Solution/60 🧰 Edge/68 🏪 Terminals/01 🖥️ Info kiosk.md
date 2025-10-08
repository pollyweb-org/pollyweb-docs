<!-- #TODO -->

🖥️ Kiosk user experience (UX)
===

![](<00 📎 Assets/🏪 Kiosk.png>)

1. **Can Wallets run as kiosks?**

    Yes. Organizations can use Wallets as kiosks to allow users to interact with touch screens (e.g., McDonald's, Burger King).

    ---

1. **What can users do in kiosk mode?**

    In kiosk mode, Wallets run a video in loop until a user touches the screen. 
    - When touched by a user, the Wallet initiates a new chat in a given fixed Locator.
    - When the chat ends or times out, the Wallet returns to the looping video.

    ---

1. **How to set a Wallet in kiosk mode?**

    On the Host:
    - create a Locator for each of the kiosks;
    - attach a video to the Locators.

    Then, on the kiosk's Wallet app:
    - initiate a chat using one of the Locators above;
    - bind the Wallet to the Host;
    - accept and download the Host's KIOSK Token.

    The Wallet immediately enters in kiosk mode.

    ---

1. **Does it survive device reboots?**

    Yes, assuming that the admin has set the Wallet app to start automatically when the device's operating system boots. 
    
    When the Wallet app starts, it automatically enters the kiosk mode if the Token hasn't been revoked by the Host.

    ---

1. **Does it support payments, coupons, and loyalty cards?**

    Yes, see Custodian domains for details.

    ---
