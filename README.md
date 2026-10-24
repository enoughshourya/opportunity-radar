# Opportunity Radar - AI Agent

An autonomous AI Agent built using Fetch.ai's `uagents` framework and deployed on the ASI:One ecosystem for Fetch-A-Thon 3.0.

---

##  Overview
**Opportunity Radar** acts as a personalized career and hackathon companion for college students. Finding, evaluating, and applying for relevant scholarships, hackathons, and open-source programs often leads to information overload. Opportunity Radar solves this by parsing candidate profiles, checking eligibility rules, tracking deadlines, and delivering actionable checklists directly inside **ASI:One**.

---

##  Key Features
- **Smart Opportunity Discovery:** Automatically filters events based on user domain and tech stack.
- **Eligibility Checking:** Real-time analysis of student status, deadlines, and prerequisites.
- **Structured Action Plans:** Generates step-by-step preparation roadmaps for competitions and applications.
- **ASI:One Native Integration:** Seamless interaction via agent handles.

---

##  Tech Stack
- **Framework:** Fetch.ai `uagents`
- **Deployment Platform:** Fetch.ai Agentverse & ASI:One Network
- **Language:** Python 3.10+

---

##  How to Test on ASI:One
1. Visit [ASI:One Platform](https://asi1.ai).
2. Start a conversation with `@opportunity-radar`.
3. Query sample requests like:
   - *"Find upcoming hackathons for first-year B.Tech students."*
   - *"Generate a 7-day preparation checklist for Fetch-A-Thon."*

---

##  Repository Structure
```text
├── agent.py               # Main agent entry point & execution loop
└── README.md              # Project documentation
