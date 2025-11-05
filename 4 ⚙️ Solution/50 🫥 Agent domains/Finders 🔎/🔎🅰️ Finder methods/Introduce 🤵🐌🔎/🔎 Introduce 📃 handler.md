# 🔎 Introduce 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Introduce@Finder` 🅰️ method](<🔎 Introduce 🐌 msg.md>)

<br/>

## Flow

![alt text](<🔎 Introduce ⚙️ uml.png>)

<br/>

## Script

> Called by the [`Assess@Broker` 📃 handler](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 📃 handler.md>)

```yaml
📃 Introduce@Finder: 

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
                    Domain: $.Msg.Host$

        Translate:
            SEND >> $translation:
                Header:
                    To: $.Hosted.Graph
                    Subject: Identity@Graph
                Body:
                    Language: $.Msg.Language
                    Domain: $.Msg.Host$

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
        Subject: Introduced@Broker
    Body:
        Chat: $.Msg.Chat
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`INFO`](<../../../../35 💬 Chats/Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`PARALLEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identity@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) <br/> [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) <br/> [`Reviews@Reviewer` 🅰️ method](<../../../Reviewers ⭐/⭐🅰️ Reviewer methods/🔎🚀⭐ Reviews.md>)
|