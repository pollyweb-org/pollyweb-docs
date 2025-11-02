# 🔎 Introduce 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Introduce@Finder` 🅰️ method](<🔎 Introduce 🐌 msg.md>)

## Script

```yaml
# Verify the message
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Chat, Host, Language
    UUIDs: Chat
    Texts: Host, Language

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
                    To: $.Hos

# Send the Prompt
- INFO|Any Host (4.3 ⭐):
This host sells shoes.
- They were founded in 1987.
- Joined NLWeb 2 years ago.
User feedback:
- Delivery 4.7⭐ by 357 users
- Support 3.5⭐ by 21 users

# Inform the Broker
- SEND:
    Header:
        To: $.Msg.From
        Subject: Introduced@Broker
    Body:
        Chat: $.Msg.Chat
```