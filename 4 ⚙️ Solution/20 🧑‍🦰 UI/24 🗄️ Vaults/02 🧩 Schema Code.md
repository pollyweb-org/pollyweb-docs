🧩 Schema Codes FAQ
===

![](<./📎 Assets/🗄️ Schema Manifest.png>)

1. **How do domains validate the structure of messages?**

    In NLWeb, information is shared based on Schema Codes 🧩. 
    
    * When a [Consumer 💼](<../25 💼 Consumers/04 💼🎭 Consumer role.md>) domain needs information stored in a [Vault 🗄️](<03 🗄️🎭 Vault role.md>) domain, it states the Schema Code in the form of `{domain}/{code}:{version}` 
        - this allows the chat participants to know where to get the schema definition for the [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) 
        - e.g., the code `nlweb.com/TOKEN:2.0` references version `2.0` of a schema called `TOKEN` that is defined in the [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) of the [Authority 🏛️](<../../40 👥 Domains/43 👍 Trusts/02 🏛️👥 Authority helper.md>) domain `nlweb.com`. 
    
    * For resilience and performance, domains can query [Graphs 🕸](<../../40 👥 Domains/44 📜 Manifests/03 🕸👥 Graph helper.md>) directly for a schema definition by passing a Schema Code 🧩.

    ---

1. **Are there any pre-defined Schema Codes?**

    Yes. 
    - The NLWeb protocol is supported by a set of Schema Codes 🧩 defined in the nlweb.org [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>). 
    
    - This high-level manifest includes the schema definition for all communications explicitly supported by the core NLWeb protocol, but also a set of auxiliary schemas used to implement various business use cases. 

    ---

1. **Is the NLWeb manifest a single point of failure?**

    No. 
    - Domains don't need nlweb.org to be online to access its [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) (nor the Manifest of any other domain, for that matter).
    - Instead, domains should rely on [Graph 🕸](<../../40 👥 Domains/44 📜 Manifests/03 🕸👥 Graph helper.md>) caches to look up schema definitions.

    ---

1. **Wouldn't JSON be faster than YAML?**

    Yes. 
    - But, because of [Graph 🕸](<../../40 👥 Domains/44 📜 Manifests/03 🕸👥 Graph helper.md>) caches, the performance of either protocol is irrelevant in this context. 
    - NLWeb advocates for human readability, with YAML format being closer to natural language.

    ---

1. **Are NLWeb schema definitions compatible with JSON Schema?**

    Yes. 
    - NLWeb schemas are defined by JSON Schema converted to YAML, leveraging YAML's ability to include JSON as valid syntax.

    ---