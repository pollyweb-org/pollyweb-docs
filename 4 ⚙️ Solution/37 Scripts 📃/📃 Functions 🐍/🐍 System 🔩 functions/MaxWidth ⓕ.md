# 😃ⓕ Talker `.MaxWidth` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Counterpart of the [`.MaxHeight`](<MaxHeight ⓕ.md>) function

## FAQ


1. **What is the .MaxWidth function?**

    `.MaxWidth`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that given a Base64 string representation of an image 
    * returns the Base64 content of the image 
        * resized to the given maximum width, 
        * while maintaining the aspect ratio.

    ---
    <br/>

1. **What's the syntax of the .MaxWidth function?**

    ```yaml
    $image.MaxWidth: <maxWidth>
    ```

    |Property|Type|Description
    |-|-|-
    | `$image`  | text  | Base64 encoded image string
    | `<maxWidth>`  | num   | Maximum width to resize the image to, in pixels

    ---
    <br/>

1. **What's the error handling behavior?**

    If the `<maxWidth>` fails to be a number greater than 0, then the original `$image` is returned.

    ---
    <br/>