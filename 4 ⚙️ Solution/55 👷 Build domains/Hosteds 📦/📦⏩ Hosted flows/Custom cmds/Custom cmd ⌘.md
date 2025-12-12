# 😃⌘ Custom talker `<Command>`

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>


1. **How to create custom commands?**

    |#|Step|Details
    |-|-|-
    |1| `Upload` | Upload the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) for the [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)
    |2| `Parse` | Parse it at the [`Parse@Hosted` 🚀 call](<../../📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 call.md>)
    |3| `Register`| Register it on the [`Commands.yaml` ⌘ file](<../../📦📄 Hosted files/📄⌘ Commands file.md>) 
    

    ---
    <br/>

1. **How to build a custom `ECHO` command?**

    Here's the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [ Test ] my echo | > Test
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 Say something | `Test`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Custom echo `Test`
    |

    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) for the [`Hello@Host` 📨 msg](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Goodbye 🤗⏩👋/🤗 Goodbye ⏩ flow.md>) 

    ```yaml
    💬 /Test my echo:
    - TEXT Say something >> $something
    - ECHO|$something
    ```
    Uses: [`TEXT`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 💭/💭 TEXT ⌘ cmd.md>)

    <br/>

    Here's the `ECHO` [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

    ```yaml
    📃 .ECHO:
    - INFO: Custom echo `{$UserInput}`
    ```
    Uses: [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    <br/>

    Here's the python handler for the [`Parse@Hosted` 🚀 call](<../../📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 call.md>)

    ```python
    def talkerParser(args):
        match args['Command']:
            case 'ECHO':

                # Get the raw input
                #   ECHO|$something
                input_str = args['Input']             

                # Extract the holder
                #   $something
                parts = input_str.split("|", 1)       
                holder = parts[1] if len(parts) > 1 else ""

                # Instruct what to do next
                return {
                    'RUN .ECHO': {
                        'UserInput': holder
                    }
                }
    ```
    Uses: [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)

    ---
    <br/>