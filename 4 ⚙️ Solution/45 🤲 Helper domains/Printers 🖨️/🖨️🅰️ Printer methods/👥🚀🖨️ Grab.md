# 👥🚀🖨️ Grab @ Printer

> A [Printer 🖨️ domain](<../🖨️🤲 Printer helper.md>) grabs an available alias. 

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: any-domain.dom
    To: any-printer.dom
    Subject: Grab@Printer

Body: 
    Alias: ANY-ALIAS
    Locator: .HOST,any-host.dom,any-key
```

|Object|Property|Type|Description
|-|-|-|-
|Header| `From`| string | Caller [domain 👥](<../../../40 👥 Domains/👥 Domain.md>) name
|| `To` | string | [Printer 🖨️ domain](<../🖨️🤲 Printer helper.md>) name
|| `Subject`| string | `Grab@Printer`
|Body|`Alias`| string | Unique alias on the [Printer 🖨️](<../🖨️🤲 Printer helper.md>)
|| Locator | string | [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) 
|

<br/>

## Synchronous Response

| HTTP | Details
|-|-
| 200   | Success.
| 409   | Alias already occupied - use another alias.
| 400   | Locator not supported - only [`.HOST 🧩`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>) is supported.
|

<br/>

## Handler

```yaml
# Verify the signature.
- VERIFY|$.Msg

# Only create Alias for Hosts.
- ASSERT|$.Msg.Locator:
    Host: .HOST

# Save on the table.
- SAVE|Aliases@Printer >> $locator:
    Alias: $.Msg.Alias
    Locator: $.Msg.Locator 

# Respond with the Locator.
- REEL
```

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| 🚦 [`ASSERT`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) | Require [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) schemas as `.HOST`
| 💾 [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) | Save to [Aliases 🪣](<../🖨️🪣 Printer tables/🖨️🪣 Aliases.md>) with `NoUpdate`
| 🎣 [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) | Respond to the [Synchronous Request 🚀](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)
|

