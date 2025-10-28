<!-- TODO -->
# 💼 SHARE 📃 script

[Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) that implements [`SHARE`](<💼 SHARE ⌘ cmd.md>)

# Flow



## How to call

```yaml
- RUN|SHARE:
    Schemas: 
      - any-authority.dom/ANY-SCHEMA
```

## Script

```yaml
📃 SHARE:

# Assert inputs
- ASSERT:
    AllOf: $:Schemas
    Lists: $:Schemas

# Save the hook
- SAVE|TalkerHooks >> $hook:
    Hook: .UUID
    Broker: $.Chat.Broker
    PublicKey: $.Chat.PublicKey
    Schemas: $:Schemas

# Query the Broker
- SEND:
    Header:
        To: $.Chat.Broker
        Subject: Query@Broker
    Body: 
        Chat: $.Chat.Chat
        Hook: $hook.Hook
        Schemas: $:Schemas

# Wait for the shared data
- WAIT >> $shared:
    Signal: $hook.Hook

# Return the data
- RETURN:
    $shared
```