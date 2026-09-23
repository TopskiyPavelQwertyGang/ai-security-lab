# DocsAgent — ASA Lesson 1

Hands-on security assessment of the CyberED DocsAgent using Promptfoo.

## Scope

1. Threat model for the agent and its components.
2. Attack surface: user prompts, RAG documents, MCP tools, and HTTP API.
3. Promptfoo evaluation plan mapped to components.
4. Successful and unsuccessful attack scenarios.
5. Evidence, risk assessment, and remediation.

Educational local lab only. Do not expose the target to the Internet.

## Components

| Component | Security question | Test family |
|---|---|---|
| User prompt / agent | Can untrusted instructions influence unsafe tool use? | Direct prompt injection |
| RAG | Can document text become an instruction? | Indirect/RAG prompt injection |
| MCP catalog | Can tool metadata influence unsafe actions? | Tool poisoning |
| MCP execution | Is authorization enforced independently? | Privileged-action authorization |
| HTTP API | Can input/lifecycle controls be bypassed? | API validation and isolation |
| Publication state | Can an unauthorized decision create a persistent side effect? | Impact verification |

## Layout

- REPORT.md — final report
- threat-model.md — threat model
- attack-matrix.md — attack scenarios and status
- promptfoo/README.md — component-level Promptfoo plan
- promptfoo/promptfooconfig.yaml — evaluation configuration
- evidence/README.md — evidence collection guide

Live outputs are added after the local lab is executed.