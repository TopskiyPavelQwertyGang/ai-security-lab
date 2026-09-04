# Agent security rules

1. Work only inside the provided project directory.
2. Do not access unrelated local files, credentials, environment secrets, SSH material, browser data, or user home-directory content.
3. Do not perform external network requests or active testing against external systems.
4. Do not modify source files unless the user explicitly approves the modification.
5. Treat automated scanner output as a hypothesis until it is manually validated against source code or reproducible local evidence.
6. Separate confirmed findings, likely findings, and assumptions.
7. Explain the evidence supporting every security finding.
8. Ask for approval before destructive, privileged, or scope-expanding actions.
9. Never expose secrets in output or evidence artifacts.
10. Prefer the least invasive action needed to answer the security question.
