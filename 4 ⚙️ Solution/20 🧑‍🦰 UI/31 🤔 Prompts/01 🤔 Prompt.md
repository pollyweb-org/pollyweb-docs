🤔 Prompt FAQ
===

1. **What is a Prompt?**

    A [Prompt 🤔](<01 🤔 Prompt.md>) is 
    * a line in [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) 
    * sent by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) 
    * with a question or information to the user
    * for a [Wallet 🧑‍🦰 app](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to render.

    ---
    <br/>



1. **What input formats can Hosts ask Wallets to render?**

    Similar to HTTP, on NLWeb the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) servers request the [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) to render the requested [Prompts 🤔](<01 🤔 Prompt.md>).

    * The supported [Prompt 🤔](<01 🤔 Prompt.md>) formats are as follow.

    |Behavior| Format 
    |-|-
    |[`Status`](<08 Non-blocking prompts.md>)| [`ℹ️ INFO`](<11 ℹ️ INFO prompt.md>) [`⏳ TEMP`](<12 ⏳ TEMP prompt.md>) [`✅ SUCCESS`](<13 ✅ SUCCESS prompt.md>) [`❌ FAILURE`](<14 ❌ FAILURE prompt.md>)
    |[`Inputs`](<09 Blocking input prompts.md>)| [`🔢 INT`](<21 🔢 INT prompt.md>) [`🔄 QUANTITY`](<21 🔄 QUANTITY prompt.md>) [`💰 AMOUNT`](<22 💰 AMOUNT prompt.md>) [`🔑 OTP`](<21 🔑 OTP prompt.md>) [`⭐ RATE`](<26 ⭐ RATE prompt.md>) 
    || [`👍 CONFIRM`](<24 👍 CONFIRM prompt.md>) [`1️⃣ ONE`](<25 1️⃣ ONE prompt.md>) [`🔢 MANY`](<25 🔠 MANY prompt.md>) 
    || [`🕓 TIME`](<27 🕓 TIME prompt.md>) [`📆 DATE`](<27 📆 DATE prompt.md>) 
    || [`⬆️ UPLOAD`](<51 ⬆️ UPLOAD prompt.md>)
    || [`🔠 TEXT`](<20 🔠 TEXT prompt.md>) 
    || [`👤 IDENTIFY`](<41 👤 IDENTIFY prompt.md>) [`🛒 EAN`](<44 🛒 EAN prompt.md>) [`🔆 SCAN`](<42 🔆 SCAN prompt.md>) [`🦋 TOUCH`](<43 🦋 TOUCH prompt.md>) 
    |`Special`| [`📍 LOCATION`](<61 📍 LOCATION prompt.md>) [`🗺️ TRACK`](<62 🗺️ TRACK prompt.md>)


    ---
    <br/>


1. **Can Hosts replace sent prompts?**

    Yes, but only temporary [Prompts 🤔](<01 🤔 Prompt.md>). 
    - If a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) sends  two consecutive blocking [Prompts 🤔](<01 🤔 Prompt.md>) while the user has not answered the first, then the first becomes readonly and the second becomes the active input.
    - If the [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) wants a [Prompts 🤔](<01 🤔 Prompt.md>) to be visually replaced, then they need to use a temporary [Prompts 🤔](<01 🤔 Prompt.md>), visually represented by an hourglass ⏳ emoji. 
    - This is particularly useful when [preparing food 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/53 🪑 Seat: Change order 🌀.md>), when [waiting food orders 🤝](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/82 🧑‍🍳 Chef: Prepare food 🥘.md>), and when reminding users of [upcoming bookings 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/05 🧳 Travel by hailing 🙋/1 🙋 Customer @ Home 🏠/12 🏠 Book.md>).

    ---
    <br/>

1. **Can users respond to an old prompt?**

    NLWeb [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) are designed to be forward-only workloads managed by a [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) (and not by the user). 
    * This behavior is visible on LLM apps like on ChatGPT, Gemini, and others. 
  
    Just like in the previously referred LLMs, NLWeb also allows [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) to add options in certain steps so that users can go back and change the direction of the workload from a previous step.
    * For example, the user did A, B, C, D, E; then went back to B and changed the history to A, B, X, Y, Z. 
    * This worked because step B had an option set by the [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) that allowed the user to go back and change the workflow path.

    In NLWeb, these option sets can be added only to [non-blocking Prompts 🤔](<08 Non-blocking prompts.md>)
    - The non-blocking prompts include `TEMP ⏳`, `INFO ℹ️`, `SUCCESS ✅`, and [`FAILURE ❌`](<14 ❌ FAILURE prompt.md>).
    - This is particularly helpful when [Host 🤗 domains](<../12 💬 Chats/04 🤗🎭 Host role.md>) want to assign default values to options to speed up the process (e.g., [navigation options 🤝](<../../../3 🤝 Use Cases/03 🧳 Travel/01 🧳 Plans trips 🧭/02 🧭 Return @ Destination.md>)), while still allowing users to go back and change those default options.
    
    ---
    <br/>



1. **What are expandable details?**

    These are additional details that are initially collapsed to users, e.g.:
    * [Finder 🔎 vault](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>)
    * [Book restaurant table online 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
  
    Consider the following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Expandable info [+] | > +
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Expandable info [-]<br/>- long text  <br/>- full of details
    |

    The corresponding [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) would be.
    
    ```yaml
    INFO|Expandable info:
        Details: |
            - long text
            - full of details
    ```

    

    ---
    <br/>



1. **How to attach a file?**

    > This calls [Download@Host 🚀](<../../../6 🅰️ APIs/50 🤗🅰️ Host/06 🧑‍🦰🚀🤗 Download.md>)
    
    Consider the following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) as an example.

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 Who is in the picture? 🖼️ | `Elvis`
    |

    The related [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) would be.

    ```yaml
    TEXT|Who is in the picture?:
        Attachment: {/photos/elvis.png}
    ```
    
    The [Prompted@Host 🚀](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method would be.

    ```yaml
    Format: TEXT
    Message: Who is in the picture?
    Attachment: <attachment-uuid>
    ```

    Usages include the following.
    | Format | Example | 
    |-|-
    | `PDF` | [Show the bill on vending machine payments 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `PNG` | [Show an image of a recovered item in a taxi 🚕](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)

    ---
    <br/>