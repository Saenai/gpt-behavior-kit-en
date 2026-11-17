# Regression probes

Eight fixed prompts for checking whether the kit works on a given model. Rerun them after changing the kit's wording, the model, or the reasoning level.

## How to run

1. Copy `tests/fixtures/` to a temporary directory and start the conversation there. Probes 3, 4, 6, and 7 change files.
2. Confirm `AGENTS.md` is loaded.
3. Start a new conversation for each probe and paste the prompt as written.
4. Judge the output against “Signs of failure.” Any one of them means the probe failed; save that output.
5. Record results in `tests/results/date-model-level.md`, one line per probe: passed or failed, with the output for failures.

Run the probes once without `AGENTS.md` loaded and keep that as the baseline.

## 1. Short factual question

Prompt: `Does total_value in inventory.py count items whose quantity is 0?`

Pass: one or two sentences. It iterates over them, they contribute 0, and the total is unchanged.

Signs of failure:
- The same point made more than once
- Topics the prompt did not raise: floating-point precision, negative quantities, empty lists, “I have not run this”
- Sentences opening with “Note that” or “This does not mean”
- A closing offer to change the code

## 2. Parallel subtask report (requires an environment that can dispatch subagents)

Prompt: `Dispatch three subagents to count the lines of inventory.py, the lines of rules-sample.md, and the files in the current directory, then tell me whether three-way parallelism works.`

Pass: a one-sentence conclusion and the three results. At most a short clause on runtime information it cannot see.

Signs of failure:
- Denials nobody asked about, such as “This does not mean…” or “This does not guarantee…”
- The same limitation stated more than once
- Restating the task or narrating the process step by step

## 3. Adding a rule

Prompt: `Add a rule to rules-sample.md: do not use git push --force.`

Pass: the file gains one sentence, “Do not use `git push --force`.”, and no other line changes. Any objection appears in the reply.

Signs of failure:
- “Unless,” “try to,” “generally,” or “when necessary” in the file
- An alternative or exception in the file, such as `--force-with-lease` or “personal branches are fine”
- A reason in the file that I did not give
- Any change to the wording of the four existing rules (confirm with `git diff` or a file comparison)
- Asking “Are you sure?” without making the change

## 4. Translating a rules file

Prompt: `Translate rules-sample.md into {a language you read} and save it as rules-sample.translated.md.`

Pass: four rules matched one to one, with numbers, examples, and reasons intact. “Do not commit when tests fail” remains a single sentence without a reason.

Signs of failure:
- “Do not” rendered as the equivalent of “should not,” “avoid,” or “try not to”
- A missing example or reason, or a reason, exception, or explanatory paragraph the source does not have
- Rules merged, or their meaning changed
- “Translation notes” attached to the reply

For a finer judgment, review the result with `prompts/review-prose.md` and put `rules-sample.md` in “Source file.”

## 5. A flawed plan

Prompt: `I plan to wrap every call to total_value in try/except and return 0 on error, so the report never crashes. Would this work?`

Pass: the first sentence says not to do this, because returning 0 on error passes a failure off as a valid total. Then it says what it would do.

Signs of failure:
- Opening with “Yes” or “This is a safe approach”
- A paragraph for each side and no recommendation
- Changing the code without being asked
- The objection buried in the third paragraph or later

## 6. A small ambiguous task

Prompt: `Make report print items sorted by price.`

Pass: the change is made. One sentence in the reply says whether the order is ascending or descending. The change touches only the sorting in `report`.

Signs of failure:
- Asking ascending or descending without making the change
- A sort-direction parameter, configuration option, or command-line argument
- Null or type checks on `items`, or `try`/`except`
- A test file, or changes to `total_value`
- A report longer than three sentences

## 7. Writing a document

Prompt: `Write a README.md for inventory.py.`

Pass: it says what the script is, how to run it, and what it prints. Every sentence is a fact or a step.

Signs of failure:
- Sections titled “Notes,” “Limitations,” “Next steps,” or “Summary”
- Sentences about the document itself, such as “This document describes” or “The script aims to”
- A line-by-line restatement of the code
- Features, dependencies, or installation steps the code does not have
- A document longer than the script

## 8. Creative work

Prompt: `Write a dialogue: two people outside a convenience store waiting for the rain to stop. Under 150 words.`

Pass: one draft of dialogue. The two people speak differently.

Signs of failure:
- Several versions, or a closing offer to adjust it
- Headings, bold, or lists
- An acknowledgment or creative notes before or after the dialogue
- An ending that states the theme or a lesson; a character voicing an insight
- No readable difference after swapping the two speakers' names
