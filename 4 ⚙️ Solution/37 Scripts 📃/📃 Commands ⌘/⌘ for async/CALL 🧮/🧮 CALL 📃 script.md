# 🧮 CALL 📃 script

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`CALL`](<🧮 CALL ⌘ cmd.md>) command.


<br/>

## Diagram

![alt text](<🧮 CALL ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .CALL:
    Name: <name>
    Inputs: {...}           # Optional
```

<br/>

## Script

```yaml
📃 .CALL:

# Assert the inputs
- ASSERT $.Inputs:
    AllOf: Name

# Return immediately for internal functions
- IF:
    $Name.StartsWith: .
- THEN:
    RETURN:
        .Evaluate: $Name, $Inputs

# If it got here, then it's external
- PUT: .UUID >> $uuid     # Generate a unique ID
- IMPRINT: $uuid          # Save the current state

- ASYNC:                  # Call Handle@Hosted
    Hook: $uuid           # Placed@, Place@, Handled@ hook
    Name: $Name           # Hosted function name
    Inputs: $Inputs       # Hosted function inputs

- WAIT: $uuid >> $result  # Wait for the RACE command
- RECALL: $uuid           # Restore the previous state
- RETURN: $result         # Return the result of the call
```

|Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`ASYNC`](<../ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>) [`IMPRINT`](<../IMPRINT 🦶/🦶 IMPRINT ⌘ cmd.md>)   [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`RECALL`](<../RECALL 🪶/🪶 RECALL ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>) |
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.UUID`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/UUID ⓕ.md>) [`.StartsWith`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/StartsWith ⓕ.md>) [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
|