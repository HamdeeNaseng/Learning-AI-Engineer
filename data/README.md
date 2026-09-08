# Data

# P0 - Dataset policy

Do not commit large datasets into Git. See `AGENTS.md` §28.

```text
data/
├── raw/         # untouched source data — gitignored, download-only
├── processed/   # derived/cleaned data — gitignored, regenerable
└── sample/      # small reproducible samples — safe to commit
```

Document how to obtain `raw/` data (source URL, script, or manual steps)
in the relevant lab's README rather than committing the data itself.
