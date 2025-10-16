# 📝 Talker INFORM command

> Part of [Talker 😃](<../😃 Talker.md>)

> Related to [Host Inform ⏩ flow](<../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>) 

  
<br/>

1. **What is an INFORM message command?**
   
    An `INFORM`
    * is a message [Command ⌘](<../😃⚙️ Talker cmds/10 ⌘ Command.md>) 
    * that informs that a new form is starting
    * by triggering the [Host Inform ⏩ flow](<../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>)
    * and passing the form key in the Host's [Manifest 📜](<../../../40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>).


    ---
    <br/>

1. **What's the INFORM syntax?**

    ```yaml
    INFORM|<key>
    ```

    | Argument| Purpose
    |-|-
    | `<key>` | Form key for [`Form@Graph`](<../../../45 🤲 Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Form.md>)
    

    ---
    <br/>       

1. **What's an example of INFORM?**


    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🤵 [Broker](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
    |

    <br/>

    Here's the [Talker 😃](<../😃 Talker.md>).

    ```yaml
    # Talker
    - INFORM|TableOrder
    ```

    <br/>

    Here's the [Manifest 📜](<../../../40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>).
    ```yaml
    Forms:
      TableOrder:
        Verb: order
        Steps:
          - Code: .CURATOR/FILTER
            Purpose: your curator orders 🧚
          - Code: .PAYER/CHARGE
            Purpose: your payer pays the bill 💳  
    ```

    ---
    <br/>