📺 How do 📨 email servers authenticate?
---

This 2023 video from Mailtrap, titled *"How DKIM works - Tutorial by Mailtrap"*, explains how email servers authenticate each other.

- When email servers send messages between them, the message is signed with the sender's private key, and the receiver uses the sender's public key (available as a DKIM DNS record) to verify the message. 

- Domains may have more than one active DKIM to support [periodic rotations](<00 📎 Assets/🔐 dkim-rotations.pdf>) (e.g., every 4 months), so receivers need to lookup the message's DKIM selector to know which active key to use for validation.

<!-- https://www.youtube.com/watch?v=oPdGmJUquyM --><br/>

[379937041-41580fd2-89ab-4bdc-bc14-670640d38d78.webm](https://github.com/user-attachments/assets/95499ec4-7033-4d2b-b450-a5fc75ca5a72)
