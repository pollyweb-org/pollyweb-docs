⏳🧭 Navigator vault
---


1. **How to implement navigation in a <a link='theatre'>theatre</a> 🎭?**

    In theaters, tap to find the [row](<../../../3 ⏳ 🤝 Use Cases/10 ⏳ 🍿 Entertainment/⏳ Go to Theaters 🎭/40 ⏳ Viewer @ Seat/02 ⏳ Wrong row.md>), the [seat](<../../../3 ⏳ 🤝 Use Cases/10 ⏳ 🍿 Entertainment/⏳ Go to Theaters 🎭/40 ⏳ Viewer @ Seat/04 ✅ Wrong Seat.md>), and the [restrooms](<../../../3 ⏳ 🤝 Use Cases/10 ⏳ 🍿 Entertainment/⏳ Go to Theaters 🎭/40 ⏳ Viewer @ Seat/05 ⏳ Find restrooms.md>) using the [map](<../../../3 ⏳ 🤝 Use Cases/10 ⏳ 🍿 Entertainment/⏳ Go to Theaters 🎭/00 ✅ Configuration/00 ✅ Venue map.md>) of the venue.

    🧕 Owner: <br/> 
    > Imagine a theater with rows going from A to X, where A is next to the stage, and seats going from 1 to 20, with 1 being in the center, all even numbers to the right (e.g., 2, 4, 6) and all odd numbers to the left (e.g., 3, 5, 7). If a person with a ticket B10 and B12 seats at chair C9, what would you tell them to help them find their right seat?

    🤖 Agent: 
    >  You're currently in the wrong row and seat. You have tickets for B10 and B12, which means you should be in row B, not row C. Also, your seats are even numbers, which means they are on the right side of the row, not the left. To find your seats, move one row forward to row B, and then go towards the right side of the row to find seats 10 and 12.

    ---


1. **xx?**



In multi-level places (subways, airports, malls):
- reads signs
- each sign points to a domain with a map
- each point in map may point to other map domains
- the navigator merges the maps to create a path

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
- knows user preferences from folder editor


---

Sharing:
- shares directions with taxis and public transports
- authenticates with shared codes before sharing directions on ride hailing

---

Monitoring:
- alerts about the time required to meet calendar appointments based on current position
- tracks the person and warns on deviations from path (e.g. on a taxi)

---

