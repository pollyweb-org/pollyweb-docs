🤝 Biller Templates
===

> About
* Part of the [Biller 🤝 domain](<../🤝 Biller/🤝 Biller 🤲 helper.md>)

## FAQ

1. **What are Biller Templates?**

    Biller Templates
    * are rendering settings
    * to generate PDF documents (e.g., invoices)
    * from a given [Map 🧠](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) input.

    ---
    <br/>

1. **What do Biller Templates include?**
    
    Part | Purpose
    |-|-
    | `Formulas` | Calculations over the data with [{Functions} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    | `Formats` | Formatting rules over the data with [Prompt 🤔](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) formats
    | `Layout` | Markdown arrangement of the data in a paginated PDF

    ---
    <br/>

1. **How to send data into templates?**

    ```yaml
    Customer:
        Name: John Doe
        TaxNumber: 123456789
    
    Items:

        - Name: Product 1
          Tax: 0.1
          Price: 100.00

        - Name: Product 2
          Quantity: 2
          Tax: 0.2
          Price: 200.00
    ```

    ---
    <br/>

1. **How to define formulas for a template?**

    ```yaml
    Items:
        Quantity.Default: 1
        Price: Price.Round(5)
        PreTaxes: Price.Times(Quantity).Round(2)
        Taxes: PreTaxes.Times(Tax).Round(2)
        PostTaxes: PreTaxes.Plus(Taxes)
    Total: Items.PostTaxes.Sum
    Taxes: Items.Taxes.Sum
    ```
    Uses: [`.Default`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Default ⓕ.md>) [`.Round`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Round ⓕ.md>) [`.Times`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Times ⓕ.md>) [`.Plus`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Plus ⓕ.md>) [`.Sum`](<../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Sum ⓕ.md>)

    ---
    <br/>



1. **How to format values in templates?**

    Follow the definitions of [`AMOUNT`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/AMOUNT 💰/AMOUNT 💰 prompt.md>) [`DATE`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DATE 📆/DATE 📆 prompt.md>) [`DIGITS`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/DIGITS 🔢 prompt.md>) [`QUANTITY`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) [`TEXT`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>)
  
    * either inline, with `Variable: <FORMAT>`
    * or in blocks, like the `Price` block below.

    ```yaml
    Items: 
        Quantity: QUANTITY
        Price: 
            Format: AMOUNT
            Precision: 5
        Tax: PERCENT
        PreTaxes: AMOUNT
    Total: AMOUNT
    Taxes: AMOUNT
    ```

    ---
    <br/>


1. **What are template layouts?**

    Layouts are Markdown definitions that support HTML.
    * Follows the [markdown-it](https://markdown-it.github.io) playground behavior.
    * Follows the [WeasyPrint](https://weasyprint.org/) pagination behavior.
    * Translates the output with [`TRANSLATE` 🈯](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>), except for `´´`.
    * Replaces variables enclosed in `{}` with data and formulas.
    * Renders lists into tables using the `{List|...}` syntax.

    ---
    <br/>

1. **How to use sequences?**

    Sequences are unique identifiers of documents.
    * They're assigned with the inputs on rendering.
    * When rendering, they're available on the `Sequence` [map](<../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>).

    The available fields are:
    - `Sequence.Name`: the name of the sequence requested.
    - `Sequence.Number`: the current number in the sequence.
    - `Sequence.Year`: the current year of the sequence.

    ---
    <br/>


1. **What's an example of a template layout?**

    ```markdown
    ## My Invoice {Sequence.Number}
    **Customer**: ´{Customer.Name}´ <br/>
    **Tax Number**: ´{Customer.TaxNumber}´
    
    |Qt|Item|Tax|Per Unit|Sub Total
    |-:|-|-:|-:|-:-:
    {Items: {Quantity}|´{Name}´|{Tax}%|${Price}|${PreTaxes}} 

    |||
    |-|-:|
    **Total**| $ {Total}
    **Taxes**| $ {Taxes}

    <p align="center">My final message.</p>
    ```

    ---
    <br/>


1. **What's an example of a final outcome?**

    
    ## My Invoice 001
    **Customer**: John Doe <br/>
    **Tax Number**: 123456789
    
    |Qt|Item|Tax|Per Unit|Sub Total
    |-:|-|-:|-:|-:
    1 | Product 1 | 10% | $ 100.00 | $ 100.00
    2 | Product 2 | 20% | $ 200.00 | $ 400.00

    |||
    |-|-:|
    **Total**| $ 590.00
    **Taxes**| $ 80.00

    <p align="center">My final message.</p>

    ---
    <br/>