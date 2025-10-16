🧑‍🦰 Wallet QR scan ✨
===

1. **How can website developers render an NLWeb QR?**

    Website developers can use NLWeb's proxy at `nlweb.org/go`;
    - e.g., a [Locator 🔆](<../🔆 Locator.md>)Locator `XPTO` is defined as an HTML image with source `https://nlweb.org/go/XPTO`. 
    
    If in a mobile web browser, the proxy renders a button; 
    - if not in a mobile browser, it renders a QR image;
    - buttons and QR images contain links to the `nlweb.org/go` proxy.

    ---
    <br/>

1. **How do Wallet apps scan an NLWeb QR?**

    An NLWeb QR contains a redirect URL starting with `https://nlweb.org/go/`. 
    
    * When a user scans the QR with an NLWeb Wallet app, the Wallet reads the [Locator 🔆](<../🔆 Locator.md>) from the URL and opens a chat with the Locator's [Host 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>).


    ---
    <br/>

1. **What if users use the default QR reader instead?**

    If a user with an NLWeb [Wallet app 🧑‍🦰](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) installed decides to use the mobile device's default QR scanner instead (e.g., Google Lens in Android) then a web browser opens the NLWeb HTTPS proxy (e.g., `https://nlweb.org/go/ABC`), which in turn redirect to a `nlweb` URL, signaling the OS to open the Wallet - the Wallet then opens with a chat to the QR's [Host 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>). 
    - Wallets should identify this redirect and educate users to prefer using the Wallet to perform the QR scan.


    ---
    <br/>

1. **What if users without a Wallet scan a QR?**

    If a user doesn't have an NLWeb [Wallet app 🧑‍🦰](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) installed and scans an NLWeb QR with the mobile device's default QR scanner (e.g., Google Lens in Android) then a web browser will open on `https://nlweb.org/install` educating the user to find and install a compatible NLWeb app. 

    ---
    <br/>

1. **What's NLWeb view on entitlement QR codes?**

    NLWeb is generally against entitlement QR codes;

    - these are one-time QR codes that customers need to present to other users or machines to prove entitlement;
    - example #1: an online-store may ask customers to present a one-time pick-up QR code upon delivery by the courier, to prove that the entitlement of the recipient to receive the package;
    - example #2: an online-store locker asks customers to present their collection QR to open the corresponding locker door;
    - example #3: boarding passes for flights, which need to be presented at airport gates.

    The referred QR presentation is either done by scanning the customer's smartphone screen, or a customer QR printed in a paper;
    
    - e.g., when traveling, a customer with a broken screen will have trouble reading the QR code, raising anxiety when catching a return flight after breaking the phone screen during holidays, and requiring the customer to get a printed version of the ticket at the airport;
    - customers with a working phone may also face difficulties, with QR scanners unable to read QR codes from low-light and/or auto-rotating screens;
    - often, well-intended airport security personal take the phone out of the customer's hand to scan the QR on their behalf, raising the risk of dropping and breaking the phone.
  
    On NLWeb, QR codes are to be scanned by customers, not businesses;
    - i.e., apart from rare exceptions where two [Wallets 🧑‍🦰](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) are co-operating, users are not required present a QR.

    ---
    <br/>

1. **What's NLWeb view on pin codes for entitlement?**

    NLWeb generally advocates for simple pin codes for entitlement;

    - these are short strings off letters and numbers for confirming a previous step;
    - they also commonly referred as "one-time passwords", or OTPs;
    - examples include:
        - receiving a package after submitting an order;
        - dynamic one-time passwords when logging into a website.

    Simple pin codes should be use for the customer benefit:

    - there's no need for complex pins after the user has already provided some sort of token or confirmation;
    - regarding deliveries, it's common for customers to share these pins to the household, as when ordering pizza or receiving a package at home;
    - consider the following examples:
        - Google uses 3 pairs of 2-digit numbers when confirming an authentication after asking the user of they are the one performing the authentication, asking the user to select one of the 3 pair for confirmation;
        - Visa uses 4-digit pins on credit cards, after the user has presented the card to the card-reader machine;
        - Uber Eats deliverers asks for a 4-digit pin on food delivery;
        - Uber allows for car drivers to ask for a 4-digit pin for night rides if the user has set up that security feature;
        - The national mail delivery in Portugal requires a 4-digit pin when delivering packages from Amazon.

    Conversely, NLWed advocates for biometric confirmation when the entitlement is done to a particular person, and only to that person;

    - pin codes don't fit this requirement because they can be easily shared with anyone else; 
    - for example, a child will be able to by alcohol on vending machine by scanning their parent's identification document, if only requested to provide their parent's pin as confirmation.

    Note that NLWeb does not enforce the usage of pins and biometric validation for entitlement confirmation;
    - i.e., the choice to use pins and/or biometrics falls into the custom defined workflow of each business;
    - NLWeb does provide [Chat 💬 prompts](<../../../35 Chats/12 💬 Chats/💬 Chat.md>) to render OTPs and face scans;
    
    Consider the following workflow examples with pin usage:
    <!-- TODO: add examples -->

    ---
    <br/>

1. **How can businesses protect users from fake QRs?**
    
    Businesses can protect users from fake QRs with visual queues that are hard for bad actors to replicate or replace - e.g.:
    - big QR codes integrated into to a shop's top banner, 2 meters high;
    - screen-based QR codes, integrated into physical displays, i.e. TVs;
    - screen-based QR+NFC devices, e.g. [Ephemeral 🦋 devices](<../../../60 🧰 Edge/62 🦋 Ephemerals/03 🦋🔌 Ephemeral device.md>).
    
    ---
    <br/>
