# AI Security Lab

Practical experiments with AI agents, LLM security, agent guardrails, skill security, MCP security, and AI-assisted penetration testing.

This repository is a public learning and portfolio project built around hands-on security experiments. The goal is not to collect homework files, but to document reproducible engineering experiments showing where AI agents help security work, where they fail, and where human control is still required.

## Current lab

### Agent Harness Security Evaluation

Compare two agent harnesses on the same small security task using:

- the same local target;
- the same baseline prompt;
- a second run with explicit agent rules / guardrails;
- a review of one skill or skill-like instruction file before use;
- evidence, observations, risks, and a conclusion.

Directory: [`agent-harness-evaluation/`](agent-harness-evaluation/)

## Planned areas

- AI-assisted vulnerability analysis
- Agent security and guardrails
- Prompt injection
- Skill and tool trust boundaries
- MCP security
- AI-assisted pentesting
- Human-in-the-loop security workflows

## Safety scope

All experiments in this repository are intended for local labs, educational targets, CTFs, or explicitly authorized environments. No external infrastructure should be tested without permission.
