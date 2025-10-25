# 😃📝 Talker `INFORM` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

> Related to [Host Inform ⏩ flow](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>) 

  
<br/>

1. **What is an INFORM message command?**
   
    An `INFORM`
    * is a message [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) 
    * that informs that a new form is starting
    * by triggering the [Host Inform ⏩ flow](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>)
    * and passing the form key in the Host's [Manifest 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest.md>).


    ---
    <br/>

1. **What's the INFORM syntax?**

    ```yaml
    INFORM|<key>
    ```

    | Argument| Purpose
    |-|-
    | `<key>` | Form key for [`Form@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Form.md>)
    

    ---
    <br/>       

1. **What's an example of INFORM?**


    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🤵 [Broker](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
    |

    <br/>

    Here's the [Script 📃](<../../...commands ⌘/Script 📃/Script 📃.md>).

    ```yaml
    # Talker
    - INFORM|TableOrder
    ```

    <br/>

    Here's the [Manifest 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest.md>).
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