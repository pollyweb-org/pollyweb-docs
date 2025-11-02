# 🔎 Introduce 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Introduce@Finder` 🅰️ method](<🔎 Introduce 🐌 msg.md>)

## Script

```yaml
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
    Text:   
        {$translation.Domain} 
        ({$reviews.Rating} ⭐)
    Details: |
        {$reviews.Description}
        {$identity.Description}

# Inform the Broker
- SEND:
    Header:
        To: $.Msg.From
        Subject: Introduced@Broker
    Body:
        Chat: $.Msg.Chat
```

Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | 
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Identity@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) <br/> [`Translate@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) <br/> [`Reviews@Reviewer` 🅰️ method](<../../../Reviewers ⭐/⭐🅰️ Reviewer methods/🔎🚀⭐ Reviews.md>)
|