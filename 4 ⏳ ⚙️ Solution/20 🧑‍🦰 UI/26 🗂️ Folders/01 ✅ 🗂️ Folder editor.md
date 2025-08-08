🗂️ Folder editor FAQ
===

1. **What is an NLWeb Folder editor?**

    Folder editors are desktop apps designed to concentrate into a single editor the CRUD datasets from multiple user [Vaults 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>).

    ---

1. **Why not using wallets for editing CRUD datasets?**

    While possible, the small screens of wallets don't provide a good experience to write big text properties (editors) nor dataset items with many properties.

    ---

1. **What are the benefits for businesses?**

    Businesses don't need to maintain a website for users to edit their datasets. 
    - Only an API is required.

    ---

1. **How can users start using a folder editor?**

    On the editor's desktop app, users scan the editor's [Locator 🔆](<../22 ✅ 🔆 Locators/01 ✅ 🔆 Locator.md>) with their [Wallets 🧑‍🦰](<../01 ✅ 🧑‍🦰 Wallets/01 ✅ 🧑‍🦰 Wallet app.md>).

    ---

1. **How can users bind a vault to the editor?**

    With their wallets:
    - editors ask users to share a CRUD [Vault 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>),
    - then connect to the vault's CRUD API.

    ---

1. **How can users edit a vault's dataset?**

    On the editor. 
    - Users list the connected [Vaults 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>), then select the intended dataset from the vault. 
    - On the list of dataset items, users perform typical CRUD operations.

    ---

1. **How do editors render and verify the rules of dataset item?**

    [Vaults 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>) share the list of the user datasets on their CRUD API, as well as the schema of each dataset. 

    ---

1. **Is there data corruption if editors don't comply dataset rules?**

    No. [Vaults 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>) re-check the rules on their side when receiving write requests.

    ---

1. **How are complex rules shared with editors?**

    They are not. 
    - Complex rules that required cross validation between multiple fields (e.g., password confirmation must match the password) are validated by the CRUD API only. 
    - On each field validation event (e.g., textbox exit), editors send the entire item payload for pre-validation on the API, then render the validation errors to the user.

    ---

1. **Can datasets have list properties referencing other datasets?**

    Yes. Options are:
    - Another dataset on the same [Vault 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>).
    - A dataset on another connected [Vault 🗄️](<../24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>).
    - A public paid [🪣 Dataset](<../23 ✅ 💬 Chats/05 ✅ 🪣🎭 Dataset role.md>) (vaults pay, not editors).

    ---

1. **Is the user's data stored on the editor?**

    No. Only wallet locators and their connected vaults.

    ---
