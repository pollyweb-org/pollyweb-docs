<!-- TODO -->
# 🈯 Talker `TRANSLATE` command

## FAQ

1. **What's the syntax of TRANSLATE?**

    ```yaml
    TRANSLATE >> $translation:
        Schema: $schema
        Schemas: [$schemas]
        Domain: $domain
        Domains: [$schemas]
    ```

    ---
    <br/>

1. **What are the outputs of TRANSLATE?**

    |Inputs|Output| Example
    |-|-|-
    |`Schema` or `Domain` | The translated text | `Any Domain`
    |`Schema` and `Domain`  | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | `{Domain:X, Schema:X}`
    |Other inputs | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)| `{Domains:[...]}`

    ---
    <br/>

