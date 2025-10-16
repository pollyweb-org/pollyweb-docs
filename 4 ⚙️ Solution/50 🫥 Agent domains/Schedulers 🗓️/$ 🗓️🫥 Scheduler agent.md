<!-- #TODO -->

⏳🗓️ Scheduler vault domains
===

1. **What is a Scheduler?**

    Schedulers are user-bound vaults responsible for representing a user's schedule, namely:    
    - knows the people on the invites
    - knows the user preferences from Editor
    
    ---

1. **Are schedulers the same as calendars?**

    Not necessarily. 
    - Schedulers are API definition, regardless of internals; this means that a scheduler domain might decide to parse user calendars (e.g., Google calendar) or it might decide to hold its own internal calendar.

    ---


1. **What's the role of schedulers in new bookings?**

    Services leverage schedulers to ask users for a specific date, date/time, or period between dates.
    - Before sending the date inputs to the requesting service, schedulers identify potential clashes (e.g., "it will take you 30 minutes to get there").
    - It also takes into account user preferences ("You'll arrive 5 minutes before the show, and I told you like to arrive 30 minutes in advance").

    ---

1. **Do schedulers create new events?**

    Yes. Schedulers parse saved booking tokens and registers the booking in the underlying calendar.

    ---