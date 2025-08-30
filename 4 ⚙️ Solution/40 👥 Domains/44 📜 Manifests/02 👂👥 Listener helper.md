👂 Listener domains FAQ
===

![](<.📎 Assets/📜 Listeners.png>)

1. **What is a Listener domain in NLWeb?**

    A Listener is a [🌬️ Streamer](<../41 📨 Comms/02 🌬️🎭 Streamer role.md>) domain that propagates [Manifest 📜](<01 📜 Domain Manifest.md>) updates. 

    ---

1. **Why are Listeners necessary?**

    NLWeb relies on a distributed cache of [Graphs 🕸](<03 🕸👥 Graph helper.md>), which allows Manifest-owners to go offline without impacting whoever needs the information contained in the Manifest. 
    * Listeners ensure that the cache in these Graphs is updated in near-real-time by propagating domain update notifications to Graphs. 

    ---

1. **How aren't Listeners and Graphs the same?**

    Because of the separation of responsibilities. 
    * While [Graphs 🕸](<03 🕸👥 Graph helper.md>) can be built by anyone, Listeners are a lightweight layer managed by a coordinated consortium of cloud providers.

    ---

1. **How do Listeners address resilience?**

    Listeners exist as a limited cluster of independent well-known nodes that listen to each other. 
    * For business continuity, all Listeners are built and managed by different organizations. 

    ---

1. **How do domains discover Listeners?**

    Domains can either contact a Listener directly, or they can use the NLWeb cluster at `listeners.nlweb.org`. 
    * NLWeb advocates for a combination of both, defaulting to the cluster, and falling back to a named Listener in case the cluster is compromised.

    ---

1. **What is contained in a Manifest-changed event?**

    An event from a domain comes inside an [envelope](<../41 📨 Comms/01 📨 Domain Message.md>) containing:
    - the change (e.g., CREATED, UPDATED, DELETED, RESEATED)
    - the path changed (e.g., `/Code/SSR/MEAL`)
    - the content of the Manifest that changed, if not deleted
    - the size of the content in bytes (e.g., `256`)

    ---

2. **What is the syntax of the path in the Manifest-changed event?**

    Paths allowed in Manifest-changed events are:
    * `Identity`, encompassing the Identity object of a Manifest;
    * `Trust/{key}`, containing a single [trust 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>) relationship identified by a unique key (e.g., `ssr-meals-airlines`);
    * `Code/{key}`, containing a single [Schema Code 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) definition identified by a unique key (e.g., `/SSR/MEAL`);
    * `Code/{key}:{version}`, containing a version of the schema definition for code identified (e.g., `Code/SSR/MEAL:1.0`);
    * `Delegate/{key}`, for a delegation identified by a unique key;
    * `Offer/{key}`, for an offer identified by a unique key.
    
    ---

3. **Do Listeners validate the content of events?**

    Yes. Listeners perform the following validations:
    - 1/ is the schema of the event correct?
    - 2/ is the size informed smaller than maximum allowed for events?
    - 3/ does the size of the change match the size informed?
    - 4/ does the path informed match a valid [Manifest 📜](<01 📜 Domain Manifest.md>) schema part?
    - 5/ is the schema of change correct for the path informed?

    ---

4. **How can domains know that their updates were rejected?**

    Listeners raise alerts when rejecting events. 
    * Interested domains should subscribe to that [🌬️ Streamer](<../41 📨 Comms/02 🌬️🎭 Streamer role.md>), filtering the domains they're interested in receiving alerts about.
    * For privacy reasons, some alerts are only be pushed to the subscriber domain that is referenced in the alert.

    ---

5. **Do Listeners read domain Manifests from the domain?**

    Not while reading events. 
    * [Manifest 📜](<01 📜 Domain Manifest.md>) events contain the content changed. 
    * However, domains may explicitly request Listeners to reset the domain's Manifest based on a content located in a given URL, as long as the content doesn't reach a maximum size for a Manifest.

    ---

6. **What are the size limits for events and Manifests?**

    * Manifest-changed events: 100 KB;
    * Manifest full content: 1 GB.

    ---

7. **Why is there a size limitation on events?**

    Limiting the size of Manifest-change events come with several benefits:

    * **Interoperability**: Cloud event buses have limited capacity to hold event content, with 256 KB being the lowest common denominator amongst the well-known cloud providers - this about 30 pages of a narrative.

    * **Simplicity**: by limiting the size of the events, NLWeb allows changes to be propagated across many cloud providers without the need for round trips (i.e., returning to the origin to download the content).

    * **Scalability**: multiple small events can scale horizontally, virtually to infinite, by using cloud functions with small memory footprints - otherwise, single download of the [Manifest 📜](<01 📜 Domain Manifest.md>) of an [🏛️ Authority](<../43 👍 Trusts/02 🏛️👥 Authority helper.md>) could require several gigabytes of memory to be parsed.

    ---

8. **Why is there a size limitation on the entire Manifest?**

    Domains may ask Graphs and Listeners to download their Manifest for drift detection and sync reset. 
    - For that, the entire content of the Manifest needs to be in memory, with 1 GB being the minimum common denominator for functions among the well-known cloud providers.

    ---

9. **How can domains keep Manifest-change events small?**

    Domains can apply the following techniques to keep [Manifest 📜](<01 📜 Domain Manifest.md>) parts small:
    - follow the Manifest Schema to break the Manifest into valid paths (e.g., `Identity`);
    - separate lists into item-level parts (e.g., for `Trusts`, `Codes`, and `Delegates`);
    - further break [Schema Codes 🧩](<../../20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) by using Code references;
    - write each part to key-value stores that support change notifications (e.g., object stores and NoSQL databases);
    - when creating and updating Manifest parts, keep each part below 200 KB.
    
    ---

10. **Do Listeners propagate all notifications downstream?**

    Not necessarily. 
    - Listener subscribers can filter the events they subscribe to.

    ---

11. **What's the retention commitment of Listeners?**

    Listeners keep all changes from all domain [Manifests 📜](<01 📜 Domain Manifest.md>) and public keys indefinitely. 

    ---

12. **How are new Listener nodes added to the cluster?**

    New nodes first rebase by replaying NLWeb's history from another Listener, then join the cluster.

    ---

13. **What if a subscriber wants to read all history?**

    Subscribers can ask Listeners to replay all domain updates in a given period, or from the beginning of times.

    ---

14. **What if a subscriber goes offline?**

    Listeners have a retry policy, as defined by the Streamer role. Nonetheless, subscribers are advised to bind to [⏳ Buffer](<../41 📨 Comms/03 ⏳👥 Buffer helper.md>) domains to increase resilience.

    ---

15. **How to deploy a new Listener?**

    Subscribe to another two Listeners and replay the entire history from one of them.

    ---

16. **Is there data loss when a Listener goes down?**

    No. 
    * Each Listener is fully independent, being responsible for replying the entire history of domain Manifest changes, even if it is the only Listener available in the cluster. 
    * All Listeners are fully subscribed to one another, ensuring that one domain notification arriving in any Listener will be propagated to all other Listeners in the cluster. 
    * This configuration allows any graph to subscribe to any Listener, confident that all Listeners will eventually hold the same data. 

    ---

17. **How do Listeners avoid infinite loop cycles?**

    Listeners propagate the correlation ID sent by the original domain, discarding any repeated update notifications.

    ---

18. **Can an attacker compromises all cluster nodes?**    

    No. Each Listener in the cluster node is managed by a different organization, and implemented with different technologies, making it hard for an attacker to replicate an attack on all cluster nodes.

    ---

19. **How to identify if a Listener was compromised?**

    [Firewalls 🔥](<../43 👍 Trusts/03 🔥👥 Firewall helper.md>) monitor the behavior of any Listener and match domain information with other Listeners. If necessary, Firewalls immediately revoke a Listener's [trust 👍](<../43 👍 Trusts/01 👍 Domain Trust.md>).

    ---

20. **Is the cluster endpoint a single point of failure?**

    No. 
    * The NLWeb cluster endpoint is a latency-based routing visible at a well-known DNS name (`listeners.nlweb.org`). 
    * While this endpoint is managed by the NLWeb foundation under the supervision of a consortium of multiple cloud providers, domains should nonetheless fall back to using a specific Listener node in case the cluster is unavailable.

    ---

21. **How can a subscriber filter notifications by content?**

    Subscribers can set a filter when subscribing to Listeners 
    - e.g., a financial regulator may only want notifications about changes in domains referencing bank Schema Codes.

    ---
