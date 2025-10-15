# 📝 Talker INFORM command

> Part of [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>)

> Related to [Host Inform ⏩ flow](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/32 💼⏩🧑‍🦰 Inform 📝 flow.md>) 

  
<br/>

1. **What is an INFORM message command?**
   
    An `INFORM`
    * is a message [Command ⌘](<../40 🌊 Talker flows/10 ⌘ Command.md>) 
    * that informs that a new form is starting
    * by triggering the [Host Inform ⏩ flow](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/32 💼⏩🧑‍🦰 Inform 📝 flow.md>)
    * and passing the form key in the Host's [Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).


    ---
    <br/>

1. **What's the INFORM syntax?**

    ```yaml
    INFORM|<key>
    ```

    | Argument| Purpose
    |-|-
    | `<key>` | Form key for [`Form@Graph`](<../../4 ⚙️ Solution/45 🛠️ Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Form.md>)
    

    ---
    <br/>       

1. **What's an example of INFORM?**


    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🤵 [Broker](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
    |

    <br/>

    Here's the [Talker 😃](<../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>).

    ```yaml
    # Talker
    - INFORM|TableOrder
    ```

    <br/>

    Here's the [Manifest 📜](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).
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