🧑‍💻 Editor agent
===

1. **What is an NLWeb Editor?**

    An [Editor 🧑‍💻 agent](<🧑‍💻🫥 Editor agent.md>) is a [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) that exposes a desktop app designed to concentrate into a single editor the CRUD datasets from multiple user-bound [Vaults 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>).

    ![alt text](<.📎 Assets/Editor-.png>)

    ---
    <br/>

1. **Why not using wallets for editing CRUD datasets?**

    While possible, the small screens of wallets don't provide a good experience to write big text properties (editors) nor dataset items with many properties.

    ---
    <br/>



1. **What are the benefits for businesses?**

    With [Editor 🧑‍💻 domains](<🧑‍💻🫥 Editor agent.md>), businesses that implement a [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) don't need to maintain a website for users to edit their datasets - only an API is required.

    ---
    <br/>



1. **How can users start using an Editor?**

    On the Editor's desktop app, users scan the editor's [Locator 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) with their [Wallets 🧑‍🦰](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) - the interaction is described in [Edit in folder 🗂️💬](<🧑‍💻💬 Editor chats/🧑‍💻💬 Edit in Editor.md>).

    ![alt text](<.📎 Assets/Editor-Login.png>)


    ---
    <br/>



1. **How can users add a vault to the editor?**

    When clicking the "Add Vault" button in the desktop app, the [Editor 🧑‍💻 agent](<🧑‍💻🫥 Editor agent.md>) initiates a [Chat 💬](<../../35 💬 Chats/💬 Chats/💬 Chat.md>) with the user's [Wallet 🧑‍🦰](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) - the interaction described in [Bind to folder 🗂️💬](<🧑‍💻💬 Editor chats/🧑‍💻💬 Bind to Vault.md>).

    ![alt text](<.📎 Assets/Editor-Flow.png>)

    ---
    <br/>


1. **How can users edit a vault's dataset?**

    On the editor. 
    - Users list the connected [Vaults 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>), then select the intended dataset from the vault. 
    - On the list of dataset items, users perform typical CRUD operations.

    ![alt text](<.📎 Assets/Editor-UX.png>)

    ---
    <br/>


1. **How do editors render and verify the rules of dataset item?**

    [Vaults 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) share the list of the user datasets on their CRUD API, as well as the [Schema 🧩](<../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) of each dataset. 

    ---
    <br/>

1. **Is there data corruption if editors don't comply dataset rules?**

    No. [Vaults 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) re-check the [Schema 🧩](<../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) rules on their side when receiving write requests.

    ---
    <br/>

1. **How are complex rules shared with editors?**

    They are not. 

    - Complex rules that required cross validation between multiple fields (e.g., password confirmation must match the password) are validated by the CRUD API only. 
  
    - On each field validation event (e.g., textbox exit), editors send the entire item payload for pre-validation on the API, then render the validation errors to the user.

    ---
    <br/>

1. **Can datasets have list properties referencing other datasets?**

    Yes. Options are:
    - Another dataset on the same [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>).
    - A dataset on another connected [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>).
    - A public paid [🪣 Dataset](<../../41 🎭 Domain Roles/Datasetters 🪣/🪣🎭 Datasetter role.md>) (vaults pay, not editors).

    ---
    <br/>

1. **Is the user's data stored on the editor?**

    No. 
    - [Editor 🧑‍💻 domains](<🧑‍💻🫥 Editor agent.md>) only store a references to [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) and [Binds 🔗](<../../30 🧩 Data/Binds 🔗/🔗 Bind.md>).

    ---
    <br/>

1. **How are concurrency conflicts resolved?**

    To prevent an [Editor 🧑‍💻](<🧑‍💻🫥 Editor agent.md>) from override a change done by another [Editor 🧑‍💻](<🧑‍💻🫥 Editor agent.md>) to the same document between the read and the write, [Editor 🧑‍💻 domains](<🧑‍💻🫥 Editor agent.md>) use optimistic concurrency.
    
    - When a document is pulled from a [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>), it comes with a version UUID.
    
    - When saving a new version of the document back to the [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>), [Editor 🧑‍💻 domains](<🧑‍💻🫥 Editor agent.md>) send the original version.

    - If there's a mismatch between the document version currently stored in the [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) and the original version sent by the [Editor 🧑‍💻](<🧑‍💻🫥 Editor agent.md>), then the [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) returns a mismatch error.
  
    - The [Editor 🧑‍💻](<🧑‍💻🫥 Editor agent.md>) then cancels the change, reloads the latest version from the [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>), and asks the user to apply the changes again.

    - Smarter [Editor 🧑‍💻 domains](<🧑‍💻🫥 Editor agent.md>) may be able to compare and merge the 3 versions (the originally pulled, the changed by the user, and the new version from the [Vault 🗄️](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)), asking the user to just review the changes with a diff interface before resubmitting.

    ---
    <br/>