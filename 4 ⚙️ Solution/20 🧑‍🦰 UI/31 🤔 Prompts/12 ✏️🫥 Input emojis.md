> Part of [✏️ Input prompts](<11 ✏️ Input behavior.md>)

1. **How do emojis work?**

    Most (but not all) inputs work with the following emojis.

    Emoji | Behavior
    |-|-
    😃 | The happy emoji 😃 represent the chat's [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>).
    🫥 | The faded emoji 🫥 represents other domains that have been pulled into the chat. These can be either a user's [Agent 🫥 vault](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) or a [Helper 🛠️ domain](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that was [invited ⏩](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>) by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>).

    ---
    <br/>


1. **How to implement emotions?**

    The `😃` emoji can be replaced with one of the following.

    ||Emoji | Application
    |-|-|-
    || 😐 | Neutral
    || 😕 | Confused, sad
    || 🥺 | Pleading face
    || ✏️ | Form input field
    |


    On a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>):

    ```yaml
    CONFIRM|Are you OK? >> $status:
        Emoji: 😕
    ```
    
    On the [Prompted@Host 🚀](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method:

    ```yaml
    Format: CONFIRM
    Message: Are you OK?
    Emoji: 😕
    ```

    ---
    <br/>
