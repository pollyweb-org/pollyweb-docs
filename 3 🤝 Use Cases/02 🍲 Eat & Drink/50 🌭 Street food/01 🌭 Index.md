# 🌭 Eat street food  `index`

> Part of [🍲 Eat & Drink use cases](<../🍲 Eat & Drink index.md>)


<br/>

## 💬 Chats

| Persona  | [Chat 💬](<../../../4 ⚙️ Solution/35 💬 Chats/💬 Chats/💬 Chat.md>) | [Agents 🫥](<../../../4 ⚙️ Solution/50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>)
|-|-|-
|🧑‍🦰 `🎪 Stall`|[Buy hot dog 🌭](<21 🎪 Stall: Buy hot dog 🌭.md>) | [`🧚 Curator`](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) [`🧢 Persona`](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>)   [`💳 Payer`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) 
||[Cancel hot dog 🌭](<22 🎪 Stall: Cancel hot dog.md>) | [`💳 Payer`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) 
||[Cancelled chips 🥔](<23 🎪 Stall: Cancelled chips 🥔.md>) | [`💳 Payer`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) 
||[Receive hot dog 🧑‍🍳](<24 🎪 Stall: Receive hot dog.md>) | [`💖 Vitalogist`](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Vitalogists 💖/💖🫥 Vitalogist agent.md>) 
||[Pay after 💳](<31 🎪 Stall: Pay after 💳.md>) | [`💳 Payer`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) 
|`🧑‍🍳 Staff`|[Start shift 🪪](<91 🧑‍🍳 Chef: Start shift 🪪.md>) | [`🎫 Token`](<../../../4 ⚙️ Solution/30 🧩 Data/Tokens 🎫/🎫 Token.md>) [`🆔 Identity`](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>)
||[Serve 🌭](<92 🧑‍🍳 Chef: Serve 🌭.md>)
||[Bill wallet 💳](<93 🧑‍🍳 Chef: Bill wallet 💳.md>) | [`🏦 Collector`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>)
||[Bill userable 💍](<94 🧑‍🍳 Chef: Bill userable 💍.md>) | [`🏦 Collector`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) [`💳 Payer`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) 
|`💼 Business` | [Menu](<11 🏢 Owner: Menu.md>) | [`Editor 🧑‍💻`](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Editors 🧑‍💻/🧑‍💻🫥 Editor agent.md>)
|

<br/>

## 🧑‍🦰 Customer Setup

1. **What [Agent 🫥 vault domains](<../../../4 ⚙️ Solution/50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) do customers need?**

    |  Agent| Purpose
    |-|-
    |🔎 [Finder](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) | Feedback on the business.
    |🧚 [Curator](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | Filter options for the business.
    | 🧢 [ Persona](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>) | Share the user's social name.
    | 💳 [Payer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | Pays for the food.
    | 💖 [Vitalogist](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Vitalogists 💖/💖🫥 Vitalogist agent.md>) | Registers the food intake.
    | 🧳 [Custodian](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Custodians 🧳/🧳🫥 Custodian agent.md>) | To pay with a [💍 Userable](<../../../4 ⚙️ Solution/25 🔆 Locators/Userables 💍/💍💠 Userable thing.md>).
    |

    <br/>

## 💼 Business Setup


1. **What [Agent 🫥 vault domains](<../../../4 ⚙️ Solution/50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) does staff need?**

    |  Agent| Purpose
    |-|-
    [🆔 Identity](<../../../4 ⚙️ Solution/50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>) | To verify the [staff Token 🎫](<../../../4 ⚙️ Solution/30 🧩 Data/Tokens 🎫/🎫 Token.md>).
    |

    
    <br/>

1. **What are the [domain Roles🎭](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain.md>) required?**

    | [Role 🎭](<../../../4 ⚙️ Solution/40 👥 Domains/👥 Domain.md>) | Purpose
    |-|-
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | To manage the [Chats 💬](<../../../4 ⚙️ Solution/35 💬 Chats/💬 Chats/💬 Chat.md>).
    | [💵 Seller](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>) | To charge for the products.
    | [💼 Consumer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | To verify minimum age.
    |


    <br/>

1. **What are the [domain Helpers 🤲](<../../../4 ⚙️ Solution/45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) required?**
   
    | [Helper 🤲](<../../../4 ⚙️ Solution/45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | Purpose
    |-|-
    | [🏦 Collector](<../../../4 ⚙️ Solution/45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>) | To collect the amount paid.
    |

    <br/>


1. **What does the [domain Manifest 📜](<../../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest.md>) look like?**

    ```yaml
    About:
      Domain: any-street-food.com
      Name: Any Street Food
    ```
    
    <br/>