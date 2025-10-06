# ↩️ Talker `EXIT` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's an EXIT flow?**

    An `EXIT` ↩️
    * is a flow [Command ⌘](<10 ⌘ Command.md>) 
    * that leaves a [Procedure ⚙️](<11 ⚙️ Procedure.md>) to another.

    ---
    <br/>





1. **What's the RETURN syntax?**

    ```yaml
    - EXIT|<procedure>:
        - <command-1>
        - <command-n>
    ```

    | Argument| Purpose
    |-|-
    | `<procedure>` | Optional [Procedure ⚙️](<11 ⚙️ Procedure.md>) to exit to.
    | `<command-n>` | Optional [Commands ⌘](<10 ⌘ Command.md>) to run.
    
    ---
    <br/>



1. **What happens after an EXIT?**

    Nothing runs on a [Procedure ⚙️](<11 ⚙️ Procedure.md>) after the `EXIT`.

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ We are at Step 3.
    |
    
    The related [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) is as follows.

    ```yaml
    # 😃 Talker 

    💬 Step1:
    - RUN|Step2
    - FAILURE|Step 1 never fails.
    
    Step2:
    - EXIT|Step3
    - FAILURE|Step 2 also never fails.

    Step3:
    - SUCCESS|We are at Step 3.
    ```

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | ▶️ [RUN](<24 ▶️ RUN flow.md>) | To run Step 2.
    

    ---
    <br/>


