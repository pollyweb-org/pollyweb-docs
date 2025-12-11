# 🔎 Present 📃 handler

> Purpose
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Present@Finder` 🐌 msg](<🔎 Present 🐌 msg.md>)

<br/>

## Flow

![alt text](<🔎 Present ⚙️ uml.png>)

<br/>

## Script


```yaml
📃 Present@Finder: 

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Chat, Host, Language, Reviewers
    UUIDs: Chat
    Texts: Host, Language, Reviewers

# Get the details about the domain
- PARALLEL|Identity,Translate,Reviews|$task:
    CASE|$task:

        Identity:
            SEND >> $identity:
                To: $.Hosted.Graph
                Subject: About@Graph
                Domain: $Host

        Translate:
            TRANSLATE >> $translation:
                Domain: $Host
                To: $Language

        Reviews:
            SEND >> $reviews:
                To: $Reviewer
                Subject: Reviews@Reviewer
                Language: $Language
                Domain: $Host

# Send the Prompt
- INFO:
    Text: "{$translation.Domain} ({$reviews.Rating} ⭐)"
    Details: |
        {$reviews.Description}

        {$identity.Description}
    Options:
        $reviews.Options
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`PARALLEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`About@Graph` 🚀 call](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 🚀 call.md>) <br/> [`Translate@Graph` 🚀 call](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) <br/> [`Reviews@Reviewer` 📨 msg](<../../../Reviewers ⭐/⭐📨 Reviewer msgs/Reviews 🔎🚀⭐/🔎🚀⭐ Reviews.md>)
|