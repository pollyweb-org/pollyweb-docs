# 😃📝 Talker `INFORM` command

> Implementation 
 * Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
 * Implemented by the [`INFORM` 📃 script](<📝 INFORM 📃 script.md>)

> Purpose
* Related to the [Consumer Inform ⏩ flow](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>) 

  
<br/>

## FAQ

1. **What is an INFORM message command?**
   
    An `INFORM`
    * is a message [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
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
    | `<form>` | Form key for [`Form@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Form/🕸 Form 🚀 call.md>)
    

    ---
    <br/>     

1. **What's the `Forms` syntax on the [Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>)?**


    ```yaml
    # Comprehensive syntax
    <name>:
        Title: <title>
        Steps:
            - Schema: <schema>
              Purpose: <purpose>          
    ```

    ```yaml
    # Simplified syntax
    <name>: [schemas...]
    ```
    
    The simplified version expects the `Purpose` to be on the [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) definition.

    ---
    <br/>

1. **What's an example of INFORM?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 Ready to order? [Yes, No] <br/> - your curator orders 🧚<br/>  - your payer pays the bill 💳  | > Yes
    

    ---
    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    # Talker
    - INFORM: Order a meal
    ```

    <br/>

    Here's the comprehensive [Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).

    ```yaml
    Forms:
      Order a meal:
        Title: Order a meal
        Steps:
          - Schema: .CURATOR/CURATE
            Purpose: your curator orders 🧚
          - Schema: .PAYER/CHARGE
            Purpose: your payer pays the bill 💳  
    ```

    <br/>

    Here's a simplified version.

    ```yaml
    Forms:
        Order a meal:
          - .CURATOR/CURATE
          - .PAYER/CHARGE
    ```
    
    ---
    <br/>