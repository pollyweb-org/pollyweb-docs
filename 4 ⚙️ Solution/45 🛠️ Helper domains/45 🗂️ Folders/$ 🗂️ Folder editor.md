🗂️ Folder editor
===

1. **What is an NLWeb Folder editor?**

    A Folder 🗂️ editor is a [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) that exposes a desktop app designed to concentrate into a single editor the CRUD datasets from multiple user-bound [Vaults 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>).

    ![alt text](<.📎 Assets/Folder-.png>)

    ---


1. **Why not using wallets for editing CRUD datasets?**

    While possible, the small screens of wallets don't provide a good experience to write big text properties (editors) nor dataset items with many properties.

    ---



1. **What are the benefits for businesses?**

    With Folders 🗂️, businesses that implement a [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) don't need to maintain a website for users to edit their datasets - only an API is required.

    ---



1. **How can users start using a folder editor?**

    On the Folder editor's desktop app, users scan the editor's [Locator 🔆](<../../20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) with their [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) - the interaction is described in [Edit in folder 🗂️💬](<03 🗂️💬 Edit in folder.md>).

    ![alt text](<.📎 Assets/Folder-Login.png>)


    ---



1. **How can users add a vault to the editor?**

    When clicking the "Add Vault" button in the desktop app, the Folder 🗂️ editor initiates a [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) with the user's [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) - the interaction described in [Bind to folder 🗂️💬](<02 🗂️💬 Bind to folder.md>).

    ![alt text](<.📎 Assets/Folder-Flow.png>)

    ---


1. **How can users edit a vault's dataset?**

    On the editor. 
    - Users list the connected [Vaults 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>), then select the intended dataset from the vault. 
    - On the list of dataset items, users perform typical CRUD operations.

    ![alt text](<.📎 Assets/Folder-UX.png>)

    ---


1. **How do editors render and verify the rules of dataset item?**

    [Vaults 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) share the list of the user datasets on their CRUD API, as well as the [Schema 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) of each dataset. 

    ---

1. **Is there data corruption if editors don't comply dataset rules?**

    No. [Vaults 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) re-check the [Schema 🧩](<../../30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) rules on their side when receiving write requests.

    ---

1. **How are complex rules shared with editors?**

    They are not. 

    - Complex rules that required cross validation between multiple fields (e.g., password confirmation must match the password) are validated by the CRUD API only. 
  
    - On each field validation event (e.g., textbox exit), editors send the entire item payload for pre-validation on the API, then render the validation errors to the user.

    ---

1. **Can datasets have list properties referencing other datasets?**

    Yes. Options are:
    - Another dataset on the same [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>).
    - A dataset on another connected [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>).
    - A public paid [🪣 Dataset](<../../41 🎭 Domain Roles/28 🪣 Datasets/$ 🪣🎭 Dataset role.md>) (vaults pay, not editors).

    ---

1. **Is the user's data stored on the editor?**

    No. 
    - Folders 🗂️ only store a references to [Wallets 🔗](<../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>) and [Binds 🔗](<../../30 🧩 Data/20 🔗 Binds/🔗 Bind.md>).

    ---

1. **How are concurrency conflicts resolved?**

    To prevent a Folder 🗂️ from override a change done by another Folder 🗂️ to the same document between the read and the write, Folders 🗂️ use optimistic concurrency.
    
    - When a document is pulled from a [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>), it comes with a version UUID.
    
    - When saving a new version of the document back to the [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>), Folders 🗂️ send the original version.

    - If there's a mismatch between the document version currently stored in the [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) and the original version sent by the Folder 🗂️, then the [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) returns a mismatch error.
  
    - The Folder 🗂️ then cancels the change, reloads the latest version from the [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>), and asks the user to apply the changes again.

    - Smarter Folders 🗂️ may be able to compare and merge the 3 versions (the originally pulled, the changed by the user, and the new version from the [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>)), asking the user to just review the changes with a diff interface before resubmitting.

    ---