## 🏪 Drink at vending machines  `index`

![alt text](<.📎 Assets/cartoon.png>)

<br/>

## 💬 Chats

|Persona|Chat 💬|Notes
|-|-|-
| `🧑‍🦰 Customer`|[Buy water 💧](<11 💧 Buy water.md>)  | [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>)
| `🧑‍🦰 Customer` | [Buy beer 🍺 21+ ](<12 🍺 Buy beer.md>)| [`🆔 Identity`](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/03 🆔🫥 Identity agent.md>)  [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) 
||

<!-- 
TODO: other scenarios
  * 21 🏢 Plan route 🗺️.md
  * 22 🏢 Load truck 🚚.md
  * 31 🏪 Stock machine 📦.md
-->

<br/>

## 💼 Business Setup

1. **What does the [😃 Domain Talker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 😃 Talker.md>) look like?**

    ```yaml
    💬|[Buy] an item:
    - INT|What's the item number?
    - CONFIRM|{confirm}     # Map item number to name.
    - IF|{min-21}|share-21  # Ask proof of over 21 if needed.
    - CHARGE|{amount}       # Map item number to price.
    - TEMP|Delivering...    # Active the mechanical delivery.
    - IF|{success}|goodbye|fail  # Block until delivered. 

    share-21:
    - SHARE|nlweb.org/IDENTITY/OVER-21

    goodbye:
    - SUCCESS|Thanks! Pick up your item.
    - GOODBYE

    fail:
    - FAILURE|{failure}
    ```

    |Functions|Returns|Description
    |-|-|-
    |`confirm`| string | Translate from item number to name.
    |`amount`| currency  | Translates the item number to price.
    |`success`| bool | Wait until the item is delivered.
    |`failure`| string | Register the unexpected failure.
    |

    | Schema Codes | Purpose
    |-|-
    | [🧩 nlweb.org/IDENTITY/OVER21](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/IDENTITY/🧩 IdentityOver21.md>) | Verify minimum age to drink.
    |

    
    <br/>

2. **What does the data look like?**

    

    ```yaml
    # 🪣 Items

    | Number | Name          | Price  | 21+
    |--------|---------------|--------|----
    | 123    | Water bottle  | $1.50  |
    | 124    | Beer          | $4.50  | Yes
    | 126    | Sandwich      | $5.00  |
    | 127    | Chocolate bar | $1.00  |
    ```
    
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
      Domain: any-vending.com
      Name: Any Vending
    ```
    
    <br/>

<!--
  1. **What does the [Hoster 🧑‍💻 helper](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/05 🧑‍💻🛠️ Hoster helper.md>)
 -->