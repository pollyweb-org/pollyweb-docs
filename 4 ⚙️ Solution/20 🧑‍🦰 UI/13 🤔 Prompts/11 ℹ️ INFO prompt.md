# Non-blocking info ℹ️ ⓘ

> Part of [Non-blocking status prompts 🤔](<10 Non-blocking status.md>)

<br/>

1. **What is a non-blocking info?**

    This is an informative [Prompt 🤔](<01 🤔 Prompt.md>) that does not require the user input.

    ---
    <br/>

1. **How do INFO emojis work?**
   
    |Emoji | Details
    |-|-
    ℹ️ | The strong info emoji ℹ️ represents the chat's [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>);
    ⓘ | The faded info emoji ⓘ represents other domains that have been pulled into the [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) - e.g.: <br/>• a user's [Agent 🫥 vault](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>), or <br/>• a [Helper 🛠️ domain](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that was  [invited ⏩](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite.md>) by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>).

    ---
    <br/>



1. **What's an example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Simple info.
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ⓘ Info from an agent.
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ⓘ Info from a guest.
    

    ---
    <br/>


2. **What's an expandable example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Collapsed details [+]
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Expanded details [-]<br/>- long text  <br/>- full of details
    |

    Usage examples:
    * [Finder 🔎 vault](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>)
    * [Book restaurant table online 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

    ---
    <br/>

3. **What's an example with non-blocking options in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ With options:<br/>- [ Cancel ] later <br>- [ Play ] music | > Cancel
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 I'm blocking, but  did <br/>   you that you can still<br/>   go back and cancel? <br/> - [ Yes, I did ] <br/> - [ No, I didn't ]

    Usage examples:
    * [Driver pick-up on pizza delivery 🛵](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/82 🛵 Driver: Pick-up.md>)

    ---
    <br/>


5. **What are business cases?**

    |Category|Use case
    |-|-
    |`Options`|

    ---
    <br/>


1. **What's the format for a [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>)?**

    ```yaml
    INFO|<message>|<options> >> <key>
    ```
    * Options are optional, comma separated (e.g., `Erase, Duplicate`)

    

    |Parameter|Details
    |-|-
    | `message` | 
    | `options` | List of options (optional)
    | `key`     | Stores the answer with this key
    ---
    <br/>

2. **What's an example of a [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>)?**

    ```yaml
    INFO|{item}|Details,Remove >> option
    ```

    ---
    <br/>

3. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    
    ```

    ---
    <br/>

4. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    
    ```