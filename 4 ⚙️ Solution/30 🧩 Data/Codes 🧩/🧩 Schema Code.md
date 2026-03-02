🧩 Schema Codes
===

1. **What is a Schema Code?**

    A [Schema 🧩](<🧩 Schema Code.md>) is a string 
    * formatted as `{authority}/{code}[:{version}]`
    * e.g., `pollyweb.org/HOST:1.0`
    * that points to a public data schema
    * describing the structure of a sharable dataset.

    ---
    <br/>

1. **What are examples of Schema Codes?**

    ⓘ Note: the following examples use fictitious domains.

    | Schema Code | Purpose |
    |-|-
    | [`.MSG` 🧩](<../Messages 📨/📨🧩 Message schemas/🧩 MSG.md>) | Schema of [Messages 📨](<../Messages 📨/📨 Message/📨 Message.md>) 
    | [`.TOKEN` 🧩](<../Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>) | Schema of [Tokens 🎫](<../Tokens 🎫/🎫 Token/🎫 Token.md>)
    | [`unicode.org/FLAG` 🧩](<../../../8 📜 Manifests/👥 any-igo.dom/📜 unicode.any-igo.dom.md>) | Flags for country [Prompts 🤔](<../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)
    | [`locale.org/TERRITORY` 🧩](<../../../8 📜 Manifests/👥 any-igo.dom/📜 locale.any-igo.dom.md>) | Country names for [Prompts 🤔](<../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)
    | [`standards.org/639-1` 🧩](<../../../8 📜 Manifests/👥 any-igo.dom/📜 standards.any-igo.dom.md>) | Language codes (e.g., `en-us`)

    ---
    <br/>

1. **What is contained in a Schema Code?**

    The string of a [Schema 🧩](<🧩 Schema Code.md>) is composed of the following parts.

    |#| Part |  Description
    |-|-|-
    |1| `domain` |  The [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) that published the [Schema 🧩](<🧩 Schema Code.md>) in their [domain Manifest 📜](<../Manifests 📜/📜 Manifest/📜 Manifest.md>).
    |2| `code`    | A unique ID of the schema in the domain.
    |3| `version` | The optional version of the schema <br/>- formatted as `{major}.{minor}`.   
    |

    For example, 
    * the code `pollyweb.org/TOKEN:2.0`  🧩 
    * references version `2.0` 
    * of a schema called `TOKEN` 
    * that is defined in the [domain Manifest 📜](<../Manifests 📜/📜 Manifest/📜 Manifest.md>) 
    * of the [Authority 🏛️ domain](<../../45 🤲 Helper domains/Authorities 🏛️/🏛️🤲 Authority helper.md>) called `pollyweb.org`. 
    
    For readability:
    * given that `pollyweb.org` schemas will be widely used, 
    * a dot can be used as a prefix of `pollyweb.org/`
    * e.g., `.TOKEN` is the same as `pollyweb.org/TOKEN:1.0`
  
    ---
    <br/>

1. **How do versions work?**

    | | |
    |-|-
    | `MAJOR`| Are incompatible between versions:<br/>- i.e., a [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) expecting content on version `1.x` will not be able to read content on version `2.0`.
    | `minor`| Are retro-compatible within the same major, typically only adding new properties or updating descriptions: <br/> - i.e., a [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) expecting version `1.3` will be able to read version 1.7, although it will ignore the properties added after the expected version.

    ---
    <br/>

1. **Are versions mandatory?**

    Versions are always optional, but behave differently according to the situation.

    | Expectation | Behavior |
    |-|-
    | [📜 Manifest](<../Manifests 📜/📜 Manifest/📜 Manifest.md>)  | When a version is omitted in the [Schema 🧩](<🧩 Schema Code.md>) in its [domain Manifest 📜](<../Manifests 📜/📜 Manifest/📜 Manifest.md>) definition, then it is assumed to be `1.0`.
    | [📨 Message](<../Messages 📨/📨 Message/📨 Message.md>) | When a version is omitted in a [domain Messages 📨](<../Messages 📨/📨 Message/📨 Message.md>), then it is also assumed to be `1.0`.
    | [🕸 Graph](<../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>) | When a version is omitted when calling [`Schema@Graph`](<../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Schema/🕸 Schema 🚀 call.md>), then the [🕸 Graph](<../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>) returns the latest version.

    ---
    <br/>


1. **How are Schema Codes used in data sharing between domains?**
   
    When a [Consumer 💼 domain](<../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) needs information stored in a [user's Vault 🗄️ domains](<../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>), 
    * it invokes the [`Query@Broker`](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) from the [user's Broker 🤵 domain](<../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>), asking for datasets that comply with a given [Schema 🧩](<🧩 Schema Code.md>).

    For example, consider an airline requesting passport data for a flight check-in from a citizen with dual British and American nationalities:
    * the airline may ask for the `icao.int/PASSPORT`  [Schema 🧩](<🧩 Schema Code.md>)
    * and receive datasets from the user's `uk.gov` and `usa.gov` [Binds 🔗](<../Binds 🔗/🔗 Bind.md>).
        ```yaml
        # Sample request to share user data.
        Header:
            From: any-consumer.dom
            To: any-broker.dom
            Subject: Query@Broker
        Body:
            Chat: <chat-uuid>
            Schemas:
              - icao.int/PASSPORT
              - usa.gov/DRIVER-LICENSE
        ```
     
    ---
    <br/>

1. **How can domains read Schemas in domain Manifests?**

    For resilience and performance, [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) cannot read [domain Manifest 📜](<../Manifests 📜/📜 Manifest/📜 Manifest.md>) directly from the source.

    * Instead, [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) need to query [Graph 🕸 domains](<../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>) for a schema definition, by passing the [Schema 🧩](<🧩 Schema Code.md>) to the [`Schema@Graph`](<../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Schema/🕸 Schema 🚀 call.md>).

        ```yaml
        # Sample request to read a schema.
        Header: 
            From: any-domain.dom
            To: any-graph.dom
            Subject: Schema@Graph
        Body:
            Schema: .LOCATOR:1.0
        ```

    ---
    <br/>

1. **What does it mean when a YAML content starts with 🤝?**

    When YAML content starts with `🤝: {Schema Code}`,
    * e.g., `🤝:` [`.MANIFEST/CODE`](<../Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)
    * it means that the following YAML content should comply with the given [Schema 🧩](<🧩 Schema Code.md>) defined.
    * This allows readers to validate the YAML content by pulling the validation schema from the [`Schema@Graph`](<../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Schema/🕸 Schema 🚀 call.md>).
    
    ---
    <br/>

1. **How do define a Schema in a Manifest?**

    The instructions on how to add a [Schema 🧩](<🧩 Schema Code.md>) to a [domain Manifest 📜](<../Manifests 📜/📜 Manifest/📜 Manifest.md>) are themselves published as special [Schema Codes 🧩](<🧩 Schema Code.md>):

    | Schema | Description
    |-|-
    | [`.MANIFEST/CODE` 🧩](<../Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>) | CODE properties
    | [`.MANIFEST/DELEGATE` 🧩](<../Manifests 📜/📜🧩 Manifest schemas/🧩 DELEGATE.md>) | Delegation to other [Authorities 🏛️](<../../45 🤲 Helper domains/Authorities 🏛️/🏛️🤲 Authority helper.md>)
    | [`.TYPES` 🧩](<../../../7 🧩 Codes/$/🧩 TYPES.md>) | Generic referenceable types

    ---
    <br/>

1. **Does pollyweb.org define Schema Codes?**

    Yes. 
    - The PollyWeb protocol is supported by a set of [Schema Codes 🧩](<🧩 Schema Code.md>) defined in the `pollyweb.org` [domain Manifest 📜](<../Manifests 📜/📜 Manifest/📜 Manifest.md>). 
    
    - This high-level manifest includes the schema definition for all communications explicitly supported by the core PollyWeb protocol, but also a set of auxiliary schemas used to implement various business use cases. 

    ---
    <br/>

1. **Is the PollyWeb Manifest a single point of failure?**

    No. 
    - [Domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) don't need `pollyweb.org` to be online to access its [domain Manifest 📜](<../Manifests 📜/📜 Manifest/📜 Manifest.md>) (nor the one of any other [domain 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>), for that matter).
    - Instead, [domains 👥](<../../40 👥 Domains/👥 Domain/👥 Domain.md>) should rely on [Graph 🕸 helper domains](<../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>) to look up schema definitions.

    ---
    <br/>


1. **Are PollyWeb Schema definitions compatible with JSON Schema?**

    Yes. 
    - PollyWeb schemas are defined by [JSON Schema](https://json-schema.org/understanding-json-schema/reference) converted to YAML.
    - Details are available at [`pollyweb.org/MANIFEST/CODE` 🧩](<../Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>).
  

    Consider the following example from [`standards.any-igo.dom` 📜](<../../../8 📜 Manifests/👥 any-igo.dom/📜 standards.any-igo.dom.md>).

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
    <br/>

1. **Wouldn't JSON be faster than YAML?**

    Yes, JSON is much faster than YAML. 
    - But, because of [Graph 🕸 helper domains](<../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>), the performance of either protocol is irrelevant in this context. 
    - PollyWeb advocates for human readability, with YAML format allowing comments and being closer to structured natural language in this context.

    ---
    <br/>


1. **Can a Schema inherit from another Schema?**

    Yes.
    * Using the `Inherits` property
        * defined in [`.MANIFEST/CODE` 🧩](<../Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>).
    * Consider [`.LOCATOR` 🧩](<../../../7 🧩 Codes/$/🧩 LOCATOR.md>)
        * who defines properties `Schema`, `Domain`, `Resource`.
    * It is inherited by [`.TOKEN` 🧩](<../Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>)
        * who adds properties `Issued`, `Starts`, `Expires`, `Signature`.
    * Then inherited by [`.HOST/BOOKING` 🧩](<../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST'BOOKING.md>)
        * who adds properties `For`, `Time`, `Place`, `Seat`, `Latitude`, `Longitude`.
    
    ---
    <br/>


1. **Can a Schema reference another Schema?**

    Yes, 
    * using the `$ref` keyword from JSON Schema 
    * as defined in [`.MANIFEST/CODE` 🧩](<../Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>).
    
    Consider [`.MANIFEST` 🧩](<../Manifests 📜/📜 Manifest/📜 Manifest.md>):
    * it references [`.MANIFEST/ABOUT` 🧩](<../Manifests 📜/📜🧩 Manifest schemas/🧩 ABOUT.md>)
        ```yaml
        About:
          $ref: pollyweb.org/MANIFEST/ABOUT:1.0
        ```
    * and references [`.MANIFEST/TRUST` 🧩](<../Manifests 📜/📜🧩 Manifest schemas/🧩 TRUST.md>).
        ```yaml
        Trusts:
        type: array
        items:
          $ref: pollyweb.org/MANIFEST/TRUST:1.0
        ```
    
    ---
    <br/>

1. **Can a Schema reference a specific property of another Schema?**

    Yes.
    * See [`.MANIFEST/TRUST` 🧩](<../Manifests 📜/📜🧩 Manifest schemas/🧩 TRUST.md>)
        * whose property `Domain`
        * references `Domain@.TYPES`
        * defined in [`.TYPES` 🧩](<../../../7 🧩 Codes/$/🧩 TYPES.md>).
    * See [`.PERSONA/ADDRESS` 🧩](<../../50 🫥 Agent domains/Personas 🧢/🧢🧩 Persona schemas/🧩 ADDRESS.md>)
        * whose property `Country`
        * references `Alpha2@standards.any-igo.dom/3166-1`
        * defined in [`standards.any-igo.dom/3166-1` 📜](<../../../8 📜 Manifests/👥 any-igo.dom/📜 standards.any-igo.dom.md>).

    ---
    <br/>