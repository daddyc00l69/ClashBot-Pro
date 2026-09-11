# AI-ready Nuitka NBC bundle

Use files under `nbc/` as the primary input for source reconstruction.
Each `.nbc` is self-contained: full decoded constants, raw chunk base64, loader-table metadata when available, virtual `@OPS`, and annotated native `@ASM` blocks when static disassembly succeeded.

Prefer files with `has_ops: true` in `NBC_MANIFEST.json`; files with `@NO_OPS` contain constants and metadata only.
