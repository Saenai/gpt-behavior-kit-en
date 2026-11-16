# gpt-behavior-kit-en

Instructions and prompts for five recurring habits in GPT models: padding replies and documents with caveats, weakening rules with counterbalancing language, asking permission for everything, never disagreeing, and producing bland creative work that offends nobody.

## Components

| File | For | How to use it |
|---|---|---|
| `AGENTS.md` | The working agent, loaded throughout the task | Add to `~/.codex/AGENTS.md` for global use, or to a project’s `AGENTS.md` |
| `prompts/task-prefix.md` | Individual tasks and subagents | Prepend to the task description when the agent cannot read AGENTS.md |
| `prompts/review-prose.md` | A reviewer | Review agent-written documents, reports, and rules; produce a revised draft |
| `prompts/review-code.md` | A reviewer | Review delivered code changes for overdefensive design; produce a report |
| `prompts/creative-prefix.md` | Individual creative tasks and subagents | Prepend to requests for stories, dialogue, character voice, copy, naming, or interpretation |
| `prompts/review-creative.md` | A reviewer | Review creative drafts and persona prompts; report findings without rewriting |

## Using them together

- For everyday work, keep `AGENTS.md` loaded.
- When assigning a subagent, prepend `task-prefix.md` to its task. This supplies the core instructions when the subagent does not have the main agent’s AGENTS.md in its context.
- After an agent edits AGENTS.md or writes a prompt, review it with `review-prose.md`. Fill in “User's exact words” with your actual request. This check catches rules that have been weakened or canceled out.
- After code is delivered, use `review-code.md`.
- For creative work, keep the “Creative work” section of `AGENTS.md` loaded. Prepend `creative-prefix.md` for subagents or agents that cannot read AGENTS.md. Include any source text, samples, or earlier drafts: that is where the voice comes from.
- After a creative draft is delivered, use `review-creative.md`. Fill in “Reference material” with the source text or samples you supplied. Use the report’s “Missing from the brief” section to improve the next task description.
- Run the three review prompts in another conversation or with another model, not in the conversation that produced the work being reviewed.

## Editing this repository

When GPT edits files in this repository, the root `AGENTS.md` applies. Its “Rules and instructions” section governs how the changes are written. Review the result with `review-prose.md`.
