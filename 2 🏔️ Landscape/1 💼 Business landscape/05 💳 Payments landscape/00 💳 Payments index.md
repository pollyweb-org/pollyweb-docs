💳 Payments landscape FAQ
===

## 🎯 Target

Payments are intrinsic to human transactions, as they represent the counter-part for the received goods or services. 



## 🧠 Learning resources 

In this chapter, you will learn:

- What challenges [🧑 end-users](<01 🧑 User challenges.md>) face with payments.
- What the [🌐 market size](<02 📄 Market size.md>) for end-user payments is.
- What the [🌐 financial industry](<03 📄 Financial industry.md>) is doing around payments.
- How countries and intergovernmental organizations are addressing end-user payments, e.g.: 
    - 🌍 the [African Union](<04 📺 🌍 Africa's PAPSS.md>) with the PAPSS central platform;
    - [🇧🇷 Brazil](<05 📺 🇧🇷 Brazil's Pix.md>) with the PIX central platform;
    - [🇨🇳 China](<06 📺 🇨🇳 Alibaba+Tencent.md>) with interoperability between super-apps like Alipay and WeChat;
    - 🇪🇺 the [European Union](<07 📺 🇪🇺 Europe's EPI.md>) with the EPI central platform, the Wero app, and the EU Digital Wallet;
    - 🇮🇳 [India](<08 📺 🇮🇳 India's UPI.md>) with the UPI central platform;
    - 🇵🇹 [Portugal](<09 📺 🇵🇹 Portugal's MBWay.md>) with the MB Way central platform; 
    - 🇺🇸 and the [United States](<10 📺 🇺🇸 Apple vs Banks.md>) with smartphone manufacturers like Apple and Google.
- Why stores like [🇺🇸 Walmart](<11 📺 🇺🇸 Walmart vs Apple.md>) limit shoppers' payment options.
- What was [🌐 Libra](<12 📺 Meta's Libra.md>), Facebook's cryptocurrency project.



## 💬 Proposed Solution

NLWeb aims to seamlessly incorporate payments into interaction workflows, while simplifying the experience to both users and businesses.

|Domain | Purpose
|-|-
|[💳 Payer](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | Pays money on behalf of users.
|[🏦 Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | Collects money on behalf of businesses.


## 💬 Proposed Workflow

|#|Category|Workflow Step
|-|-|-
|1|`Bill`| A Businesses issues a bill via their [Collector 🏦 helper domain](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>).
|2|`Collect`| The [business' Collector 🏦 helper](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) asks the money in the business currency to [user's 💳 Payer agent domain](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>).
|3|`Negotiate`| The [user's Payer 💳 domain](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) and the [business' Collector 🏦 domain](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) agree on the transfer channel (e.g. Wise).
|4|`Pay`| Users pay in their preferred currency and methods (e.g., AMEX).
|5|`Fees`| The [user's Payer 💳 domain](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) collects and distributes additional payment fees (e.g., AMEX fee).
