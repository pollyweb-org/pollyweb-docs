👍 Domain Trust Framework
===

![](<.📎 Assets/👍 Trust Framework.png>)

1. **How do domains avoid interacting with bad actors?**

    The NLWeb implements a domain trust framework that allows:
    * [sender domains 📤](<../👥 Domains/👥 Domain.md>) to know if they can [trust 👍](<👍 Domain Trust.md>) a [receiver domain 📥](<../👥 Domains/👥 Domain.md>) with a specific [Schema Code 🧩](<../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) path - e.g. `nlweb.org/PERSONA/*`, and vice-versa.
    
    For example:
      * `any-buyer.com` may accept payment requests 
      * from `any-seller.com` 💸
      * but not from `any-scammer.com` 🦹‍♂️. 

    ---
    <br/>

1. **How to define Trust relationships?**

    [Trusts 👍](<👍 Domain Trust.md>) 
    * are defined in [domain Manifests 📜](<../👥📜 Domain Manifests/📜 Manifest.md>) 
    * using the schema code [nlweb.org/MANIFEST/TRUST 🧩](<../👥📜 Domain Manifests/🧩 Manifest schemas/🧩 TRUST.md>).

    ```yaml
    # Trust example
    - Title: My trust                     # Optional
      Expires: '2050-01-01T10:00:00.000Z' # Empty = forever
      Action: GRANT                       # Empty = grant
      Roles: CONSUMER                     # Empty = both
      Query: nlweb.org/PERSONA/*          # Empty = anything
      Domain: nlweb.org                   # Empty = everyone
    ```

    Property | Type | Description
    |-|-|-
    `Title`          | string | Optional description
    `Expires`        |timestamp| Expiration date:<br/>• default: forever
    `Action`         |enum| Giving or removing trust: <br/>• enum: [GRANT, REVOKE, INHERIT] <br/>• default: GRANT
    `Role`<br/>`Roles`     |enum,<br/>enum[]| Purpose of referred actor:<br>• enum: [VAULT, CONSUMER, *] <br/>• default: both
    `Query`<br/>`Queries`  |string,<br/>string[]| [Schema Code 🧩](<../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)  paths to trust: <br/>• default: everything
    `Domain`<br/>`Domains` |string,<br/>string[] | Domains to trust: <br/>• default: everyone

    ---
    <br/>

1. **How to trust an unknown domain trusted by others?**
    
    A [domain 👥](<../👥 Domains/👥 Domain.md>) may trust an unknown domain on a specific subject if there’s a [trust 👍](<👍 Domain Trust.md>) third domain advocating on behalf of the unknown one;   
    * e.g., `any-buyer.com` accepts payment requests from all domains 
    * whose payment requests are also [trust 👍](<👍 Domain Trust.md>) by `any-nation.com`. 
  
    Consider the following example for Special Service Requests (SSR) in aviation.

    * [U.S. Government 📜](<../../../8 📜 Manifests/👥 usa.gov/📜 usa.gov.md>) allows airlines to ask SSR from U.S. citizens.
        ```yaml
        # 📜 usa.gov 

        - Role: CONSUMER          # Inbound allowed
          Query: iata.org/SSR/*   # for SSR info
          Domain: iata.org        # from IATA
        ```

    * The [International Air Transport Association (IATA) 📜](<../../../8 📜 Manifests/👥 any-igo.org/📜 airlines.any-igo.org.md>) requests SSR info from U.S. citizens, and allows airlines to share SSR info between them. 
    
        ```yaml
        # 📜 iata.org

        - Role: VAULT             # Outbound allowed
          Query: iata.org/SSR/*   # for SSR info
          Domain: usa.gov         # to the U.S.

        - Query: iata.org/SSR/*   
          Domains:
            - flytap.com           # TAP Air Portugal
            - ba.com               # British Airways
        ```
    
    * British Airways (ba.com) can now send SSR requests to the U.S. Government because IATA is bridging the relationship.

    ---
    <br/>

1. **How is it related to the Gaia-X initiative?**

    The NLWeb and the *Gaia-X Trust Frameworks* share the same goal: to safeguard data protection, transparency, security, portability, and flexibility within their ecosystems. 
    * However, they have different geopolitical ambitions and technical approaches.

    ---
    <br/>

1. **How are time-bounded agreements represented?**

    [Trusts 👍](<👍 Domain Trust.md>) can have an expiration date, allowing domains to set an end-date to a [trust 👍](<👍 Domain Trust.md>);
    - e.g., `any-country.com` may allow temporary visa-less immigration during an international soccer event.

    ---
    <br/>

1. **How can legal bans be imposed nation-wide?**

    [Trust 👍](<👍 Domain Trust.md>) can be granted or revoked. 
    
    * A sovereign domain may revoke a [trust 👍](<👍 Domain Trust.md>) on another domain to explicitly break indirect trust-chains for that other domain;
  
    * e.g., `any-nation.org` may impose a ban on `sanctioned-domain.com` on the basis of terrorism, telling all the business that rely on `any-nation.org`’s indirect [trust 👍](<👍 Domain Trust.md>) to cease interactions with the banned domain, while allowing those businesses to exceptionally override the indirect revoke with a direct grant.

        ```yaml
        # 📜 any-nation.org
        - Action: REVOKE
          Domain: sanctioned-domain.com
        ```

        ```yaml
        # 📜 any-domain.com
        - Domain: any-nation.com
        - Domain: sanctioned-domain.com
        ```

    ---
    <br/>

1. **How are immediate security bans imposed?**

    To protect themselves from harmful actors,
    *  [domains 👥](<../👥 Domains/👥 Domain.md>)s may inherit all revokes from [Firewall 🔥 domains](<../../45 🤲 Helper domains/Firewalls 🔥/🔥🤲 Firewall helper.md>) to immediately block any new threat, regardless of any direct or indirect [trust 👍](<👍 Domain Trust.md>) to the harmful actor;
    
    e.g., if `any-firewall.com` revokes `any-threat.com`, 
    *  and `any-domain.com` inherits [Trusts 👍](<👍 Domain Trust.md>) from `any-firewall.com`, 
    *  then `any-domain.com` won’t communicate with `any-threat.com` 
    *  event if there are direct or indirect [Trusts 👍](<👍 Domain Trust.md>) from `any-domain.com` to `any-threat.com`. 

    e.g., the [U.S. Department of Health & Human Services 📜](<../../../8 📜 Manifests/🌐 Vaults/📜 hhs.gov.md>) blocks whoever the [US Government 📜](<../../../8 📜 Manifests/👥 usa.gov/📜 usa.gov.md>) blocks.

    ```yaml
    # 📜 usa.gov blocks sanctioned-domain.com
    - Action: REVOKE
      Domain: sanctioned-domain.com
    ```

    ```yaml
    # 📜 hhs.gov blocks whoever the US and the Firewall block
    - Action: INHERIT
      Domains: 
        - usa.gov
        - any-firewall.com
    ```    
    
    ---
    <br/>

1. **Why not using the PKI (rfc5280) to handle domain trust?**

    The *Public Key Infrastructure (PKI)* is already used by *Certificate Authorities (CAs)* to access if domains can be trusted, both directly and indirectly. 
    
    However, its binary decision don’t allow for complex scenarios like:
    * partial [Trusts 👍](<👍 Domain Trust.md>) by subject - e.g., 
        - `A` trusts `B` for `X` but not `Y`; 
    * asymmetric [Trusts 👍](<👍 Domain Trust.md>) by subject - e.g., 
        - `A` trusts `B` for `X` but not `Y`, 
        - while `B` trusts `A` for `Y` but not `X`;
    * override modes - e.g., 
        - a direct `GRANT` prevails over an indirect `REVOKE`, 
        - while an `INHERIT` `REVOKE` prevails over any `GRANT`.

    ---
    <br/>

1. **How to calculate indirect trust paths when nodes are down?**

    Domains can rely on [Graph 🕸 domains](<../../45 🤲 Helper domains/Graphs 🕸/🕸🤲 Graph helper.md>):
    - these keep up-to-date graph representations of all possible trust-paths between two domains, allowing [Trust 👍](<👍 Domain Trust.md>) paths to be queried even when the domains comprising the nodes of those paths are unavailable 
    - e.g., `any-domain.com` can ask `any-graph.com` if `any-seller.com` can be trusted for payment requests.

    ---
    <br/>

1. **How can domains know when another domain lost trust in them?**

    [Domains 👥](<../👥 Domains/👥 Domain.md>) can rely on [Graph 🕸 domain helpers](<../../45 🤲 Helper domains/Graphs 🕸/🕸🤲 Graph helper.md>):
    - these can detect trust removals and notify affected [subscriber 🔔 domains](<../../41 🎭 Domain Roles/Subscribers 🔔/🔔🎭 Subscriber role.md>);
    - e.g., `any-graph.com` may inform `any-domain.com` whenever `any-seller.com` explicitly adds or removes a trust to `any-domain.com`.


    ---
    <br/>

1. **How can domains know when indirect trust changes affect them?**

    [Domains 👥](<../👥 Domains/👥 Domain.md>) can rely on [Graph 🕸 domains](<../../45 🤲 Helper domains/Graphs 🕸/🕸🤲 Graph helper.md>):
    - these can monitor for changes in specific [Trust 👍](<👍 Domain Trust.md>) paths that may affect an indirect [Trust 👍](<👍 Domain Trust.md>) relationship;
    - a typical scenario is an inter-governmental agreement where two entities from different countries trust each other indirectly because their government bodies trust each other.

    Consider the following manifests.

    ```yaml
    # 📜 bank-of-nation-1.com
    - Domain: nation-1.org
    ```
    ```yaml
    # 📜 bank-of-nation-2.com
    - Domain: nation-2.org
    ```
    ```yaml
    # 📜 nation-1.com 
    - Domain: nation-2.org # trusts the 2nd nation.
    ```
    ```yaml
    # 📜 nation-2.com 
    - Domain: nation-1.org # trusts the 1st nation.
    ```
    `any-graph.com` may monitor changes in the existing [Trust 👍](<👍 Domain Trust.md>) path between the two banks, checking for changes like:
    * `nation-1.org` removing a [Trust 👍](<👍 Domain Trust.md>)  to `bank-of-nation-1.com`, or
    * `nation-1.org` removing a [Trust 👍](<👍 Domain Trust.md>) to `nation-2.org`.

    ---
    <br/>