🧑‍💻 Unsupervised ID authentication landscape FAQ
===

🎯 Unsupervised ID authentication/verification is the ability for organizations to trust that the holder of a digital credential is the indeed the person to whom the credential was issued to, while the user is remotely and asynchronously submitting the credential.

- A typical scenario involves a new customer [opening a bank account](<AlRayan) on their smartphone while sitting on their sofa late at night.

- While 👮 [supervised scenarios](<../06 👮 Supervised ID landscape/00 👮 Supervised ID Index.md>) allow for simple face matching solutions (e.g., a face scan at London Heathrow Airport is enough to match the person to the passport before crossing the border gate), unsupervised remote scenarios require increasingly complex solutions to avoid fraud (e.g., bad actors impersonating someone else by replacing biometrics or leveraging generative AI).

---

💬 NLWeb advocates for facial verification with remotely-controlled web-based [liveness-checks](<09 📺 Amazon liveness.md>):

- This limits the ability of bad actors to interfere with user devices.
- It allows delegating the verification to the user's citizenship trusted nation.
- By leveraging the web, it was a low-implementation cost and high resilience.

---

📺 In this chapter, you will learn:

- How organizations are using remote authentication, e.g.:
    - how [🌎 Uber](<01 📺 Uber remote ID.md>) authenticates drivers with face biometrics before rides;
    - how [🇬🇧 Al Rayan Bank UK](<02 📺 🇬🇧 Al Rayan Bank UK.md>) remotely onboards new customers using face biometrics with movement-based liveness checks;
    - how [🇸🇬 Singapore](<../04 🆔 Digital ID landscape/10 📺 🇸🇬 Singapore's DID.md>) adopted face biometrics with color-based liveness checks for their national identity program;
    - and how [🇸🇬 OCBC Bank Singapore](<04 📺 🇸🇬 OCBC Bank.md>) customers withdraw money from ATMs using face biometrics with color-based liveness checks.

- Why 📱 phone-managed face biometrics is not a secure authentication mechanism, e.g.:
    - Apple's [Face ID](<05 📺 Apple Face ID.md>) is design for **users** to unlock phones, and not to authenticate the **owner**;
    - the owner's [family members](<06 📺 Apple's security.md>) can also unlock the phone and perform transactions;
    - thieves can [replace the face ID](<07 📺 Apple's thief.md>) to drain the owner's bank accounts;
    - and hackers can use [Generative AI](<08 📺 Deep fakes.md>) to interfere with the device's face biometrics.

- How remotely-controlled liveness checks are safer than phone's face biometrics, e.g.:
    - [Amazon](<09 📺 Amazon liveness.md>), with Amazon Rekognition Liveness Check;
    - and [Microsoft](<10 📺 Microsoft liveness.md>), with Microsoft Entra Verified ID.


---