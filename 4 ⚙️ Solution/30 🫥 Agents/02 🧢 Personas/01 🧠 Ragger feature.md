🧠 Ragger feature FAQ
===

1. **What is the Ragger domain feature?**

    A Ragger is an implementation feature that enables Retrieval Augmented Generation (RAG) inferences with Generative Artificial Intelligence (GenAI) over a vector database.

    ---

1. **What are examples of Ragger usages?**

    - [Curator 🧚](<../03 🧚 Curators/01 🧚🫥 Curator agent.md>) vaults use it to build indirect knowledge about the user, to then filter and sort options suggested by other domains;
    - [👀 Advertiser](<../10 🔎 Finders/03 👀👥 Advertiser helper.md>) domains use it to select the next best ad options following a user's interaction with a [Host 🤗](<../../20 🧑‍🦰 UI/23 💬 Chats/04 🤗💬 Host chats.md>) domain;
    - [Finder 🔎](<../10 🔎 Finders/02 🔎🫥 Finder vault.md>) domains use it to select the best [Locators 🔆](<../../20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>) for a user search;
    - [Concierge 🛎️](<../06 🛎️ Concierges/01 🛎️🫥 Concierge agent.md>) domains use it to select the best [Suppliers 🏭](<../06 🛎️ Concierges/02 🏭🎭 Supplier role.md>) for a given task;
    - [Wand 🪄](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🏭 Wand supplier.md>) domains use it to build knowledge about a [Thing 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>) based on the documents provided by its [Brand 🍏](<../../70 ✅ 🌳 Ambient/71 ✅ 💠 Brand Things/07 ✅ 🍏🎭 Brand role.md>) domain;
    - [🛰️ Relayer](<../../60 ⏳ 🧰 Edge/61 ✅ 🔌 Pluggables/04 ✅ 🛰️🏭 Relayer supplier.md>) domains use it to understand how [Pluggable 🔌](<../../60 ⏳ 🧰 Edge/61 ✅ 🔌 Pluggables/01 ✅ 🔌 Pluggable device.md>) devices work, based on the documents provided by its [Brand 🍏](<../../70 ✅ 🌳 Ambient/71 ✅ 💠 Brand Things/07 ✅ 🍏🎭 Brand role.md>) domain.

    ---

1. **How to implement a Ragger on AWS?**

    ![](<./00 ✅ 📎 Assets/🧠 Ragger @AWS.png>)

    Raggers rely on the following component:
    - 📦 **Storage cache**: to maintain a local cache for [Storage 📦](<../01 ✅ 📦 Storage/01 ✅ 📦🫥 Storage agent.md>) vaults.

    ---