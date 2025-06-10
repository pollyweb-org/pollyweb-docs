👥 Domain Development FAQ
===

![](<./📎 Assets/Domain.png>)


1. **How can NLWeb be added to a domain?**

    While NLWeb is only a protocol specification that can be implemented with any web technology, the NLWeb foundation (`nlweb.org`) provides a managed service for quick deployment using any NLWeb wallet. 
    
    For an admin of an existing domain (e.g., `any-airport.com`) to implement NLWeb on their domain, they need to use their wallet to: 
    - 1/ scan the QR on `nlweb.org`; 
    - 2/ follow the deployment workflow; 
    - 3/ delegate the DNSSEC for `nlweb` on the parent domain (e.g., `nlweb.any-airport.com`); and 
    - 4/ download the admin credential signed by their nlweb subdomain. 
    
    Once deployed, admins can retrieve the access credentials to the account for further customization.

    ---

1. **How long does it take to deploy?**

    It depends on the roles deployed. Roles allow domains to limit the amount of resources deployed (e.g., if a domain `any-notepad.com` wants to allow users to store notes online with a monthly subscription, it deploys the `Host` role for chatting, the `Vault` role for storing user notes, and the `Seller` role to charge for the subscriptions).

    ---

1. **Can NLWeb be deployed into an existent cloud account?**

    Yes. The deployment workflow allows users to provide admin access to an existing account on a supported cloud provider (e.g., AWS), or it can create a new account on behalf of the user. 

    ---

1. **Does the NLWeb subdomain work before DNSSEC delegation?**

    Yes. The deployment sets up a fully functioning random domain under `dev.nlweb.org` (e.g., `12346789.dev.nlweb.org`), allowing admins to perform tests and customizations while waiting for the DNSSEC delegating on the parent domain.

    ---

1. **Is there an SDK for manual NLWeb deployment?**

    Yes. Assuming all the environment requirements are met, domain admins can download the NLWeb Python SDK and run the deployment from their laptops.

    ---

1. **How can admins publish the domain's manifest?**

    NLWeb advocates for managing the domain's manifest using a local project created with the SDK and versioned with Git.  Domain admins use the SDK to publish the manifest to the cloud provider's account. When publishing, the SDK can merge multiple partial files into a single manifest, helping to keep readability during development. 

    ---

1. **Where is the domain manifest propagated to?**

    When deployment NLWeb to a domain, the SDK sets up default domain providers for manifest propagation. Domain admins can use their wallet to change these default settings.

    ---

1. **What other domain providers are set by the SDK?**

    - **👂 Listeners**: list of domains to notify whenever the domain manifest has changed (e.g., `any-listener.nlweb.org`)
    - **🕸 Graph**: domain to query for Trusts, Schema Codes, and translations (e.g., `any-graph.org`)
    - **💳 Payer**: domain responsible for handling paying requests from other domains (e.g., `any-payer.org`)
    - **🏦 Collector**: domain responsible for collecting payments (e.g., `any-collector.org`)

    ---

1. **How do admins receive alerts from the domain?**

    Domain admins receive alerts from the domain via a chat message (e.g., new manifest version published).

    ---

1. **How can admins receive alerts from other domains?**

    Whenever another domain notifies an issue with the admin's domain (e.g., missing DKIM record), the admin receives a chat message about it.

    ---
