# 😃ⓕ Talker `{.MaxHeight}` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Counterpart of the [`.MaxWidth`](<MaxWidth ⓕ.md>) function

## FAQ


1. **What is the .MaxHeight function?**

    `{.MaxHeight}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that given a Base64 string representation of an image 
    * returns the Base64 content of the image 
        * resized to the given maximum height, 
        * while maintaining the aspect ratio.

    ---
    <br/>

1. **What's the syntax of the .MaxHeight function?**

    ```yaml
    $image.MaxHeight: <maxHeight>
    ```

    |Property|Type|Description
    |-|-|-
    | `$image`  | text  | Base64 encoded image string
    | `<maxHeight>`  | num   | Maximum height to resize the image to, in pixels

    ---
    <br/>

1. **What's the error handling behavior?**

    If the `<maxHeight>` fails to be a number greater than 0, then the original `$image` is returned.

    ---
    <br/>