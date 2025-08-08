👍 NLWeb Trust Framework FAQ
===

![](<.📎 Assets/👍 Trust Framework.png>)

1. **How do domains avoid interacting with bad actors?**

    The NLWeb implements a domain trust framework that allows sender domains to know if they can trust a receiver domain with a specific subject, and receivers to know if they can trust a specific subject from a sender (e.g., `any-buyer.com` accepts payment requests from `any-seller.com`, but not from `any-scammer.com`). 

    ---

1. **How to trust an unknown domain trusted by others?**
    
    A domain may trust an unknown domain on a specific subject if there’s a trusted third domain advocating on behalf of the unknown one (e.g., `any-buyer.com` accepts payment requests from all domains whose payment requests are also trusted by `any-nation.com`). 

    ---

1. **How is it related to the Gaia-X initiative?**

    The NLWeb and the *Gaia-X Trust Frameworks* share the same goal: to safeguard data protection, transparency, security, portability, and flexibility within their ecosystems. However, they have different geopolitical ambitions and technical approaches.

    ---

1. **How are time-bounded agreements represented?**

    Trusts can have an expiration date, allowing domains to set an end-date to a trust (e.g., `any-country.com` may allow temporary visa-less immigration during an international soccer event).

    ---

1. **How can legal bans be imposed nation-wide?**

    Trusts can be granted or revoked. 
    
    A sovereign domain may revoke a trust on another domain to explicitly break indirect trust-chains for that other domain (e.g., `any-nation.com` may impose a ban on `sanctioned-domain.com` on the basis of terrorism, telling all the business that rely on `any-nation.com`’s indirect trust to cease interactions with the banned domain, while allowing those businesses to exceptionally override the indirect revoke with a direct grant).

    ---

1. **How are immediate security bans imposed?**

    To protect themselves from harmful actors, domains may inherit all revokes from Firewall domains to immediately block any new threat, regardless of any direct or indirect trust to the harmful actor (e.g., if `any-firewall.com` revokes `any-threat.com`, and `any-domain.com` inherits Trusts from `any-firewall.com`, then `any-domain.com` won’t communicate with `any-threat.com` event if there are direct or indirect Trusts from `any-domain.com` to `any-threat.com`). 

    ---

1. **Why not using the PKI (rfc5280) to handle domain trust?**

    The *Public Key Infrastructure (PKI)* is already used by *Certificate Authorities (CAs)* to access if domains can be trusted, both directly and indirectly. 
    
    However, its binary decision don’t allow for complex scenarios like:
    - 1/ partial Trusts by subject (e.g., 
        - `A` trusts `B` for `X` but not `Y`); 
    - 2/ asymmetric Trusts by subject (e.g., 
        - `A` trusts `B` for `X` but not `Y`, 
        - while `B` trusts `A` for `Y` but not `X`);
    - 3/ override modes (e.g., 
        - direct grants prevail over indirect revokes, 
        - while inheritance revokes prevail over all grants).

    ---

1. **How to calculate indirect trust paths when nodes are down?**

    Domains can rely on [Graphs 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>):
    - these keep up-to-date graph representations of all possible trust-paths between two domains, allowing Trust paths to be queried even when the domains comprising the nodes of those paths are unavailable 
    - e.g., `any-domain.com` can ask `any-graph.com` if `any-seller.com` can be trusted for payment requests.

    ---

1. **How can domains know when another domain lost trust in them?**

    Domains can rely on [Graphs 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>):
    - these can detect trust removals and notify affected subscribers;
    - e.g., `any-graph.com` may inform `any-domain.com` whenever `any-seller.com` explicitly adds or removes a trust to `any-domain.com`.


    ---
2. **How can domains know when indirect trust changes affect them?**

    Domains can rely on [Graphs 🕸](<../44 📜 Manifests/03 🕸👥 Graph helper.md>):
    - these can monitor for changes in specific trust paths that may affect an indirect trust relationship;
    - a typical scenario is an inter-governmental agreement where two entities from different countries trust each other indirectly because their government bodies trust each other;
    - e.g., `any-graph.com` may monitor a trust path between `bank-of-nation-1.com` and `bank-of-nation-2.com`, checking for changes like `nation-1.org` removing a trust to `nation-2.org` or `nation-2.org` removing a trust to `bank-of-nation-2.com`.