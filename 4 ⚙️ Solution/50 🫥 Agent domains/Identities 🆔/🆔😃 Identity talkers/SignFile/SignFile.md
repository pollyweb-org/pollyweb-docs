
## Chat

| [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
| - | - | - 
| 🆔 [Identity](<../../../../50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔🫥 Identity agent.md>) | 🫥 [Sign terms?](<../../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/5 Verify Signatures 🆔⏩🔏/🆔⏩ Verify Signatures 🔏.md>) 📄 [Yes, No] | > Yes
| 🆔 [Identity](<../../../../50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../../../50 🫥 Agent domains/Identities 🆔/🆔⏩ Identity flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)

<br/>

## Script

```yaml
# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Context, Bind

# Assert the context
- ASSERT|$Context:
    AllOf: Title
    Texts: Title

# Sign the file
- CONFIRM|Sign {$Context.Title} ?:
    Appendix: $$
```

---
<br/>
