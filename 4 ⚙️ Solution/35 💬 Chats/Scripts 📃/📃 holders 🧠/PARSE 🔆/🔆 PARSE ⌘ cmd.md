# 🔆 Talker `PARSE` command

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

> Used by [`Grab@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Grab 👥🚀🖨️/🖨️ Grab 🚀 request.md>)

<br/>

1. **What's a PARSE command?**
   
   A `PARSE` 
   * is a handler [Command ⌘](<../../📃 commands ⌘/Command ⌘/⌘ Command.md>) 
   * that parses a [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>).

    ---
    <br/>

1. **What's the PARSE syntax?**

    ```yaml
    PARSE >> $out:
        Locator: $locator
    ```

    | Inputs | Purpose
    |-|-
    | `$locator` | [Holder 🧠](<../$Holder 🧠.md>) with the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) to parse.

    ---
    <br/>

1. **How to use a PARSE?**

    Consider the following [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in a holder `$in`.

    ```yaml
    .HOST:1.0,any-host.dom,ANY-RESOURCE
    ```

    Here's the [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    - PARSE|$in >> $out
    ```

    Here's the properties returned by `$out`.

    | Expression| Result
    |-|-
    | `Schema`| `nlweb.dom/HOST:1.0`
    | `IsAlias` | `False`
    | `Host`| `any-host.dom`
    | `Key`| `ANY-RESOURCE`

    ---
    <br/>

