🧩 Schema Codes FAQ
===


1. **How do domains validate the structure of messages?**

    In NLWeb, information is shared based on [Schema Codes 🧩](<02 🧩 Schema Code.md>). 
    
    * When a [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) needs information stored in a [Vault 🗄️ domain](<03 🗄️🎭 Vault role.md>), it states the [Schema Code 🧩](<02 🧩 Schema Code.md>) of the information in the form of `{domain}/{code}:{version}`;
        - this allows the chat participants to know where to get the schema definition for the [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) 
        - e.g., the code `nlweb.com/TOKEN:2.0` references version `2.0` of a schema called `TOKEN` that is defined in the [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) of the [Authority 🏛️ domain](<../../40 👥 Domains/43 👍 Trusts/02 🏛️🛠️ Authority helper.md>) `nlweb.com`. 
    
    * For resilience and performance, domains can query [Graph 🕸 domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) directly for a schema definition by passing a [Schema Code 🧩](<02 🧩 Schema Code.md>).

    ---

2. **What does it mean when a YAML content starts with 🤝?**

    When YAML starts with `🤝: {domain}/[{path}/]{code}[:{version}]`,
    * e.g., `🤝: nlweb.org/MANIFEST/CODE`
    * it means that the following YAML content should comply with the given [Schema Code 🧩](<02 🧩 Schema Code.md>) defined.
    * This allows readers to validate the YAML content by pulling the validation schema from [Schema @ Graph](<../../../6 🅰️ APIs/08 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>).
    
    ---

3. **How do define a Schema in a Manifest?**

    The instructions on how to add a [Schema Code 🧩](<02 🧩 Schema Code.md>) to a [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) are themselves published as special [Schema Codes 🧩](<02 🧩 Schema Code.md>):

    | Schema | Description
    |-|-
    | [`nlweb.org/MANIFEST/CODE 🧩`](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCode.md>) | CODE properties.
    | [`nlweb.org/MANIFEST/CODE/SCHEMA 🧩`](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCodeSchema.md>) | CODE/SCHEMA properties.
    | [`nlweb.org/MANIFEST/DELEGATE 🧩`](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestDelegate.md>) | Delegation to other [Authorities 🏛️](<../../40 👥 Domains/43 👍 Trusts/02 🏛️🛠️ Authority helper.md>).
    | [`nlweb.org/TYPES 🧩`](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/TYPES/🧩 Types.md>) | Generic referenceable types.

    ---
    <br/>

4. **Are there any pre-defined Schema Codes?**

    Yes. 
    - The NLWeb protocol is supported by a set of [Schema Codes 🧩](<02 🧩 Schema Code.md>) defined in the `nlweb.org` [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>). 
    
    - This high-level manifest includes the schema definition for all communications explicitly supported by the core NLWeb protocol, but also a set of auxiliary schemas used to implement various business use cases. 

    Examples include.

    * 

    ---

5. **Is the NLWeb manifest a single point of failure?**

    No. 
    - Domains don't need `nlweb.org` to be online to access its [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) (nor the Manifest of any other domain, for that matter).
    - Instead, domains should rely on [Graph 🕸 helper domain](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) to look up schema definitions.

    ---


5. **Are NLWeb schema definitions compatible with JSON Schema?**

    Yes. 
    - NLWeb schemas are defined by JSON Schema converted to YAML, leveraging YAML's ability to include JSON as valid syntax.

    ---

4. **Wouldn't JSON be faster than YAML?**

    Yes JSON is much faster than YAML. 
    - But, because of [Graph 🕸 domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>), the performance of either protocol is irrelevant in this context. 
    - NLWeb advocates for human readability, with YAML format allowing comments and being closer to structured natural language in this context.

    ---