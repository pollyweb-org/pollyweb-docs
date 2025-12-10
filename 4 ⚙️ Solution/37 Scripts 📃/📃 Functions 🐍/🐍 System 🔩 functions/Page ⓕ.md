# 😃🔩 Talker `{.Page}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What is the .Page function?**

    `{.Page}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that given a Base64 PDF string
    * returns the Base64 content of a specific page number, 
    * allowing large PDFs to be downloaded page by page.

    ---
    <br/>

1. **What's the syntax of the .Page function?**

    ```yaml
    .Page($pdf, <page>)
    ```

    |Property|Type|Description
    |-|-|-
    | `$pdf`  | text  | Base64 encoded PDF string
    | `<page>`  | num   | Page number to extract (1-based index)

    ---
    <br/>