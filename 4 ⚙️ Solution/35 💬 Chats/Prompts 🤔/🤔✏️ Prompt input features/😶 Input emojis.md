# 😶 Input emojis

> Part of [✏️ Input prompts](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>)

> Implemented by the [`PromptEmoji` 📃 script](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 📃 emoji.md>)


## FAQ

1. **Are emojis mandatory in inputs?**

    No.

    * Emojis are not specified in the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) message.
        * Thus, [Host 🤗 domains](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) can send simple strings to [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).
  
    * However, NLWeb advocates for emojis.
        * They align with human's non-verbal communication, from wish our brain process the underlying meaning of ambiguous text-only sentences. 
            * e.g., who never misunderstood an ambiguous and apparently threatening text conversation, to  immediately clarify in the first 3 seconds of a follow-up video call with a very friendly 🤗 and joyful 😃 sender on the other end of call?
        * Emojis also reduce brain effort when reading and interpreting text.
            * e.g., `congrats` versus `🥳🎂 congrats 💕`
            * e.g., `that's funny` versus `🤣🤣🤣`
  
    * To help [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) developers, 
        * [Scripts 📃](<../../Scripts 📃/📃 basics/Script 📃.md>) add emojis to [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) messages. 


    ---
    <br/>

1. **How do emojis work on Talkers?**
    
    Most (but not all) [Talker input commands ✏️](<../🤔⚙️ Prompt features/9 ✏️ as Input.md>) work with the following emojis.

    Emoji | Behavior
    |-|-
    😃 | The happy emoji 😃 represent the chat's [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).
    🫥 | The faded emoji 🫥 represents other domains that have been pulled into the chat. These can be either a user's [Agent 🫥 vault](<../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) or a [Helper 🤲 domain](<../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) that was [invited ⏩](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) by a [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

    ---
    <br/>

1. **What's an example of emojis in Talkers?**

    Consider the following [Chat 💬](<../../Chats 💬/💬 Chat.md>).

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Continue? [Yes, No]
    |

    <br/>

    Here's the [Script 📃](<../../Scripts 📃/📃 basics/Script 📃.md>).

    ```yaml
    # 😃 Talker
    - CONFIRM|Continue?
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: CONFIRM
    Emoji: 😃 
    Text: Continue?
    ```

    ---
    <br/>


1. **Can Talker prompts use alternative emojis?**

    The default [Script 📃](<../../Scripts 📃/📃 basics/Script 📃.md>) emoji `😃` can be replaced with one of the following.

    ||Emoji | Application | Example
    |-|-|-|-
    || 😐😶 | Neutral inputs | `Are you OK?`
    || 😌😊 | Calm inputs    | `Thanks! And you?`
    || 😕🙁 | Sad inputs     | `That's odd! Undo?`
    || 😔🥺 | Sorry inputs   | `We failed! Retry?`
    || 🤣😅 | Joyful inputs  | `Likewise! Another?`
    || ✏️ | Form input field | `IP address?`
    |

    The selection is restricted to emojis that can convey empathy:
    * without expressing strong internal emotions,
        * e.g., a machine crying becomes awkward to a human;
    * nor strong external emotions,
        * e.g., an angry machine is not socially acceptable.

    ---
    <br/>

1. **How to replace emojis in Talkers?**

    The replacement can either be:
    * per [Prompt 🤔](<../🤔 Prompt.md>) by setting the `Emoji` parameter,
    * or by default for upcoming [Prompts 🤔](<../🤔 Prompt.md>) with the [`EMOJI`](<😶⌘ EMOJI cmd.md>) command.

    ---
    <br/>

1. **How to change an emoji in a Prompt?**

    Here's a [Script 📃](<../../Scripts 📃/📃 basics/Script 📃.md>).

    ```yaml
    - CONFIRM|Are you OK?:
        Emoji: 😕 
    ```
    
    This translates to the following [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) response.

    ```yaml
    Format: CONFIRM
    Emoji: 😕 
    Text: Are you OK?
    ```

    ---
    <br/>
