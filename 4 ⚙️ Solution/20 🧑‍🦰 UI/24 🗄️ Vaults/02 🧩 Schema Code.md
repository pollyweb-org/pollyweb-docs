🧩 Schema Codes FAQ
===

1. **What is a Schema Code?**

    A [Schema Code 🧩](<02 🧩 Schema Code.md>) is a string 
    * formatted as `{authority}/{code}[:{version}]`
    * e.g., `nlweb.org/LOCATOR:1.0`
    * that points to a public data schema
    * describing the structure of a sharable dataset.

    ---
    <br/>

1. **What are examples of Schema Codes?**

    ⓘ Note: the following examples use fictitious domains.

    | Schema Code | Purpose |
    |-|-
    | [`nlweb.org/MSG` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MSG/🧩 Mgs.md>) | Schema of [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) 
    | [`nlweb.org/TOKEN` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/TOKEN/🧩 Token.md>) | Schema of [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>)
    | [`unicode.org/FLAG` 🧩](<../../../8 📜 Manifests/👥 any-igo.org/📜 unicode.any-igo.org.md>) | Flags for country [Prompts 🤔](<../05 💬 Chats/02 🤔 Prompt.md>)
    | [`locale.org/TERRITORY` 🧩](<../../../8 📜 Manifests/👥 any-igo.org/📜 locale.any-igo.org.md>) | Country names for [Prompts 🤔](<../05 💬 Chats/02 🤔 Prompt.md>)
    | [`standards.org/639-1` 🧩](<../../../8 📜 Manifests/👥 any-igo.org/📜 standards.any-igo.org.md>) | Language codes (e.g., `en-us`)

    ---
    <br/>

2. **What is contained in a Schema Code?**

    The string of a [Schema Code 🧩](<02 🧩 Schema Code.md>) is composed of the following parts.

    |#| Part |  Description
    |-|-|-
    |1| `domain` |  The [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that published the [Schema Code 🧩](<02 🧩 Schema Code.md>) in their [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>).
    |2| `code`    | A unique ID of the schema in the domain.
    |3| `version` | The optional version of the schema <br/>- formatted as `{major}.{minor}`.   
    |

    For example, 
    * the code `nlweb.com/TOKEN:2.0`  🧩 
    * references version `2.0` 
    * of a schema called `TOKEN` 
    * that is defined in the [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) 
    * of the [Authority 🏛️ domain](<../../40 👥 Domains/43 👍 Trusts/02 🏛️🛠️ Authority helper.md>) called `nlweb.com`. 
    
    ---
    <br/>

1. **How do versions work?**

    | | |
    |-|-
    | `MAJOR`| Are incompatible between versions:<br/>- i.e., a [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) expecting content on version `1.x` will not be able to read content on version `2.0`.
    | `minor`| Are retro-compatible within the same major, typically only adding new properties or updating descriptions: <br/> - i.e., a [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) expecting version `1.3` will be able to read version 1.7, although it will ignore the properties added after the expected version.

    ---
    <br/>

2. **Are versions mandatory?**

    Versions are always optional, but behave differently according to the situation.

    | Expectation | Behavior |
    |-|-
    | [📜 Manifest](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>)  | When a version is omitted in the [Schema Code 🧩](<02 🧩 Schema Code.md>) in its [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) definition, then it is assumed to be `1.0`.
    | [📨 Message](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) | When a version is omitted in a [domain Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>), then it is also assumed to be `1.0`.
    | [🕸 Graph](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) | When a version is omitted when calling [Schema @ Graph 🚀](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>), then the [🕸 Graph](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) returns the latest version.

    ---
    <br/>


3. **How are Schema Codes used in data sharing between domains?**
   
    When a [Consumer 💼 domain](<../27 💼 Consumers/04 💼🎭 Consumer role.md>) needs information stored in a [user's Vault 🗄️ domains](<03 🗄️🎭 Vault role.md>), 
    * it invokes the [Query @ Broker 🐌 API method](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) from the [user's Broker 🤵 domain](<../03 🤵 Brokers/03 🤵 Broker domain.md>), asking for datasets that comply with a given [Schema Code 🧩](<02 🧩 Schema Code.md>).

    For example, consider an airline requesting passport data for a flight check-in from a citizen with dual British and American nationalities:
    * the airline may ask for the `icao.int/PASSPORT`  [Schema Code 🧩](<02 🧩 Schema Code.md>)
    * and receive datasets from the user's `uk.gov` and `usa.gov` [Binds 🔗](<01 🔗 Bind.md>).
        ```yaml
        # Sample request to share user data.
        Header:
            From: any-consumer.com
            To: any-broker.com
            Subject: Query@Broker
        Body:
            ChatID: <chat-uuid>
            Codes:
              - icao.int/PASSPORT
              - usa.gov/DRIVER-LICENSE
        ```
     
    ---
    <br/>

4. **How can domains read Schemas in domain Manifests?**

    For resilience and performance, [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) cannot read [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) directly from the source.

    * Instead, [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) need to query [Graph 🕸 domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) for a schema definition, by passing the [Schema Code 🧩](<02 🧩 Schema Code.md>) to the [Schema @ Graph 🚀 API method](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>).

        ```yaml
        # Sample request to read a schema.
        Header: 
            From: any-domain.com
            To: any-graph.com
            Subject: Schema@Graph
        Body:
            Code: nlweb.org/LOCATOR:1.0
        ```

    ---

5. **What does it mean when a YAML content starts with 🤝?**

    When YAML content starts with `🤝: {Schema Code}`,
    * e.g., `🤝: nlweb.org/MANIFEST/CODE`
    * it means that the following YAML content should comply with the given [Schema Code 🧩](<02 🧩 Schema Code.md>) defined.
    * This allows readers to validate the YAML content by pulling the validation schema from the [Schema @ Graph 🚀 API method](<../../../6 🅰️ APIs/45 🕸🅰️ Graph/08 👥🚀🕸 Schema.md>).
    
    ---

6. **How do define a Schema in a Manifest?**

    The instructions on how to add a [Schema Code 🧩](<02 🧩 Schema Code.md>) to a [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) are themselves published as special [Schema Codes 🧩](<02 🧩 Schema Code.md>):

    | Schema | Description
    |-|-
    | [`nlweb.org/MANIFEST/CODE` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCode.md>) | CODE properties.
    | [`nlweb.org/MANIFEST/CODE/SCHEMA` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCodeSchema.md>) | CODE/SCHEMA properties.
    | [`nlweb.org/MANIFEST/DELEGATE` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestDelegate.md>) | Delegation to other [Authorities 🏛️](<../../40 👥 Domains/43 👍 Trusts/02 🏛️🛠️ Authority helper.md>).
    | [`nlweb.org/TYPES` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/TYPES/🧩 Types.md>) | Generic referenceable types.

    ---
    <br/>

7. **Does nlweb.org define Schema Codes?**

    Yes. 
    - The NLWeb protocol is supported by a set of [Schema Codes 🧩](<02 🧩 Schema Code.md>) defined in the `nlweb.org` [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>). 
    
    - This high-level manifest includes the schema definition for all communications explicitly supported by the core NLWeb protocol, but also a set of auxiliary schemas used to implement various business use cases. 

    ---

8. **Is the NLWeb Manifest a single point of failure?**

    No. 
    - [Domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) don't need `nlweb.org` to be online to access its [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>) (nor the one of any other [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>), for that matter).
    - Instead, [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) should rely on [Graph 🕸 helper domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) to look up schema definitions.

    ---


5. **Are NLWeb Schema definitions compatible with JSON Schema?**

    Yes. 
    - NLWeb schemas are defined by [JSON Schema](https://json-schema.org/understanding-json-schema/reference) converted to YAML.
    - Details are available at [`nlweb.org/MANIFEST/CODE/SCHEMA` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCodeSchema.md>).
  

    Consider the following example from [`standards.any-igo.org` 📜](<../../../8 📜 Manifests/👥 any-igo.org/📜 standards.any-igo.org.md>).

    ```yaml
    type: object
        required: [Code, Name]
        properties:
          Code: 
            oneOf:
              - type: string
                minLength: 2
                maxLength: 2
                example: en
              - type: string
                minLength: 5
                maxLength: 5
                example: en-us
          Name: 
            type: string
            example: English
    ```

    ---

6. **Wouldn't JSON be faster than YAML?**

    Yes, JSON is much faster than YAML. 
    - But, because of [Graph 🕸 helper domains](<../../40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>), the performance of either protocol is irrelevant in this context. 
    - NLWeb advocates for human readability, with YAML format allowing comments and being closer to structured natural language in this context.

    ---


1. **Can a Schema inherit from another Schema?**

    Yes.
    * Using the `Inherits` property
        * defined in [`nlweb.org/MANIFEST/CODE/SCHEMA` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCodeSchema.md>).
    * Consider [`nlweb.org/LOCATOR` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/LOCATOR/🧩 Locator.md>)
        * who defines properties `Code`, `Domain`, `Resource`.
    * It is inherited by [`nlweb.org/TOKEN` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/TOKEN/🧩 Token.md>)
        * who adds properties `Issued`, `Starts`, `Expires`, `Signature`.
    * Then inherited by [`nlweb.org/HOST/BOOKING` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/HOST/🧩 HostBooking.md>)
        * who adds properties `For`, `Time`, `Place`, `Seat`, `Latitude`, `Longitude`.
    
    ---
    <br/>


2. **Can a Schema reference another Schema?**

    Yes, 
    * using the `$ref` keyword from JSON Schema 
    * as defined in [`nlweb.org/MANIFEST/CODE/SCHEMA` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestCodeSchema.md>).
    
    Consider [`nlweb.org/MANIFEST` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 Manifest.md>):
    * it references [`nlweb.org/MANIFEST/IDENTITY` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestIdentity.md>)
        ```yaml
        Identity:
          $ref: nlweb.org/MANIFEST/IDENTITY:1.0
        ```
    * and references [`nlweb/MANIFEST/TRUST` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestTrust.md>).
        ```yaml
        Trusts:
        type: array
        items:
          $ref: nlweb.org/MANIFEST/TRUST:1.0
        ```
    
    ---
    <br/>

1. **Can a Schema reference a specific property of another Schema?**

    Yes.
    * See [`nlweb.org/MANIFEST/TRUST` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/MANIFEST/🧩 ManifestTrust.md>)
        * whose property `Domain`
        * references `Domain@nlweb.org/TYPES`
        * defined in [`nlweb.org/TYPES` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/TYPES/🧩 Types.md>).
    * See [`nlweb.org/PROFILE/ADDRESS` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/PROFILE/🧩 ProfileAddress.md>)
        * whose property `Country`
        * references `Alpha2@standards.any-igo.org/3166-1`
        * defined in [`standards.any-igo.org` 📜](<../../../8 📜 Manifests/👥 any-igo.org/📜 standards.any-igo.org.md>).

    ---
    <br/>