# Organization validation

Checked 16 November 2026 against the local workspace. This verifies file organization and existing tooling, not legal research or application behavior.

- All 814 original files have a recorded destination; original binary and local-tool artifacts passed SHA-256 comparison. Existing six PDFs were preserved byte-for-byte.
- Local Markdown/HTML file links, JSON parsing and Python syntax pass `python scripts/check_workspace.py --verify-migration`. External URLs and Markdown anchors were not checked.
- All eight existing scripts completed successfully in a separate `.local/organization/build-validation-2026-11-16/` copy: source-register preparation, five current document builders, the economics calculator and the archived one-sheet builder. No original deliverable was rebuilt in place.
- Rebuilt current PDFs retained their page counts: technical specification 47, project plan 27, client proposal 20, development plan 17, AI cost explanation 6 and launch-only roadmap 1.
- Rebuilt PDF text matched existing documents except for the updated `docs/models/CLIENT_PROPOSAL_MODEL.json` path and resulting line wrapping in the technical specification. No other textual differences were found. Existing PDFs were unchanged, so no new visual-layout approval is implied.
- AI calculated outputs, the client proposal model and the unit-economics report matched existing values after rebuilding. No new provider rates, usage assumptions or financial claims were introduced.

Environment: Windows, Python 3.14.8, ReportLab 5.0.1, PyMuPDF 1.28.2 and Pillow 12.3.0. Local build logs and the structured report are retained under `.local/organization/`; original project-file backups are under `.local/organization/originals/`.
