# 🔎 Present 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Present@Finder` 🅰️ method](<🔎 Present 🐌 msg.md>)

<br/>

## Flow

![alt text](<🔎 Present ⚙️ uml.png>)

<br/>

## Script

> Called by the [`Locate@Broker` 📃 handler](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 📃 handler.md>)

```yaml
📃 Present@Finder: 

# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Chat, Host, Language, Reviewers
    UUIDs: Chat
    Texts: Host, Language, Reviewers

# Get the details about the domain
- PARALLEL|Identity,Translate,Reviews|$task:
    CASE|$task:

        Identity:
            SEND >> $identity:
                Header:
                    To: $.Hosted.Graph
                    Subject: Identity@Graph
                Body: 
                    Domain: $.Msg.Host

        Translate:
            TRANSLATE >> $translation:
                Domain: $.Msg.Host
                To: $.Msg.Language

        Reviews:
            SEND >> $reviews:
                Header:
                    To: $.Msg.Reviewer
                    Subject: Reviews@Reviewer
                Body:
                    Language: $.Msg.Language
                    Domain: $.Msg.Host$

# Send the Prompt
- INFO:
    Text: "{$translation.Domain} ({$reviews.Rating} ⭐)"
    Details: |
        {$reviews.Description}

        {$identity.Description}
    Options:
        $reviews.Options

# Inform the Broker
- SEND:
    Header:
        To: $.Msg.From
        Subject: Presented@Broker
    Body:
        Chat: $.Msg.Chat
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`PARALLEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identity@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity/👥🚀🕸 Identity.md>) <br/> [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/👥🚀🕸 Translate.md>) <br/> [`Reviews@Reviewer` 🅰️ method](<../../../Reviewers ⭐/⭐🅰️ Reviewer methods/🔎🚀⭐ Reviews.md>)
|