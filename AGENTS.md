# AGENTS.md — Agent Collaboration Guide

This file helps AI coding assistants (Claude, Codex, Copilot, etc.) understand this repository.

## What this repository is

A public-facing project by Longsen AI. It showcases a self-contained web tool / page.
See README.md for the full description.

## Repository layout

- `index.html` / static assets: the application (zero-dependency, open directly in browser)
- `README.md`: usage and deployment instructions
- `docs/`: extended documentation (if present)
- `.github/`: issue/PR templates and CI workflows

## Working in this repo

- **Zero-dependency philosophy**: prefer plain HTML/CSS/JS and Python standard library.
  Do not add npm/package-manager dependencies unless strictly necessary.
- **Do not modify** deployment-related files unless the change is intentional.
- Run a local HTTP server to test (e.g. `python3 -m http.server 8000`).

## Before submitting changes

- Do not include internal endpoints, ports, IP addresses, employee identifiers, or internal tool names.
- Keep external-facing copy clean and free of internal references.
- Verify the page still renders correctly.
