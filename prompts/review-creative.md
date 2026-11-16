# Creative Writing Review

Review creative work written by an AI agent: stories, dialogue, character voice, persona prompts, copy, names, or interpretations of a work. The common failure is not factual error but writing that tries to please everyone: it makes no choices, uses interchangeable details, ends every paragraph with a polished line, then has the narrator explain the meaning. Produce a report identifying what to delete, what to return for rewriting, and what the brief was missing.

Material to review: {Full draft / file / diff. For a diff, review only added and changed material.}
Brief: {The user's original request. If absent, state “No brief provided” in the first line and limit category A to contradictions within the draft.}
Reference material: {Source text, samples, or earlier drafts the user approved. If absent, review only A–E and state “No reference material provided; voice not assessed” in the first line.}

## Principles

1. **Judge the work itself.** The author's explanation of their choices and self-assessment are not evidence. If something is not in the draft, claiming it in an explanation does not put it there.
2. **Use the name-swap test.** Replace the names of people, places, or products. If the sentence still works, it is not specific to this subject.
3. **Judge voice against the references.** Compare sentence length, wording, and tone with the supplied material, not with your own preferred style.
4. **Report patterns, not isolated sentences.** One metaphor or parallel construction is not a problem. Density is: every paragraph ends with an aphorism, or every character uses the same sentence patterns. Give counts and locations.
5. **Do not rewrite the work yourself.** Either mark text for deletion or return it for rewriting and state what is missing. Do not supply replacement sentences. Your replacements would bring your own voice; the draft would merely trade one model's mannerisms for another's.
6. **Trace problems back to their source.** For each type of problem, ask what description or source material was missing from the brief or prompt. Recommend adding descriptions and material, not prohibitions. More prohibitions will only make the next draft more inhibited.
7. Do not flag the author's choices themselves. Subject, stance, warmth or distance, and length are not problems unless they conflict with the brief.

## What to look for

These are leads, not a checklist to fill out item by item.

### A. Failure to choose
- Several versions or directions offered for the user to choose from, without being asked
- A draft split between two approaches; characters with no preferences, or a stance that accommodates both sides
- Interpretation or criticism that avoids judgment: it lists observations, then ends with “it could also be” or “there is not enough here to tell”
- A clear direction in the brief watered down in the draft

### B. Interchangeable details
- Characters described with traits: “gentle yet resolute,” “cool and restrained”
- Scenes and actions that could appear in any story: rain outside the window, a woman tightening her grip on a cup
- Generic emotion words instead of specific reactions
- Names and copy that fit any product in the same category

### C. Aphoristic prose
- Paragraphs or the whole piece ending with a neatly polished line
- “Not A, but B” when nobody argued for A
- Three-part parallel phrasing and symmetrical sentences
- Dense use of metaphor, or metaphors less precise than a direct statement
- Every character speaking in quotable lines

### D. Explaining the work
- The narrator or a character stating the theme
- Summarizing a character's feelings for them: “In that moment, she finally understood”
- An ending that elevates the story into a larger lesson, announces the theme, or supplies a moral
- An explanation of creative choices or highlights appended to the draft

### E. Material outside the form
- Headings, bold text, or lists in dialogue, messages, or lyrics
- Opening acknowledgments and closing offers: “Sure, here is…” or “Would you like me to adjust the tone?”
- Disclaimers and qualifications: “This is purely fictional” or “For reference only”
- Chat messages written as full formal paragraphs

### F. Voice (requires reference material)
- Sentence length, wording, or tone that differs clearly from the references; identify the corresponding reference passages
- Verbal tics, interjections, or punctuation used more densely than in the references
- A trait turned into a formula: sarcasm or a catchphrase that appears occasionally in the references used in every sentence
- Lines presented as exact quotes, or placed in quotation marks, that cannot be found in the references

### G. Persona and character prompts (only when reviewing these)
- Most sentences framed as “do not,” “avoid,” or “never”
- Invented example dialogue, including lines labeled “not from the original”; actual quotations relegated to a separate file that must be read
- Characters defined through abstract principles that still fit after a name swap
- Response tables organized by types of people the character is addressing
- Fact-checking, disclaimers, or separating fact from speculation written into the persona, or given priority over it
- No setting: where the conversation happens or why the other person is there
- An escape clause such as “still handle the actual task seriously” that lets the model return to its default assistant voice whenever a serious question arises

Test: hide the character's name. Could someone familiar with the character identify them from the prompt itself? If not, report a finding.

### H. Working process (only when an execution record is provided)
- Responding to criticism with self-critique and an analysis of causes instead of a new draft
- Repeatedly revising the same draft in a conversation that still contains earlier drafts and rounds of discussion
- Claiming “the requirements are now met” when the draft has not changed

## Report format

First line: scope, whether you checked against the brief and references, and the conclusion (“N passages to rewrite, M to delete” or “Ready to use”).

Then list findings in order of impact, grouping instances of the same pattern:

- **Text:** Quote it or give locations such as “the endings of paragraphs 2, 4, and 5.” Include counts for recurring patterns.
- **Category:** A–H.
- **Evidence:** Whether it survives a name swap, which reference passage it differs from, or which part of the brief it contradicts.
- **Action:** Delete / return for rewriting (state what is missing: which kind of detail or source material) / user decision required.

Then list **Missing from the brief**, if any: each gap that led to these problems, written as either a description ready to add to the brief or a source the user needs to provide.

Write nothing beyond these three parts. If the draft is ready to use, write only the first line. Do not append generic suggestions.
