<!-- TODO: replace call links -->

# 😃 Talker domain role
<!-- https://quip.com/J24GAMbu7HKF/-Talker -->

> Implemented by [Hoster ☁️ helper domain](<../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>)

<br/>

1. **What is a Talker?**

    [Talkers 😃](<😃 Talker role.md>) 
    * are [domain 👥](<../../40 👥 Domains/👥 Domain.md>) roles
    * implemented by [Hoster ☁️ helper domains](<../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>).
    * to run [Scripts 📃](<😃⚙️ Talker cmds/...commands ⌘/📃 Script.md>) 
    * for the purpose of rendering dialogs in a [💬 Chat](<../💬 Chats/💬 Chat.md>)
    

    ---
    <br/>

1. **Why are Talkers important?**

    [Talkers 😃](<😃 Talker role.md>) dramatically reduce the time to build [Hosted 📦 domains](<../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>).

    * They allow [Hoster ☁️ helper domains](<../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) to manage the workflow state on behalf of [Hosted 📦 domains](<../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>), removing the undifferentiated heavy-lifting of handling [Prompts 🤔](<../🤔 Prompts/🤔 Prompt.md>) communications, and invoking [Hosted 📦 domains](<../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) only when it's necessary to execute business-specific logic.
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
    * `<script>:`   
        * Executable script.
    * [`{function}`](<😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>)
        * Calculates the value with a function.

  
    ---
    <br/>

    
1. **What flows are initiated by Talkers?**

    |Flow|Details
    |-|-
    | [😃⏩🧑‍💻 Handle 🐍](<😃⏩ Talker flows/😃⏩🧑‍💻 Handle 🐍.md>) | Ask [Hosteds 📦](<../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) to handle [{Functions} 🐍](<😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>)
    | [😃⏩🧑‍💻 Wait ⏸️](<😃⏩ Talker flows/😃⏩🧑‍💻 Wait ⏸️.md>) | Allow [Hosted 📦](<../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>)  long-running tasks
    
    ---
    <br/>

    

1. **What API methods do Talkers expose?**

    |Method|Details
    |-|-
    | 🧑‍💻🚀 [Placed](<😃🅰️ Talker methods/🧑‍💻🚀😃 Placed.md>) | Returns the value of a [placeholder 🧠](<😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>)
    | 🧑‍💻🐌 [Place](<😃🅰️ Talker methods/🧑‍💻🚀😃 Place.md>) | Sets the value of a [placeholder 🧠](<😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>)
    | 🧑‍💻🐌 [Handled](<😃🅰️ Talker methods/🧑‍💻🐌😃 Handled.md>) | Receives the evaluation of a [{Function} 🐍](<😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>)
    

    ---
    <br/>
    