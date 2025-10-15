👂 Listener helper domains
===


1. **What is a Listener domain in NLWeb?**

    A [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) is 
    * a [Helper 🛠️ domain](<../../45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) 
    * with a [Streamer 🌬️ domain role](<../../41 🎭 Domain Roles/75 🌬️ Streamers/$ 🌬️🎭 Streamer role.md>) 
    * that propagates [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) updates. 

    ---
    <br/>

1. **How do Listeners work?**

    ![](<.📎 Assets/📜 Listeners.png>)

    |#|Step
    |-|-
    |1| [Domains 👥](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) publish their [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) updates to the DNS endpoint of the global Listeners 👂 cluster. As a fallback, the same updates may be sent to an individual [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>).
    |2| The cluster DNS routes the update messages to the best [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) based on latency.
    |3| Listeners 👂 replicate the update messages amongst all [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) of the cluster.
    |4| Each [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) performs a fan-out propagation of update events to all [Graph 🕸 helper domains](<../40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) that [subscribed 🔔](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>) to the Listener's 👂 [domain-event Stream 🌬️](<../../41 🎭 Domain Roles/75 🌬️ Streamers/$ 🌬️🎭 Streamer role.md>).

    ---
    <br/>

1. **Why are Listeners necessary?**

    NLWeb relies on a distributed cache of [Graph 🕸 helper domains](<../40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>), which allows Manifest-owners to go offline without impacting whoever needs the information contained in the [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>). 
    * [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) ensure that the cache in these [Graph 🕸 domains](<../40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) is updated in near-real-time by propagating domain update notifications to [Graph 🕸 domains](<../40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>). 

    ---
    <br/>

1. **How aren't Listeners and Graphs the same?**

    Because of the separation of responsibilities. 
    * While [Graph 🕸 domains](<../40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) can be built by anyone, [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) are a lightweight layer managed by a coordinated consortium of cloud providers.

    ---
    <br/>

1. **How do Listeners address resilience?**

    [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) exist as a limited cluster of independent well-known nodes that listen to each other. 
    * For business continuity, all [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) are built and managed by different organizations. 

    ---
    <br/>

1. **How do domains discover Listeners?**

    Domains can either contact a [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) directly, or they can use the NLWeb cluster at `listeners.nlweb.org`. 
    * NLWeb advocates for a combination of both, defaulting to the cluster, and falling back to a named [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) in case the cluster is compromised.

    ---
    <br/>

1. **What is contained in a Manifest-changed event?**

    An event from a [domain 👥](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) about a [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) change comes inside an [envelope 📨](<../../40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>) containing the following properties.

    |Property | Description
    |-|-
    |`Change`| `CREATED`, `UPDATED`, `DELETED`, `RESEATED`
    |`Path`| The location changed, e.g. `Code/SSR/MEAL`
    |`Content`| The content that changed, if not deleted
    | `Size`| The Byte sizes of the content compacted in JSON
    |

    Consider the following example.
    ```yaml
    Change: CREATED
    Path: Codes[Path=/SSR]
    Content: 
        Path: /SSR
        Delegator: airlines.any-igo.org
    Size: 50
        # Size in Bytes of the string
        # {"Path":"/SSR","Delegator":"airlines.any-igo.org"}
    ```
    
    ---
    <br/>

1. **What is the syntax of the path in the Manifest-changed event?**

    Paths allowed in Manifest-changed events are as follows.

    | Path | Description | Example
    |-|-|-
    | `Identity` | Encompassing the Identity object of a [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>). | `Identity`
    | `Trust/{key}` | Containing a single [Trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) relationship identified by a unique key. | `Trust/my-key`
    | `Code/{key}` | Containing a single [Schema Code 🧩](<../../25 Data/Schema Codes/02 🧩 Schema Code.md>) definition identified by a unique key. | `Code/SSR/MEAL`
    | `Code/{key}:{version}` | Containing a version of the schema definition for [Schema Code 🧩](<../../25 Data/Schema Codes/02 🧩 Schema Code.md>) identified. | `Code/SSR/MEAL:1.0`
    | `Delegate/{key}` | For a delegation identified by a unique key. | `Delegate/my-key`
    | `Offer/{key}` | For an offer identified by a unique key. | `Offer/my-key`
    
    ---
    <br/>

1. **Do Listeners validate the content of events?**

    Yes. [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) perform the following validations:
    - is the schema of the event correct?
    - is the size informed smaller than maximum allowed for events?
    - does the size of the change match the size informed?
    - does the path informed match a valid [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) schema part?
    - is the schema of change correct for the path informed?

    ---
    <br/>

1. **How can domains know that their updates were rejected?**

    [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) raise alerts when rejecting events. 
    * Interested [domains 👥](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) should [subscribe 🔔](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>) to that [Stream 🌬️](<../../41 🎭 Domain Roles/75 🌬️ Streamers/$ 🌬️🎭 Streamer role.md>), filtering the domains they're interested in receiving alerts about.
    * For privacy reasons, some alerts are only be pushed to the [Subscriber 🔔 domain](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>) that is referenced in the alert.

    ---
    <br/>

1. **Do Listeners read domain Manifests from the domain?**

    Not while reading events. 
    * [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) events contain the content changed. 
    * However, [domains 👥](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) may explicitly request [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) to reset the domain's [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) based on a content located in a given URL, as long as the content doesn't reach a maximum size for a [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>).

    ---
    <br/>

1. **What are the size limits for events and Manifests?**

    * Manifest-changed events: 100 KB;
    * [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) full content: 1 GB.

    ---
    <br/>

1. **Why is there a size limitation on events?**

    Limiting the size of Manifest-change events come with several benefits:

    * **Interoperability**: Cloud event buses have limited capacity to hold event content, with 256 KB being the lowest common denominator amongst the well-known cloud providers - this about 30 pages of a narrative.

    * **Simplicity**: by limiting the size of the events, NLWeb allows changes to be propagated across many cloud providers without the need for round trips (i.e., returning to the origin to download the content).

    * **Scalability**: multiple small events can scale horizontally, virtually to infinite, by using cloud functions with small memory footprints - otherwise, single download of the [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) of an [🏛️ Authority](<../../45 🛠️ Helper domains/14 🏛️ Authorities/$ 🏛️🛠️ Authority helper.md>) could require several gigabytes of memory to be parsed.

    ---
    <br/>

1. **Why is there a size limitation on the entire Manifest?**

    Domains may ask [Graph 🕸 domains](<../40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) and [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) to download their [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) for drift detection and sync reset. 
    - For that, the entire content of the [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) needs to be in memory, with 1 GB being the minimum common denominator for functions among the well-known cloud providers.

    ---
    <br/>

1. **How can domains keep Manifest-change events small?**

    Domains can apply the following techniques to keep [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) parts small:
    - follow the Manifest Schema to break the Manifest into valid paths (e.g., `Identity`);
    - separate lists into item-level parts (e.g., for `Trusts`, `Codes`, and `Delegates`);
    - further break [Schema Codes 🧩](<../../25 Data/Schema Codes/02 🧩 Schema Code.md>) by using Code references;
    - write each part to key-value stores that support change notifications (e.g., object stores and NoSQL databases);
    - when creating and updating [Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) parts, keep each part below 200 KB.
    
    ---
    <br/>

1. **Do Listeners propagate all notifications downstream?**

    Not necessarily. 
    - [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>) can filter the events they subscribe to.

    ---
    <br/>

1. **What's the retention commitment of Listeners?**

    [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) keep all changes from all domain [Manifests 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) and public keys indefinitely. 

    ---
    <br/>

1. **How are new Listener nodes added to the cluster?**

    New nodes first rebase by replaying NLWeb's history from another [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>), then join the cluster.

    ---
    <br/>

1. **What if a subscriber wants to read all history?**

    [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>) can ask [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) to replay all domain updates in a given period, or from the beginning of times.

    ---
    <br/>

1. **How to deploy a new Listener?**

    Subscribe to another two [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) and replay the entire history from one of them.

    ---
    <br/>

1. **Is there data loss when a Listener goes down?**

    No. 
    * Each [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) is fully independent, being responsible for replying the entire history of [domain Manifest 📜](<../../40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>) changes, even if it is the only [Listener 👂 node](<$ 👂🛠️ Listener helper.md>) available in the cluster. 
    * All [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) are fully subscribed to one another, ensuring that one domain notification arriving in any [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) will be propagated to all other [Listener 👂 nodes](<$ 👂🛠️ Listener helper.md>) in the cluster. 
    * This configuration allows any graph to subscribe to any [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>), confident that all [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) will eventually hold the same data. 

    ---
    <br/>

1. **How do Listeners avoid infinite loop cycles?**

    [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>) propagate the correlation ID sent by the original [domain 👥](<../../40 👥 Domains/41 📨 Messages/00 👥 Domain.md>), discarding any repeated update notifications.

    ---
    <br/>

1. **Can an attacker compromises all cluster nodes?**    

    No. 
    * Each [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) in the cluster node is managed by a different organization, and implemented with different technologies, making it hard for an attacker to replicate an attack on all cluster nodes.

    ---
    <br/>

1. **How to identify if a Listener was compromised?**

    [Firewall 🔥 helper domains](<../../45 🛠️ Helper domains/21 🔥 Firewalls/$ 🔥🛠️ Firewall helper.md>) monitor the behavior of any [Listener 👂 domain](<$ 👂🛠️ Listener helper.md>) and match domain information with other [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>). 
    * If necessary, [Firewall 🔥 domains](<../../45 🛠️ Helper domains/21 🔥 Firewalls/$ 🔥🛠️ Firewall helper.md>) immediately revoke a Listener's [trust 👍](<../../40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>).

    ---
    <br/>

1. **Is the cluster endpoint a single point of failure?**

    No. 
    * The NLWeb cluster endpoint is a latency-based routing visible at a well-known DNS name (`listeners.nlweb.org`). 
    * While this endpoint is managed by the NLWeb foundation under the supervision of a consortium of multiple cloud providers, domains should nonetheless fall back to using a specific [Listener 👂 node](<$ 👂🛠️ Listener helper.md>) in case the cluster is unavailable.

    ---
    <br/>

1. **How can a subscriber filter notifications by content?**

    [Subscriber 🔔 domains](<../../41 🎭 Domain Roles/76 🔔 Subscribers/$ 🔔🎭 Subscriber role.md>) can set a filter when subscribing to [Listener 👂 domains](<$ 👂🛠️ Listener helper.md>):
    - e.g., a financial regulator may only want notifications about changes in domains referencing bank [Schema Codes 🧩](<../../25 Data/Schema Codes/02 🧩 Schema Code.md>).

    ---
    <br/>
