<!-- TODO -->
# 🈯 Talker `TRANSLATE` command

## FAQ

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
    | `Domains` | List of domains
    | `Schema` | Schema  for [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | `.HOST`
    | `Schemas` | List of schemas

    ---
    <br/>

1. **What are the outputs of TRANSLATE?**

    |Output| Example
    |-|-|-
    |`Schema` or `Domain` | The translated text | `Any Domain`
    |`Schema` and `Domain`  | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | `{Domain:X, Schema:X}`
    |Other inputs | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>)| `{Domains:[...]}`

    |Object|Property|
    |-|-|-
    |Text   |
    |Domain |`Title`|
    |       |`Description`
    |Schema |`Title`
    |       |`Description`
    |

    ```yaml
    ┌─────────────────────┬──────────────────────────────┐
    │ Input               │ Output                       │ 
    ├─────────────────────┼──────────────────────────────┤
    │ - TRANSLATE:        │ Domain: Any Domain           |
    │     Domain: any.dom │     Title: Any Domain        |
    │                     |     Description: Bla, bla... │
    └─────────────────────┴──────────────────────────────┘    
    ```

    ---
    <br/>

