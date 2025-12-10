# 🤗 Host.Appendixes 🪣 table

> About
* Table that holds the content of the [Prompt 🤔](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) appendixes
* It serves the [`Download@Host` 🚀 call](<../../../🤗📨 Host msgs/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 call.md>)

<br/>

## Schema

Here's the [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml
Prefix: Host
Table: Appendixes
Item: Appendix
```

<br/>

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Host.Prompts`](<../../Prompts 🤔 table/🪣 Prompts/🤗 Host.Prompts 🪣 table.md>)

```yaml
Parents: Prompt, Chat
```

<br/>

The [Item 🛢 Cascade](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Cascade.md>) deletes appendixes when the prompt is deleted.

```yaml
Cascade: Prompt
```

<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Asserts:
    AllOf: Content, Prompt, Chat, Type
    UUIDs: Prompt, Chat
    Texts: Content, Type
    Nums: Pages
    Type.IsIn: PNG, JPEG, PDF
    Pages.IsAbove: 0
```
Uses: [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsAbove`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsAbove ⓕ.md>)

<br/>

## Example

Here's an example response from the [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) command.

```yaml
Prompt: <prompt-uuid>
Chat: <chat-uuid>
Type: PNG
Pages: 7    # if type is PDF
Content: <base64>
```