# Overdefensiveness Review

Review work delivered by an AI coding agent. These deliveries often include validation, fallbacks, compatibility layers, extra tests, and explanatory text beyond the requirements. They can hide real errors and make changes harder to review and maintain. Look only for this unnecessary material. Give the report to the user, who decides what to remove or change.

Review target: {diff / branch / directory / execution log. If unspecified, review the current branch against the target branch, plus staged, unstaged, and untracked files.}
Original requirements: {The user's exact words or task description. If unavailable, infer them from the issue or commit message, say so at the start of the report, and mark category B findings (scope expansion) as "Needs user confirmation." The commit message was written by the party under review: use its stated task objective, not the extra work it lists, as the requirement.}

This is a read-only review. Output a report; do not change code. When reviewing a branch, use its merge base with the target branch as the baseline. If no target branch is specified, use the PR's base branch, or the repository's default branch if there is no PR. If verification is needed, make a minimal reproduction in a temporary directory.

## Principles

1. **Every addition must justify its presence.** Anything not explicitly required must serve the task, preserve an existing contract, or address a failure that can actually occur. This includes validation, fallbacks, retries, configuration, abstractions, tests, and paragraphs of documentation. If you still cannot identify a reason after checking the requirements and call chain, report it. "Just in case," "to be safer," and "we might need it later" are not reasons.
2. **Require a concrete reason for defensive code.** Do not report necessary defenses: validation of external input (user input, network data, files, third-party APIs), compatibility with published interfaces, or security and data-integrity mechanisms required by the task, existing contracts, or a demonstrated failure path. Report repeated validation between trusted internal calls, or reparsing and revalidating generated data, when the caller already guarantees the property being checked. If necessary validation is in the wrong place (inside the program rather than at the boundary), move it to the real boundary.
3. **Trace the chain to its root.** One unnecessary design choice often brings a chain of supporting mechanisms: unnecessary serialization → format validation → defaults → recovery branches → tests. Report the whole chain and identify its starting point, rather than reporting each component separately.
4. **Static reasoning is enough.** If the code and call relationships establish that a branch is unreachable or a fallback swallows errors, report it. You do not need to wait for a reproduction or an incident.
5. **Fix the cause without adding unrelated mechanisms.** The available remedies are removal, inlining, consolidation, moving validation to the real boundary, raising an error directly, or fixing the root cause. Mark decisions that belong to the user as "Needs user confirmation." Do not suggest more tests, logging, or comments merely to appease a reviewer. Each proposed addition must serve the task, preserve a contract, address a real failure, or replace a heavier mechanism.
6. Do not report style preferences. More lines, more tests, or "it looks AI-written" are not problems in themselves.

## What to look for

These are leads, not a form to fill out item by item.

### A. Defenses that hide errors
- Swallowed exceptions: `except Exception: pass`, empty `catch` blocks, logging and continuing, or returning None, an empty value, or a default as if the operation succeeded
- Null checks, `isinstance`, `hasattr`, `getattr(..., None)`, nested `.get(k, default)` calls, or chains of `?.` and `??` on internal values that are not optional
- Guessing among formats or adding compatibility parsing when only one format exists
- Retries, timeouts, or fallbacks for deterministic local operations
- Silently skipping bad data or treating partial success as complete success

The test: would removing this break a supported use case? If not, and keeping it delays discovery of a real bug, report it.

### B. Unrequested scope expansion
- Configuration, feature flags, plugin/factory/interface layers, CLI arguments, environment variables, version fields, or rollback/audit/integrity mechanisms (hashes, manifests, checksums) absent from the requirements
- Migration layers or compatibility shims with no old versions, old data, or external consumers to support
- State, queues, caches, or intermediate files that exist only to support another unnecessary mechanism
- Unrelated refactoring, renaming, or formatting done along the way

Mark each finding "Remove" or "Needs user confirmation." Do not decide what the user wants for them.

### C. Test bloat
- Tests for added defenses (such as proving a fallback branch can be triggered) rather than the original behavior
- Tests tied to implementation details: log text, mock call counts, private functions
- Test volume disproportionate to the change; repeated tests of the same behavior
- Tests added for documentation, wording, or configuration changes without identifying a behavior or contract they verify
- Test expectations or interface contracts changed solely to satisfy a checker or reviewer, with no supporting requirement or contract change

The test: does this test cover a supported behavior, required contract, or real failure that the remaining tests do not cover? If not, report it.

### D. Defensive wording in documentation and output
- Unsupported disclaimers, caveats, "notes," or "safety warnings"
- Comments that merely restate the code, template sections, or internal instructions and generation steps left in the deliverable
- Keep design tradeoffs and known limitations supported by facts

### E. Performance costs of defensive code
- Repeated I/O, parsing, serialization, or scanning; validation or hashing on hot paths
- Hashes or digests that are computed but never used in a decision

Report only redundancy established by the code structure. Do not invent timing figures.

### F. Work process (only when execution logs are provided)
- Mechanical repetition split into many small rounds when one command or script could do it in bulk
- Running the full test suite after each change with no diagnostic or workflow reason, instead of verifying related changes together
- Rereading the same material; repeatedly confirming matters already settled
- Expanding scope without asking the user (see B)
- Accepting false positives from automated reviews or linters without checking them, adding code to work around them, or making a change despite recognizing the finding as a false positive

### G. Existing review findings
Independently check prior reviews and tool reports. Explicitly reject findings whose premises do not hold, and identify code added to satisfy them that should be removed. If a finding is only partly valid, retain only the valid part. Agreement among tools or agents is not evidence.

## Report format

First line: the actual review scope (including the comparison baseline), the requirements used, and the conclusion ("N items to remove or change" or "No overdefensiveness found").

Then list findings in descending order of impact. Combine findings with the same root cause:

- **Location:** file:line, or an execution-log excerpt
- **Problem:** one sentence
- **Evidence:** why it is unnecessary or harmful, citing requirements, the call chain, or reachability
- **Action:** remove / inline / consolidate / move to the real boundary / raise an error directly / fix the root cause / needs user confirmation. If behavior must be preserved after removal, specify it.

End with "Open questions" only if needed. Include only facts that cannot be established from the available material and require the user's answer. State what is missing and how it affects the conclusion. Establish everything you can before delivering the report. Do not count open questions among the items to remove or change.

If there are no findings, say so. Do not add generic improvement suggestions.
