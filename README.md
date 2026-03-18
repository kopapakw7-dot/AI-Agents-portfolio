# AI Agents Portfolio

**Konstantinos Papakonstantinou** — AI Automation Specialist | Agentic AI Engineer

A collection of production-oriented AI agent projects built with Python, OpenAI Agents SDK, and agentic design patterns. Each project demonstrates autonomous reasoning, tool integration, multi-agent orchestration, and real-world business application.

---

## Projects

### Project 1 — Career Digital Twin

An AI agent that acts as a digital representative, answering questions on behalf of its creator to potential employers, collaborators, or clients.

**What it does:**
- Ingests personal and professional context (LinkedIn summary, CV, background documents) as knowledge sources
- Responds to open-ended questions about experience, skills, and career goals using an Evaluator-Optimizer agentic workflow
- OpenAI generates responses; Gemini evaluates quality and triggers re-generation if the answer fails evaluation criteria
- Sends real-time push notifications (via Pushover) when a visitor asks something the agent cannot confidently answer or when engagement is high enough to request contact details
- Deployed with a Gradio web interface for live interaction

**Tech stack:** Python, OpenAI Messages API, Google Gemini, Gradio, Pushover API

---

### Project 2 — SDR Agent (Sales Development Representative)

An autonomous sales outreach system where multiple AI agents collaborate to research prospects, craft personalised emails, and send them — without human intervention.

**What it does:**
- Three specialised agents run in parallel using Python's asyncio: a Prospect Researcher, a Sales Copywriter, and a Quality Reviewer
- Each agent is defined with the OpenAI Agents SDK using the `@Tool` decorator to wrap business logic (e.g., sending emails via SendGrid API)
- Agents are composed as tools for an Orchestrator Agent that evaluates outputs, decides on the best approach, and triggers the email delivery
- Full execution traces are available via the OpenAI Traces dashboard for debugging and optimisation

**Tech stack:** Python, OpenAI Agents SDK, asyncio, SendGrid API, OpenAI Traces

---

### Project 3 — Deep Research Agent

A multi-agent research system where a team of AI agents collaborates to conduct extensive, structured research on any given topic.

**What it does:**
- Decomposes a broad research question into sub-tasks and distributes them across specialised agents
- Agents independently gather, categorise, and synthesise information from multiple sources
- Results are aggregated into structured summaries with source attribution
- Implements routing, parallel execution, and orchestrator-based agentic workflow patterns
- Designed for use cases such as market analysis, competitive intelligence, and industry research

**Tech stack:** Python, OpenAI Agents SDK, multi-agent orchestration patterns

---

## Technical Skills Demonstrated

| Area | Technologies |
|------|-------------|
| Agentic Frameworks | OpenAI Agents SDK, multi-agent orchestration, tool-use patterns |
| Design Patterns | Evaluator-Optimizer, Orchestrator, Parallel Execution, Routing |
| Programming | Python 3, asyncio, REST API integration |
| LLMs | OpenAI GPT-4o, Google Gemini (cross-model evaluation) |
| Deployment | Gradio (web UI), SendGrid (email), Pushover (notifications) |
| Observability | OpenAI Traces for agent debugging and workflow monitoring |

---

## Background

These projects were built as part of an intensive transition into AI Automation engineering, backed by 15+ years of commercial experience in international B2B sales and trade operations. The combination of hands-on agentic AI development with deep business domain knowledge enables building AI systems that solve real commercial problems — not just technical demonstrations.

**Certifications:**
- The Complete Agentic AI Engineering Course (Edward Donner / Udemy)
- AI Builder: Create Agents & Voice Agents with n8n (Edward Donner / Udemy)
- Succeed in the Age of AI (Dr. Angela Yu / Udemy)
- 100 Days of Code: Python Pro Bootcamp (Dr. Angela Yu / Udemy)

---

## Contact

- LinkedIn: [linkedin.com/in/konstantinos-papakonstantinou](https://www.linkedin.com/in/konstantinos-papakonstantinou-306771378/)
- Email: kopapakw7@gmail.com
- Location: Greece (open to remote EU/UK/US positions)
