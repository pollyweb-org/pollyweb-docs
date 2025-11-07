# 😃🔩 Talker `{.IsEmpty}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What is the .IsEmpty function?**

    `{.IsEmpty}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if the input is empty
    * or `False` otherwise.

    ---
    <br/>

1. **How is emptiness assessed?**

    | Input| Details | Examples | Result
    |-|-|-|-
    | `Lists` | Lists with values | `[0]` `[*]` | ❌ False
    | | Empty lists | `[]` | ✅ True
    | `Objects` | Objects with values | `{A:0}` | ❌ False
    | | Empty objects | `{}` | ✅ True
    | `Text` | Non-empty text | `A` | ❌ False
    |           | Empty text | ` ` | ✅ True
    | `Others`| Any values | `1` `0` | ❌ False
    |          | Empty [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)  | `$p=` | ✅ True
    |

    <br/>
