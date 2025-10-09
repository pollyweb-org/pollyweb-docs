# ☁️🛠️ Hoster helper

> 

<br/> 

1. **What is a Hoster?**

    A [☁️ Hoster](<05 ☁️🛠️ Hoster helper.md>) is 
    * any [Helper 🛠️ domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)
    * that provides the infrastructure of a [Hosted 🧑‍💻 domain](<10 🧑‍💻☁️ Hosted domain.md>)
    * and allow their owners to manage them with a [Wallet 🧑‍🦰 app](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

    ---
    <br/>


1. **What flows are initiated by Hosters?**

    |Flow|Details
    |-|-
    | [😃⏩🧑‍💻 Handle 🐍](<../../5 ⏩ Flows/79 😃⏩ Talkers/20 😃⏩🧑‍💻 Handle 🐍.md>) | Ask [Hosteds 🧑‍💻](<../../9 😃 Talkers/90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>) to handle [{Functions} 🐍](<../../9 😃 Talkers/30 🗃️ Talker data/12 🐍 {Function}.md>)
    | [😃⏩🧑‍💻 Wait ⏸️](<../../5 ⏩ Flows/79 😃⏩ Talkers/30 😃⏩🧑‍💻 Wait ⏸️.md>) | Allow [Hosted 🧑‍💻](<../../9 😃 Talkers/90 ☁️ Hosters/10 🧑‍💻☁️ Hosted domain.md>)  long-running tasks
    
    ---
    <br/>
    

1. **API Methods?**

    |Method|Details
    |-|-
    | About:chat| Returns info about the Chat.
    | Read(name) | Get the value of a $placeholder.
    | Write(name, value) | Set the value of a $placeholder.
    | Command(yaml) | Send a command.
    | Function(args) | Calculates a built-in function.

    ---
    <br/>
    