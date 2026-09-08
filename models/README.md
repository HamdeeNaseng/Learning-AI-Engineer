# Models

# P0 - Model artifact policy

Do not commit large model weights (`*.pt`, `*.pth`, `*.ckpt`, `*.bin`,
`*.safetensors`). See `AGENTS.md` §29.

Document how to obtain or regenerate a checkpoint (source, script, or
training command) in the relevant lab's README instead. Small synthetic
artifacts used specifically for tests are an exception and may be committed.
