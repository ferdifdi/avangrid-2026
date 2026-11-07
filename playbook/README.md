# playbook/: Reference Files (read, don't edit during the event)

These files tell humans and AI assistants **how to think, what to build, and how it should look**. The actual work happens in `../workspace/`.

| File | Purpose | When to read |
|---|---|---|
| `thinking.md` | How to reason about any Avangrid challenge: past winners, rubric, winning formula, 10-step protocol, likely 2026 topics, Q&A prep | Before anything else |
| `prompt.md` | Master fill-in-the-blank prompt. Part A = the material, Part B = how to build the website, Part C = short follow-up prompts | Fill on Nov 12 after kickoff; paste into the AI |
| `style.md` | Visual and writing style for website and slides | Before building the tool or deck |
| `deck.md` | Required PowerPoint structure, slide by slide, with speaker split | When drafting slides |
| `gameplan.md` | 32-hour timeline, roles, checkpoints, freezes | Before and during the event |

## How to start an AI session

Paste this first:

```
You are helping team D4G Cornell 1 in the Avangrid 2026 Energy Innovation Hackathon.
Read playbook/thinking.md, playbook/style.md, and playbook/prompt.md (Part A is filled).
Work only inside workspace/. Never invent numbers; read them from
workspace/03_results/key_numbers.json. Never edit files in workspace/01_data/raw/.
Task: <your task here>
```

## Source material

- Avangrid Hackathon Challenges 2022–2025 Study Guide (`../practice/Avangrid Hackathon Challenges 2022–2025 Study Guide.docx`)
- Event flyer (`../practice/avangrid_hackathon.jpeg`) and the logistics email from Avangrid Innovation
- Practice build of the 2023 V2G challenge: `../practice/` and https://bus-to-grid.vercel.app
