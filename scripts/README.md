# Repository scripts

Run commands from the repository root. The document builders resolve inputs from their own location, so moving them again requires updating their root calculation.

```powershell
python scripts/check_workspace.py
python -m pip install -r scripts/requirements-docs.txt
python scripts/docs/build_technical_spec.py
python scripts/docs/build_25_day_development_plan.py
python scripts/docs/build_project_plan.py
python scripts/docs/build_client_proposal.py
python scripts/docs/build_ai_token_payment_proposal.py
python scripts/models/calculate_economics.py
```

`check_workspace.py` uses only Python's standard library. It checks local Markdown/HTML file links, JSON parsing, Python syntax and existence of migrated project files. Add `--verify-migration` to include original local artifacts and compare binary/local artifact hashes before intentional rebuilds. It does not validate external URLs, Markdown anchors, regulatory claims or application behavior.

Document builders use Windows Segoe UI/Consolas fonts under `C:/Windows/Fonts/`. The existing scripts were verified with Python 3.14.8 and the versions in `requirements-docs.txt` on 16 November 2026. Alternate operating systems need font-path adjustments. Dependencies are for document tooling only.

The builders overwrite their corresponding PDFs, readable plans and JSON registers; the AI cost builder also renders page previews under `.local/pdfs/`. Review regenerated content and layout before distributing changed documents. The 25-day builder loads drawing helpers from the technical builder and therefore needs that builder's content/source inputs too.

`docs/prepare_technical_spec_sources.py` reconstructs the historical source register from locally recorded evidence; it does not browse or refresh the recorded check dates. Use it deliberately, rather than as a routine update step.

`archive/build_launch_brief.py` rebuilds a superseded whole-project one-sheet into `deliverables/archive/`. It also recalculates the historical budget output under `docs/models/`. Use the current project-plan builder for the launch-only roadmap.
