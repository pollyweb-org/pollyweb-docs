<!-- TODO: replace call links -->

# 😃 Talker
<!-- https://quip.com/J24GAMbu7HKF/-Talker -->

> Implemented by [Hoster ☁️ helper domain](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>)

<br/>

1. **What is a Talker?**

    [Talkers 😃](<10 😃 Talker.md>) 
    * are YAML scripts to render dialogs in a [💬 Chat](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)
    * structured as [Commands ⌘](<../40 🌊 Talker flows/10 ⌘ Command.md>) grouped in [Procedures ⚙️](<../40 🌊 Talker flows/11 ⚙️ Procedure.md>)
    * referencing [{Functions} 🐍](<../30 🗃️ Talker data/12 🐍 {Function}.md>) evaluated by [Hosted 🧑‍💻 domains](<../90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>)
    * and implemented by [Hoster ☁️ helper domains](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>).
    ---
    <br/>

1. **Why are Talkers important?**

    [Talkers 😃](<10 😃 Talker.md>) dramatically reduce the time to build [Host 🤗 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

    * They allow [Hoster ☁️ helper domains](<../90 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) to manage the workflow state on behalf of [Host 🤗 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>), removing the undifferentiated heavy-lifting of handling [Prompts 🤔](<20 🤔 Prompt.md>) communications, and invoking [Host 🤗 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) only when it's necessary to execute business-specific logic.
    ---
    <br/>

1. **What are examples of Talkers?**

    | Example
    |-
    | [🏪 Buy drinks at vending machines](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)
    | [🍕 Order pizza to deliver at home](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)
  

    ---
    <br/>

1. **Coding commands**

    * `💬|<title>:`	
        * Top menu entry - i.e., the "what?"
    * `<procedure>:`   
        * Executable procedure.
    * [`{function}`](<../30 🗃️ Talker data/12 🐍 {Function}.md>)
        * Calculates the value with a function.

  
    ---
    <br/>

    
1. **What flows are initiated by Talkers?**

    |Flow|Details
    |-|-
    | [😃⏩🧑‍💻 Handle 🐍](<../../5 ⏩ Flows/79 😃⏩ Talkers/20 😃⏩🧑‍💻 Handle 🐍.md>) | Ask [Hosteds 🧑‍💻](<../../9 😃 Talkers/90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>) to handle [{Functions} 🐍](<../../9 😃 Talkers/30 🗃️ Talker data/12 🐍 {Function}.md>)
    | [😃⏩🧑‍💻 Wait ⏸️](<../../5 ⏩ Flows/79 😃⏩ Talkers/30 😃⏩🧑‍💻 Wait ⏸️.md>) | Allow [Hosted 🧑‍💻](<../../9 😃 Talkers/90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>)  long-running tasks
    
    ---
    <br/>

    

1. **What API methods do Talkers expose?**

    |Method|Details
    |-|-
    | 🧑‍💻🚀 [Placed](<../../6 🅰️ APIs/92 😃🅰️ Talker/10 🧑‍💻🚀😃 Placed.md>) | Returns the value of a [$placeholder 💾](<../30 🗃️ Talker data/10 💾 $Placeholder.md>)
    | 🧑‍💻🐌 [Place](<../../6 🅰️ APIs/92 😃🅰️ Talker/20 🧑‍💻🐌😃 Place.md>) | Sets the value of a [$placeholder 💾](<../30 🗃️ Talker data/10 💾 $Placeholder.md>)
    | 🧑‍💻🐌 [Handled](<../../6 🅰️ APIs/92 😃🅰️ Talker/40 🧑‍💻🐌😃 Handled.md>) | Receives the evaluation of a [{Function} 🐍](<../30 🗃️ Talker data/12 🐍 {Function}.md>)
    

    ---
    <br/>
    