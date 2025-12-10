
![alt text](<SignFile ⚙️ uml.png>)

## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - 
| 🆔 [Identity](<../../🆔 Identity agent/🆔🫥 Identity agent.md>) | 🫥 [Sign terms?](<../../🆔⏩ Identity flows/5 Verify Signatures 🆔⏩🔏/🆔⏩ Verify Signatures 🔏.md>) 📄 [Yes, No] | > Yes
| 🆔 [Identity](<../../🆔 Identity agent/🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../🆔⏩ Identity flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)

<br/>

## Script

```yaml
# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Context, Bind

# Assert the context
- ASSERT|$Context:
    AllOf: Title, Appendix
    Texts: Title
    Appendix.IsBase64:
    Appendix.IsPDF:

# Sign the file
- CONFIRM|Sign {$Context.Title}?:
    Appendix: $Context.Appendix

# Initiate the face recognition
- CALL|Identify >> $selfie:
    Bind: $Bind.ID
    Reference: $Bind.Reference

# Show the selfie web view
- WEB|Let me see if it's you.:
    URL: $selfie.URL
    
# Wait for the selfie validation
- WAIT|$selfie.Hook

# Initiate the face recognition
- CALL|SignFile >> $signed:
    Raw: $Context.Appendix
    Bind: $Bind.ID
    Reference: $Bind.Reference

# Return the signed file
- RETURN|$signed
```

Uses ||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CALL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`CONFIRM`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM 👍 prompt.md>) [`WAIT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>) [`WEB`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/WEB 🌐/🌐 WEB ⌘ cmd.md>) |
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsPDF`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsPDF ⓕ.md>) [`.IsBase64`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsBase64 ⓕ.md>) 

---
<br/>
