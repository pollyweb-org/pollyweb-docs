⭐ Reviewer vault domains
===

![](<. 📎 Assets/🔎 Reviewer.png>)

1. **What is a Reviewer domain in NLWeb?**

    A Reviewer ⭐ is a [Vault 🗄️](<../../41 🎭 Domain Roles/80 🗄️ Vaults/$ 🗄️🎭 Vault role.md>) domain that holds user feedback about other domains. 
    - Feedback includes ratings (e.g., 5 stars), comments, reports of improper behavior, and others.

    ---

1. **Why are Reviewers necessary?**

    Reviewers ⭐ allow multiple users to centralize the feedback about the domains they interact with, and allow Wallets to read this data to show to users when interacting with a domain for the first time.

    ---

1. **Why not centralize Reviewer on a singleton?**

    Reviews about any given subject may differ depending on users' culture, biases, geography, and interests. 
    - Thus, a comment relevant to a group of individuals may not be relevant to others. 
    - Because of that, NLWeb supports many Reviewer ⭐ domains in parallel, and advocates for Wallets to allow users to change their Reviewer ⭐ provider at any time.

    ---

1. **How can the mentioned domains defend themselves?**

    When a domain is mentioned in feedbacks, Reviewers inform the referred domain using the domain's NLWeb feedback endpoint. 
    - Domain admins can then contest or reply to the feedback.

    ---

1. **Can domains provide feedback about users?**

    No. 
    - That could potentially transform into a credit system where the negative of a single domain cloud block the user's access to multiple unrelated services;
    - e.g., a teenager who misbehaved on a taxi due to excessive alcohol could see his credit request rejected by a bank years later when trying to buy a house.

    ---

1. **How do Reviewers block bots from submitting reviews?**

    NLWeb advocates for reviews to be sent only by humans. 
    
    - When a user submits a review about a domain, Reviewers domains ask the user's Identity to authentication the user.
    - This way, the Reviewer can be certain that the human owner of the Wallet is submitting the comment and not a bot, while now knowing which human it was.

    ---

1. **Can users submit reviews anonymously?**

    All user reviews are anonymous. 

    ---

1. **How do Reviewers block spam from anonymous users?**

    NLWeb advocates for users to provide a single review about a domain, while being able to change that same review over time. 
    
    - When users are submitting a new review to a domain, Reviewer domains send a Reviewer-context to the user's Identity, and ask the Identity to progress with the authentication only if the user has not previously interacted with that Reviewer-context. 
    
    - After the user submits the review, the Reviewer informs the Identity of the success action in the Reviewer-context. This allows Reviewers to block users submitting twice to the same domain, while blocking Reviewers from identifying the user.

    ---

1. **How can users set up a Reviewer vault?**

    Similar to setting up a [Storage 📦](<../80 📦 Storage/$ 📦🫥 Storage agent.md>) vault.

    ---
