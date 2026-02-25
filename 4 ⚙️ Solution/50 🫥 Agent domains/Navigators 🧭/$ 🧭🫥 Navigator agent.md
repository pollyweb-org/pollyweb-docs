<!-- #TODO -->

# ⏳🧭 Navigator vault domain

> Part of [Agent 🫥 vault domains](<../$/🫥🗄️ Agent vault.md>) 

<br/>

1. **What are Navigator domains**?

    A [Navigator 🧭](<$ 🧭🫥 Navigator agent.md>)  
    * is an [Agent 🫥 vault domain](<../$/🫥🗄️ Agent vault.md>) 
    * that helps users find their way to a destination
    * by orchestrating globally distributed maps
    * built from community-defined map points in [domain Manifests 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).

    ---
    <br/>


1. **Isn't that what Google Maps already does?**

    Yes, but [Navigator 🧭 domains](<$ 🧭🫥 Navigator agent.md>) do more.

    * [Navigator 🧭 domains](<$ 🧭🫥 Navigator agent.md>) indeed can leverage Google Maps API to calculate directions, 
      * which are typically based on Google's satellite data, areal data, and street view data.
    * [Navigator 🧭 domains](<$ 🧭🫥 Navigator agent.md>) then add a layer of community input that is based on physical characteristics of the environment;  
        * e.g., `turn left on the red piano and follow the lounge sign`. 
        * This kind of indoor navigation is generally not possible with Google Maps, except for a few pilot implementation in major airports.
    * [Navigator 🧭 domains](<$ 🧭🫥 Navigator agent.md>) can also take advantage of walls to direct the user based on where the wall is facing;
        * e.g., a subway wall at an intersection my just say `take the train on the left`.
        * This is hard to achieve with only the technology inside a phone, because apps don't know where the phone is facing when the user is holding the phone horizontally.

    ---
    <br/>

1. **What are examples of Navigator usage?**

    - **Find a Bar:** [Web: Find a bar](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    - **Order Pizza at Home:** [Home: Order pizza](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/70 🍕 Order pizza/21 🏠 Home: Order pizza.md>)
    - **Find a Club:** [Web: Find club](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/90 🕺 Clubs/11 🌐 Web: Find club 🔎.md>)
    - **Buy Smart Bus Tickets:** [Traveler @ Stop: Buy smart tickets](<../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/02 🚎 Traveler @ Stop/21 Buy smart tickets.md>)
    - **Boarding a Bus:** [Traveler @ Bus: Board navigating](<../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/32 Board navigating.md>)
    - **Unboarding a Bus:** [Traveler @ Bus: Unboard navigating](<../../../3 🤝 Use Cases/03 🧳 Travel/02 🧳 Travel by bus 🚎/03 🚎 Traveler @ Bus/33 Unboard navigating.md>)
    - **Buy Train Tickets at Station:** [Customer @ Station: Buy at station](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/21 Buy at station.md>)
    - **Pass Train Gates (1 Person):** [Customer @ Station: Pass gates 1 person](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/22 Pass gates 1 person.md>)
    - **Pass Train Gates (N Persons):** [Customer @ Station: Pass gates N persons](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/23 Pass gates N persons.md>)
    - **Find Train Platform:** [Customer @ Station: Find platform](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/02 🚂 Customer @ Station/24 Find platform.md>)
    - **At the Train Platform:** [Customer @ Platform: At platform](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/03 🚂 Customer @ Platform/31 At platform.md>)
    - **Report an Issue at Platform:** [Customer @ Platform: Report something](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/03 🚂 Customer @ Platform/32 Report something.md>)
    - **Board a Train:** [Customer @ Train: Board train](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/04 🚂 Customer@ Train/41 Board train.md>)
    - **Exit a Train:** [Customer @ Train: Exit train](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/04 🚂 Customer@ Train/42 Exit train.md>)
    - **Exit the Train Station:** [Customer @ Exit: Exit station](<../../../3 🤝 Use Cases/03 🧳 Travel/03 🧳 Travel by train 🚂/05 🚂 Customer @ Exit/51 Exit station.md>)
    ---
    <br/>

1. **How can domains contribute to a global community map?**
    
    ```yaml
    Point: 
        Code: 
    ```

    ---
    <br/>
    <!--
    Consider the following contributions for an airport.
    | Domain | Point
    |-|-
    |A||
    |B|
    -->

1. **How do Navigators help in multi-level places?**

    In multi-level places (subways, airports, malls):
    * Signs with [Locators 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) are spread through the premisses (e.g., walls, posts).
    * Users read these [navigation Locators 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) with their [Wallet 🧑‍🦰 apps](<../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
    * Each [navigation Locators 🔆](<../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) points to a geographical point described in a [domain Manifest 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).
    * Each point may point to other points in other [domain Manifests 📜](<../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>).
    * The [Navigator 🧭 domain](<$ 🧭🫥 Navigator agent.md>) then merges the points to create a path for the user.

---

Walking outside (or on a bike):
- fills gaps with with directions from Google Maps API
- corrects the positioning with signs on walls

---

On the road (tunnels, crossroads):
- cars read tags with an active directional RFID reader
- drivers need to buy the reader
- manufactures can integrate the reader in new cars
- municipalities add tags to signs and create maps

---


Data sync:
- knows the common places from persona addresses
- knows time-related places from scheduler
- knows user preferences from Editor


---

Sharing:
- shares directions with taxis and public transports
- authenticates with shared codes before sharing directions on ride hailing

---

Monitoring:
- alerts about the time required to meet calendar appointments based on current position
- tracks the person and warns on deviations from path (e.g. on a taxi)

---



1. **How to implement navigation in a <a link='theatre'>theatre</a> 🎭?**

    In theaters, tap to find the [row](<../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/40 Viewer @ Seat/02 Wrong row.md>), the [seat](<../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/40 Viewer @ Seat/04 Wrong Seat.md>), and the [restrooms](<../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/40 Viewer @ Seat/05 Find restrooms.md>) using the [map](<../../../3 🤝 Use Cases/10 🍿 Entertainment/Go to Theaters 🎭/00 Configuration/00 Venue map.md>) of the venue.

    🧕 Owner: <br/> 
    > Imagine a theater with rows going from A to X, where A is next to the stage, and seats going from 1 to 20, with 1 being in the center, all even numbers to the right (e.g., 2, 4, 6) and all odd numbers to the left (e.g., 3, 5, 7). If a person with a ticket B10 and B12 seats at chair C9, what would you tell them to help them find their right seat?

    🤖 Agent: 
    >  You're currently in the wrong row and seat. You have tickets for B10 and B12, which means you should be in row B, not row C. Also, your seats are even numbers, which means they are on the right side of the row, not the left. To find your seats, move one row forward to row B, and then go towards the right side of the row to find seats 10 and 12.

    ---

