# 🔄 QUANTITY prompt

> Part of [blocking input prompts 🤔](<03 Blocking input prompts.md>)


<br/>

1. **What's an QUANTITY prompt?**

    It's a [Prompt 🤔](<01 🤔 Prompt.md>) that shows up and down arrows.

    ---
    <br/>

2. **What's an example of a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Consider the following [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>).
    
    ```yaml
    QUANTITY|How many? >> my-variable
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the code? | `0123`
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 What's the code? | `01234`
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 What's the code? | `000`

    Usage examples:
    * [Book a restaurant table online 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    * [Split the bill at a restaurant ✂️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>)

    ---
    <br/>


2. **How to default quantities in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Consider the following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).


    | Service | Prompt | User
    | - | - | - |
    | 🍽️ Restaurant | ℹ️ Table reservation.
    | 🍽️ Restaurant | 😃 For how many? [1, 2, more] | > more
    | 🍽️ Restaurant | 😃 How many exactly? | 🔢 8
    | 🍽️ Restaurant | ⏳ Checking availability... 
    |

    The corresponding [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>) would be the following.

    ```yaml
    💬 Walk-in:
    - INFO|Table reservation.
    - ONE|For how many?|1,2,more >> qt
    - IF|{three-or-more}|ask-quantity
    - TEMP|Checking availability...
    
    ask-quantity:
    - QUANTITY|How many exactly? >> qt:
        MinValue: 3
        MaxValue: 12
    ```

    Usage examples:
    * [Walk into a full restaurant 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/44 🚪 Door: Walk in full.md>)

    ---
    <br/>

3. **What's the format of a [Talker 😃](<../12 💬 Chats/03 😃 Talker.md>)?**

    ```yaml
    QUANTITY|<message> >> <key>:
        Details: <details>
        MinValue: <min-value>
        MaxValue: <max-value>
        Emoji: <emoji>
    ```
    
    ---
    <br/>


4. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: QUANTITY
    Message: <message>
    Details: <details>
    MinValue: <min-value>
    MaxValue: <max-value>
    Emoji: <emoji>
    ```

    ---
    <br/>

5. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: -123
    ```