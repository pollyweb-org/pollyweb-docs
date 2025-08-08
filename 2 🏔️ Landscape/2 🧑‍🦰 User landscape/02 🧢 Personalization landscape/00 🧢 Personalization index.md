🧢 Personalization landscape FAQ
===

🎯 Sharing personal identifiable information(PII) with businesses and public services is a common requirement for physical and online transactions (e.g., personalization, delivery, and payment).

- However, sharing PII often results in commercial spam, fraud, and identity theft.
- To protect user PII, brands are leveraging public trust to serve as proxies for their customers, e.g.:
    - Apple with the Ad Network, making it impossible for businesses to track users;
    - Google with Chrome PassKeys, proxying unique passwords on behalf of users;
    - and PayPal with FastLane, allowing users to remain anonymous on checkouts.
- In parallel, the tech industry conceptualized the self-sovereign identity (SSI):
    - with personal vaults, where users can centralize and share their PII;
    - with selective disclosure, for users to share only parts of the PII in their documents;
    - and with zero-knowledge proof, for users to prove entitlement without sharing any PII.


💬 NLWeb advocates for data privacy with a combination of:
- **personal vaults**, implemented by the same organizations that already own PII; 
- **zero knowledge proof**, where proof is delegated to vaults in online and offline fashion;
- **multiple self-sovereign digital twins**, where the same person can anonymously share different preferences with same organization depending on the situation (e.g., a person has different preferences when traveling for business or leisure).

💬 NLWeb does not advocate for **selective discloser**:
- Taking from the experience of accepting cookies on websites, users typically default to give away all that they are being asked for by businesses, either due to laziness or fear of being denied the service or product by the business.
- Instead of selective discloser, NLWeb advocates for business to request data schemas that are purpose driven and limited to the specific purpose - e.g., when selling alcohol in the UK:
    - bars and pubs should ask "are you over 21, yes or no?";
    - instead of asking "can you selectively disclose only the date of birth from your identity card?".
- For transparency, businesses need to publicly manifest all their potential requests to customers:
    - any request to a consumer that is not listed on the public manifest will be blocked;
    - this allows regulators to monitor businesses requesting customer data not aligned with business description of their manifest.
    


📺 In this chapter, you will learn:

- How PII is traditionally abused and protected, namely:
    - how PII of [random people](<01 📺 Random PII smart glasses.md>) can be found in real-time using smart glasses;
    - how [scammers](<02 📺 Top scams 2024.md>) can take advantage of PII for spam, fraud, and identity theft;
    - how search engines like 🇺🇸 [Google](<03 📺 🇺🇸 Google's search delete.md>) allow users to remove themselves from indexes;
    - how countries like 🇨🇳 [China](<04 📺 🇨🇳 China's privacy law.md>) enforced regulation to protect PII.

- How self-sovereign identity (SSI) aims to protect PII, namely:
    - what are 🗄️ [vaults](<./05 📺 Berners-Lee vaults.md>), according to Sir Tim Berners-Lee (inventor of the web);
    - how 📝 [form auto-filling](<06 📺 SSI form auto filling.md>) simplifies sharing PII;
    - how 📜 [selective disclosure](<07 📺 SSI selective disclosure.md>) limits shared PII;
    - how 👤 [zero-knowledge proof](<08 📺 SSI zero knowledge proof.md>) avoids sharing PII;
    - how 🔐 [passwordless login](<09 📺 Passwordless login.md>) avoids activity tracking.

- How SSI concepts are being tested by public and private companies, e.g.:
    - by the travel industry, advocating for [vaccine passports](<10 📺 COVID.md>) during COVID;
    - by the 🇺🇸 U.S. Military, with 🏥 [personal health record (PHR)](<11 📺 Personal Health.md>) vaults;
    - by Affinidi, in 👚 [personalized shopping](<12 📺 Affinidi.md>), with preference vaults;
    - by PayPal, in 📦 [guest checkout](<13 📺 PayPal Fastlane.md>), with PayPal Fastlane vault.
    - and by Gartner, advocating for a [customer digital twin](<14 📺 Gartner twins.md>) in retail.
    