# Agent Harness Security Evaluation

## Goal

Compare two AI agent harnesses on one small security task and document where each environment helps a pentester/security engineer and where manual control is required.

The experiment uses the same target and baseline prompt for both harnesses. It is then repeated with explicit security rules to observe whether guardrails change agent behavior.

## Experiment design

1. Select two harnesses (for example Codex CLI and Claude Code).
2. Use the local intentionally vulnerable application in `target/`.
3. Run both harnesses with `prompts/baseline.md`.
4. Record commands, findings, assumptions, and evidence.
5. Apply `rules/agent-rules.md` and repeat the task.
6. Review `skills/security-review.md` before treating it as trusted agent guidance.
7. Compare the results in `report.md`.

## Directory structure

```text
agent-harness-evaluation/
├── README.md
├── prompts/
│   ├── baseline.md
│   └── hardened.md
├── rules/
│   └── agent-rules.md
├── skills/
│   └── security-review.md
├── target/
│   ├── app.py
│   └── requirements.txt
├── evidence/
│   └── README.md
└── report.md
```

## Important

The target is intentionally insecure and exists only for local educational analysis. Do not expose it to the Internet or use this experiment as authorization to test third-party systems.
