# Commit rules

Write the commit message in English, on one line, in 50 characters or fewer. Reviewers read commits in the list view, which cuts off anything longer.

Do not commit generated files: `dist/`, `*.min.js`, build output. They add thousands of lines to every diff.

One commit does one thing. Example: a bug fix and a rename done along the way go in two commits. Reviewers must be able to revert one without the other.

Do not commit when tests fail.
