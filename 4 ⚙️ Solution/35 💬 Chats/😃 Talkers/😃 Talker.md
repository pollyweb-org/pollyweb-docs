<!-- TODO: replace call links -->

# 😃 Talker
<!-- https://quip.com/J24GAMbu7HKF/-Talker -->

> Implemented by [Hoster ☁️ helper domain](<../../45 🤲 Helper domains/55 ☁️ Hosters/☁️🤲 Hoster helper.md>)

<br/>

1. **What is a Talker?**

    [Talkers 😃](<😃 Talker.md>) 
    * are YAML scripts to render dialogs in a [💬 Chat](<../💬 Chats/💬 Chat.md>)
    * structured as [Commands ⌘](<😃⚙️ Talker cmds/10 ⌘ Command.md>) grouped in [Procedures ⚙️](<😃⚙️ Talker cmds/11 ⚙️ Procedure.md>)
    * referencing [{Functions} 🐍](<😃💾 Talker data/12 🐍 {Function}.md>) evaluated by [Hosted 📦 domains](<../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>)
    * and implemented by [Hoster ☁️ helper domains](<../../45 🤲 Helper domains/55 ☁️ Hosters/☁️🤲 Hoster helper.md>).
    ---
    <br/>

1. **Why are Talkers important?**

    [Talkers 😃](<😃 Talker.md>) dramatically reduce the time to build [Host 🤗 domains](<../💬 Chats/💬 Chat.md>).

    * They allow [Hoster ☁️ helper domains](<../../45 🤲 Helper domains/55 ☁️ Hosters/☁️🤲 Hoster helper.md>) to manage the workflow state on behalf of [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>), removing the undifferentiated heavy-lifting of handling [Prompts 🤔](<../🤔 Prompts/🤔 Prompt.md>) communications, and invoking [Host 🤗 domains](<../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) only when it's necessary to execute business-specific logic.
    ---
    <br/>

1. **What are examples of Talkers?**

    | Example
    |-
    | [🏪 Buy drinks at vending machines](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)
    | [🍕 Order pizza to deliver at home](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)
  

    ---
    <br/>

1. **Coding commands**

    * `💬|<title>:`	
        * Top menu entry - i.e., the "what?"
    * `<procedure>:`   
        * Executable procedure.
    * [`{function}`](<😃💾 Talker data/12 🐍 {Function}.md>)
        * Calculates the value with a function.

  
    ---
    <br/>

    
1. **What flows are initiated by Talkers?**

    |Flow|Details
    |-|-
    | [😃⏩🧑‍💻 Handle 🐍](<😃⏩ Talker flows/20 😃⏩🧑‍💻 Handle 🐍.md>) | Ask [Hosteds 📦](<../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>) to handle [{Functions} 🐍](<😃💾 Talker data/12 🐍 {Function}.md>)
    | [😃⏩🧑‍💻 Wait ⏸️](<😃⏩ Talker flows/30 😃⏩🧑‍💻 Wait ⏸️.md>) | Allow [Hosted 📦](<../../55 👷 Build domains/📦 Hosteds/📦👥 Hosted domain.md>)  long-running tasks
    
    ---
    <br/>

    

1. **What API methods do Talkers expose?**

    |Method|Details
    |-|-
    | 🧑‍💻🚀 [Placed](<😃🅰️ Talker methods/10 🧑‍💻🚀😃 Placed.md>) | Returns the value of a [$placeholder 💾](<😃💾 Talker data/10 💾 $Placeholder.md>)
    | 🧑‍💻🐌 [Place](<😃🅰️ Talker methods/20 🧑‍💻🐌😃 Place.md>) | Sets the value of a [$placeholder 💾](<😃💾 Talker data/10 💾 $Placeholder.md>)
    | 🧑‍💻🐌 [Handled](<😃🅰️ Talker methods/40 🧑‍💻🐌😃 Handled.md>) | Receives the evaluation of a [{Function} 🐍](<😃💾 Talker data/12 🐍 {Function}.md>)
    

    ---
    <br/>
    