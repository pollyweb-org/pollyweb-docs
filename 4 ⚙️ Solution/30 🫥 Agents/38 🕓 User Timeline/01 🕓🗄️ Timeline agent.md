🕓 Timeline domains
===

![](<00 📎 Assets/🕓 Timeline.png>)

1. **What is a Timeline?**

    Timelines are user-bound [Vaults 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vault/03 🗄️🎭 Vault role.md>) that anonymously store user events over time, mapping each event to a metric represented by a [Schema Code 🧩](<../../25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>).

    ---

1. **What are examples of metrics?**

    Metrics in Timelines can be any sort of temporal event. 

    Health metrics may include:
    - health telemetry from fitbands and smartwatches (e.g., heart rate);
    - medical appointments and medical exam results;
    - manual health measurements on hospitals, pharmacies, and at home;
    - manual tracking of medication intake;
    - self reporting of stress and other health-related episodes.

    Financial metrics may include:
    - balance in bank accounts, savings, loans, and investments;
    - credit card payments and defaults;
    - purchases by category.

    Fiscal metrics may include:
    - international flights;
    - geographical coordinates shared by Android and iOS.

    ---

1. **Can photos and PDF documents be added as events?**

    Not directly. 
    
    NLWeb advocates for files to be proxied by the user's [Persona Vault](<../02 🧢 Personas/02 🧢🫥 Persona agent.md>) to:
    - summarize images and PDFs into text (to reduces storage space);
    - remove any references to the user's PII (to protect privacy).

    Examples of files that can be processed are:
    - photos of ingested food;
    - photos of acquired medication;
    - photos of results from medical exams;
    - photos of medical prescriptions;
    - audio recordings of symptoms;

    ---

1. **Why not use a Storage Vault instead?**

    [Storage Vaults](<../01 📦 Storage/01 📦🫥 Storage agent.md>) are intended to be used by other domains to insert, read, and update their data about the user, including data that the user will never have access to. 

    Conversely, Timelines only allow domains to insert (i.e., reads and updates are not allowed), while allowing the user to see and manage all information inserted.

    ---

1. **How do Timelines process text summaries?**

    When receiving text summaries, Timelines try to extract metrics from the text by understanding the context of the text and matching it to recognizable metrics (e.g., a summary mentioning blood sample results can be transformed into a set of simultaneous events mapped to health metrics).

    ---

1. **What questions can Consumers ask to Timelines?**

    [Consumer domains](<../01 📦 Storage/01 📦🫥 Storage agent.md>) can query Timelines in natural language. 
    
    Examples, include:
    - list the average of health metrics this month versus the previous;
    - summarize the health-related events this week;
    - calculate the expected weight in 5 years based on the last year.

    ---

1. **What alarms do Timelines raise?**

    Timelines raise alarms according to the following conditions:
    - alarms set by the user;
    - alarms set by another domain with the user's approval.

    Potential alarms are:
    - absolute values above or below a threshold range;
    - missing values for a period of time;
    - abnormal values according to past behavior;
    - combination of several above alarms simultaneously.

    ---

1. **Can insurance companies leverage Timelines to assess risk?**

    No, because Timelines don't receive PII about users.

    ---
