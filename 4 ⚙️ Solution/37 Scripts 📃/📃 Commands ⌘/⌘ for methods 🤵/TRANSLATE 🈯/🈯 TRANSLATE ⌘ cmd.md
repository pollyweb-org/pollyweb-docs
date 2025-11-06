<!-- TODO -->
# 🈯 Talker `TRANSLATE` command

1. **Syntax**

    ```yaml
    TRANSLATE >> $translation:
        Schema: $schema
        Schemas: [$schemas]
        Domain: $domain
        Domains: [$schemas]
    ```

    ---
    <br/>

1. **Outputs**

    |Inputs|Output| Example
    |-|-|-
    |`Schema` or `Domain` | The translated text | `Any Domain`
    |`Schema` and `Domain`  | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | `{Domain:X, Schema:X}`
    |Other inputs | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)| `{Domains:[...]}`

    ---
    <br/>