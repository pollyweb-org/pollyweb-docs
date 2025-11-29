<!-- TODO -->
# 🈯 Talker `TRANSLATE` command

## FAQ


1. **What's the TRANSLATE command?**

    The `TRANSLATE` command translates texts from one language to another using the [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 📃 handler.md>).

    ---
    <br/>

1. **What's the syntax of TRANSLATE?**

    ```yaml
    TRANSLATE >> $translation:
        From: en-us     # Defaults to $.Script.Language
        To: pt-br       # Defaults to $.Chat or $.Msg
        Text: Any ´don't translate´.       # Optional
        Schema: $schema                    # Optional
        Schemas: [$schemas]                # Optional
        Domain: $domain                    # Optional
        Domains: [$schemas]                # Optional
    ```

    Input | Purpose | Example
    |-|-|-
    | `From` | Original language            | `en-us`
    | | Defaults to [`$.Script`](<../../../📃 Holders 🧠/System holders 🔩/$.Script 📃/📃 $.Script 🧠 holder.md>)`.Language`
    | `To`   | Destination language         | `pt-br`
    | | Defaults to [`$.Chat`](<../../../📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)`.Language` | 
    | | Or to [`$.Msg`](<../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)`.Language`
    | `Text` | Text to translate via [`.Translate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>) | `Hi, ´John´!`
    |       | Doesn't translate between `´´`
    | `Domain` | Domain for [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | `any-domain.dom`
    | `Schema` | Schema  for [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | `.HOST`

    ---
    <br/>

1. **What are the outputs of TRANSLATE?**

    ```yaml
    ┌─────────────────────┬──────────────────────────────┐
    │ Input               │ Output                       │ 
    ├─────────────────────┼──────────────────────────────┤
    │ - TRANSLATE:        │ Domain:                      |
    │     Domain: any.dom │     Title: Any Domain        |
    │                     |     Description: Bla, bla... │
    ├─────────────────────┼──────────────────────────────┤
    │ - TRANSLATE:        │ Schema:                      |
    │     Schema: any...  │     Title: Any Schema        |
    │                     |     Description: Bla, bla... │
    ├─────────────────────┼──────────────────────────────┤
    │ - TRANSLATE:        │ Domain:                      |
    │     Domain: any.dom │     Title: Any Domain        |
    │     Schema: any...  |     Description: Bla, bla... │
    │                     │ Schema:                      |
    │                     │     Title: Any Schema        |
    │                     |     Description: Bla, bla... │
    └─────────────────────┴──────────────────────────────┘    
    ```

    ---
    <br/>

1. **How to translate a map?**

    Use `All` to translate the properties of a [Map 🧠 holder](<../../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>).

    * Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) excerpt from the [`OnHostPromptInserted` 📃 handler](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🪣 Host tables/Prompts 🤔 table/🪣🔔 11 Inserted/🤗 OnHostPromptInserted 🔔 handler.md>).
    * In this example, `Text` and `Details` are translated directly.
    * Then the `Options` [Set 🧠 holder](<../../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>) is iterated to translate all `Title` fields.
    * All translations are performed with the [`.Translate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>) function.

    ```yaml
    📃 Example: 
    - TRANSLATE|$holder:
        From: en-us
        To: pt-br
        All: Text, Details, Options.Title
    ```

    ---
    <br/>