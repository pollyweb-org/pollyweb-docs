# 😃📝 Talker `INFORM` command

> Implementation 
 * Part of [Script 📃](<../../📃 basics/Script 📃.md>)
 * Implemented by the [`INFORM` 📃 script](<📝 INFORM 📃 script.md>)

> Purpose
* Related to the [Consumer Inform ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>) 

  
<br/>

## FAQ

1. **What is an INFORM message command?**
   
    An `INFORM`
    * is a message [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that informs that a new form is starting
    * by triggering the [Host Inform ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>)
    * and passing the form key in the Host's [Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).


    ---
    <br/>

1. **What's the INFORM syntax?**

    ```yaml
    INFORM|<form>
    ```

    | Input| Purpose
    |-|-
    | `<form>` | Form key for [`Form@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Form.md>)
    

    ---
    <br/>       

1. **What's an example of INFORM?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
    |

    <br/>

    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    # Talker
    - INFORM|TableOrder
    ```

    <br/>

    Here's the [Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).
    ```yaml
    Forms:
      TableOrder:
        Verb: order
        Steps:
          - Schema: .CURATOR/FILTER
            Purpose: your curator orders 🧚
          - Schema: .PAYER/CHARGE
            Purpose: your payer pays the bill 💳  
    ```

    ---
    <br/>