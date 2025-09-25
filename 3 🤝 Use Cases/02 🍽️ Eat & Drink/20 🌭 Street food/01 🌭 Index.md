# 🌭 Eat street food  `index`

<br/>

## 💬 Chats

| Persona  | Chat 💬 | Details
|-|-|-
|`💼 Business` | [Menu](<11 🏢 Owner: Menu.md>) | [`🗂️ Folder`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/26 🗂️ Folders/01 🗂️ Folder editor.md>)
|
|`🧑‍🦰 Customer`|[Buy hot dog 🌭](<21 🎪 Stall: Buy hot dog 🌭.md>) | [`🧚 Curator`](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) [`🧢 Persona`](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>)   [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) 
||[Cancel hot dog 🌭](<22 🎪 Stall: Cancel hot dog.md>) | [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) 
||[Cancelled chips 🥔](<23 🎪 Stall: Cancelled chips 🥔.md>) | [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) 
||[Receive hot dog 🧑‍🍳](<24 🎪 Stall: Receive hot dog.md>) | [`💖 Vitalogist`](<../../../4 ⚙️ Solution/30 🫥 Agents/09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) 
||[Pay after 💳](<31 🎪 Stall: Pay after 💳.md>) | [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) 
|
|`🧑‍🍳 Staff`|[Start shift 🪪](<91 🧑‍🍳 Chef: Start shift 🪪.md>) | [`🎫 Token`](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) [`🆔 Identity`](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>)
||[Serve 🌭](<92 🧑‍🍳 Chef: Serve 🌭.md>)
||[Bill wallet 💳](<93 🧑‍🍳 Chef: Bill wallet 💳.md>) | [`🏦 Collector`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>)
||[Bill userable 💍](<94 🧑‍🍳 Chef: Bill userable 💍.md>) | [`🏦 Collector`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) 
|

<br/>

## 🧑‍🦰 Customer Setup

1. **What [Agent 🫥 vault domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) do customers need?**

    |  Agent| Purpose
    |-|-
    |🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | Feedback on the business.
    |🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | Filter options for the business.
    | 🧢 [ Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | Share the user's social name.
    | 💳 [Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | Pays for the food.
    | 💖 [Vitalogist](<../../../4 ⚙️ Solution/30 🫥 Agents/09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>) | Registers the food intake.
    | 🧳 [Custodian](<../../../4 ⚙️ Solution/70 🌳 Ambient/71 💠 Brand Things/05 🧳🗄️ Custodian vault.md>) | To pay with a [💍 Userable](<../../../4 ⚙️ Solution/70 🌳 Ambient/74 💍 Brand Userables/01 💍 Userable thing.md>).
    |

    <br/>

## 💼 Business Setup


1. **What [Agent 🫥 vault domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) does staff need?**

    |  Agent| Purpose
    |-|-
    [🆔 Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | To verify the [staff Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).
    |

    
    <br/>

1. **What are the [domain Roles🎭](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) required?**

    | [Role 🎭](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | Purpose
    |-|-
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) | To manage the [Chats 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>).
    | [💵 Seller](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | To charge for the products.
    | [💼 Consumer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | To verify minimum age.
    |


    <br/>

1. **What are the [domain helpers 🛠️](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) required?**
   
    | [Helper 🛠️](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | Purpose
    |-|-
    | [🏦 Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | To collect the amount paid.
    |

    <br/>


1. **What does the [domain Manifest 📜](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) look like?**

    ```yaml
    Identity:
      Domain: any-street-food.com
      Name: Any Street Food
    ```
    
    <br/>