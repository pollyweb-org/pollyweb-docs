🪣🎭 Dataset domain role
===

![](<../../35 💬 Chats/💬 Chats/.📎 Assets/💬 Dataset.png>)

1. **What is a Dataset domain role in NLWeb?**

    A Dataset is an [🪢 Integrator](<../Integrators 🪢/🪢🎭 Integrator role.md>) domain that exposes a synchronous data API. 

    ---

1. **What are examples of possible data APIs?**

    Data APIs can be 
    * reference data (e.g., countries, flags, country calling codes), 
    * dynamic datasets (e.g., weather forecasts), 
    * or any type of data capable of being downloaded from an HTTPS endpoint.

    ---

1. **How do Datasets handle data API requests?**

    When using the NLWeb SDK, Datasets can point the data APIs 
    * to static datasets (e.g., CSV files), 
    * to databases (e.g., PostgreSQL), 
    * or to custom-built handlers (e.g., Python).

    ---

1. **How can Hosts leverage Datasets on chats?**

    When using the NLWeb SDK, Hosts can reference these APIs in workflow and schema-based CRUD dialogs by using NLWeb locators. 
    
    * The NLWeb SDK will pull the data schema from the Dataset's Manifest, and map it to the CRUD schema of the Host. 
    * When chatting with users, the NLWeb SDK invokes the Dataset's end-point.

    ---

1. **How do Hosts reference a Datasets API?**

    Data APIs are referenced by `{column}@{domain}/{offer}` - e.g.:
    * `Code@standards.any-igo.org/639-1` 
    * references the `Code` column 
    * in the `639-1` data API 
    * offered by the domain [`standards.any-igo.org` 📜](<../../../8 📜 Manifests/👥 any-igo.org/📜 standards.any-igo.org.md>) .

    ---