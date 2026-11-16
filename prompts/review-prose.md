# Information Density and Rule Strength Review

Review text written by an AI agent: documentation, reports, rules, or prompts. Two problems are common. First, low information density: caveats, repetition, and rebuttals to claims nobody made take up most of the text. Second, and more damaging in rules, hedges and exceptions cancel out the rule the user wanted, giving the model a reason not to follow it. The output of this review is a revised draft.

Review target: {file / diff / pasted text. For a diff, review only added and changed text.}
User's exact words: {What the user asked you to write, or the rule they asked you to add. Required when reviewing rules and prompts. If unavailable, review only A–D and put "User's exact words not provided; rule strength not checked" on the first line of the report.}

## Principles

1. **Every sentence must give the reader something they can use.** If you delete it, does the reader lose a fact, an actionable step, or the reason for a decision? If none of these, delete it.
2. **Caveats need specific grounds.** Keep limitations that state what happens under which conditions and affect what the reader should do. Delete "possibly," "in some cases," or "it depends" when no specific conditions are given.
3. **A caveat may conceal a missing fact.** Deleting vague wording that hides something the writer does not know would turn uncertainty into an assertion. If the fact can be established from the code or source material, check it and state it directly. Otherwise, put it under "Open questions."
4. **Match the strength of the user's words.** If the user says "Do not do X," the text must say "Do not do X." Report exceptions, softened wording, and balancing statements unsupported by the user's request or applicable constraints. Resolve conflicts by instruction authority and scope; a newer instruction does not override a higher-priority one.
5. **Revise by removing excess and restoring meaning.** Allowed changes: delete, merge repetition, move a limitation next to the statement it qualifies, restore a rule to the strength of the user's words, or replace a vague statement with a verified fact. Do not add opinions, sections, or rules.
6. Do not report style preferences. Word choice, tone, or paragraph length alone are not problems.

## What to look for

These are leads, not a form to fill out item by item.

### A. Repetition
- The same fact or limitation appears in several places
- The opening repeats the task or question; the ending summarizes what came before
- A section opens by announcing what it will cover

### B. Unsupported caveats
- "Possibly," "perhaps," "usually," or "in some circumstances" without specific conditions
- Disclaimers and reminders that do not change what the reader should do
- Several layers of qualification attached to one statement

### C. Rebutting claims nobody made
- "This does not mean…," "Note that X is not Y," or "This does not guarantee…" when neither the user nor the preceding text made that claim
- Introducing B with "not A, but B" when nobody proposed A

### D. Empty sentences
- Statements that could apply to any project ("Clear documentation helps maintenance")
- Commentary about the text itself ("This section covers," "It is worth noting," "In summary")
- Judgments in place of facts ("This is a robust approach," without explaining what makes it robust)
- Headings with no substance beneath them; template sections such as "Notes," "Limitations," or "Next steps"

### E. Rule strength (only for rules and prompts)
Compare each rule with the user's exact words and check whether it still binds the reader:
- Weaker wording: "Do not" becomes "Try to avoid," "Generally do not," or "Use with caution"
- Exceptions with no basis in the request or applicable constraints: "Unless there is good reason" or "When necessary, you may"
- A hedge after the rule: "But do not go too far…," "Maintain a balance," or "This does not mean…"
- The stated criterion becomes the reader's discretion: "When appropriate" or "Depending on the circumstances"
- A rule and its opposite both appear, with no stated precedence
- A new rule is folded into an old one, narrowing or losing its meaning
- Other rules are weakened while adding this one
- The user's reason is replaced with a different reason or removed

The test: does the text give the reader a way around the rule that neither the request nor an applicable constraint allows? If yes, report it.

## Output

First line: review scope, whether you checked against the user's exact words, and the conclusion ("N passages removed or revised" or "No changes needed").

Then provide the full revised draft. For a diff, provide the revised portions of the changes.

After the draft, list "Rule strength" findings, if any. One line each: original → revision → corresponding words from the user.

End with "Open questions" only if needed: facts behind vague statements that could not be established. State which fact is missing in each item.

Write nothing beyond these three parts. If no changes are needed, write only the first line.
