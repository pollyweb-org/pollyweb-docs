🔌🎭 Integrator domain role
===

1. **What is an Integrator domain role in NLWeb?**

    An Integrator is any [domain 👥](<../../40 👥 Domains/👥 Domains/👥 Domain.md>) 
    * that exposes a public API 
    * for other domains to find and use.

    ---

1. **How do Integrators work?**

    ![](<../../35 💬 Chats/💬 Chats/.📎 Assets/💬 Integrator.png>)

    ---

1. **How do Integrators publicize their API?**

    Integrators publicize their API endpoints and schemas in their [domain Manifests 📜](<../../40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>).

    ---


1. **How are integrations defined in a Manifest?**

    Integration endpoints are defined with:
    - **Type**: synchronous, asynchronous, streaming;
    - **Input**: definition or reference to the request schema;
    - **Outputs**: definitions of possible outputs.

    Endpoints are then implemented by specific roles:
    - [🪣 Dataset](<../Datasets 🪣/🪣🎭 Dataset role.md>): for dataset requests;
    - [🏭 Supplier](<../Suppliers 🏭/🏭🎭 Supplier role.md>): for asynchronous requests with status updates;
    - [🌬️ Streamer](<../Streamers 🌬️/🌬️🎭 Streamer role.md>): for event streaming.

    ---

1. **How can Integrators charge other domains?**

    Integrator domains can leverage a [Biller 🤝 helper](<../../45 🤲 Helper domains/20 🤝 Billers/🤝🤲 Biller helper.md>) for managing charges.

    ---

1. **How can domains leverage Integrators?**

    Integrators allow domains to find available services on NLWeb with a standard way to use those services across domains.

    ---