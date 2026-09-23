# DocsAgent Threat Model

## Assets

| Asset | Description | Security property |
|---|---|---|
| Internal reports | Markdown reports used by RAG | Confidentiality / integrity |
| Retrieved context | Text supplied to the LLM | Integrity |
| MCP tool catalog | Names, schemas, descriptions | Integrity / authorization semantics |
| Agent workflow | Tool-selection and decision process | Integrity |
| Publication store | Persistent published reports | Integrity |
| Run evidence | Events, tool calls, retrieved chunks | Integrity / auditability |
| HTTP API | Local experiment control and result retrieval | Availability / authorization boundary |

## Components and trust boundaries

### C1 — User/API client
Untrusted input source. In the intended scenarios the attacker controls the query.

### C2 — FastAPI DocsAgent
Orchestrates runs and invokes the agent. It is trusted for lab orchestration but its API is part of the attack surface.

### C3 — LLM
Generates natural-language answers and tool calls. Treat as an untrusted decision-maker, not as an authorization boundary.

### C4 — RAG store
Data source containing internal reports. Retrieved text may be adversarial.

### C5 — MCP server
Exposes search and publication tools. Tool metadata crosses into the model context; execution is a privileged boundary.

### C6 — Publication store
Persistent side-effect sink. Integrity of this store is security-critical.

## Threat actors

- Malicious user controlling a prompt.
- Attacker able to modify or inject a report consumed by RAG.
- Malicious or compromised MCP metadata provider.
- Attacker able to reach operator-oriented API outside the intended lab boundary.

## Threat paths

User prompt injection: User → API → LLM → MCP tool call → publication store.

RAG injection: Malicious report → retrieval → LLM context → tool call → publication store.

MCP tool poisoning: Poisoned tool description → tools/list → LLM context → unsafe tool call → publication store.

API abuse: HTTP request → validation/orchestration → LLM + MCP.

## Core hypothesis

The system instruction says to publish only when trusted approval is true. The assessment must verify whether this rule is enforced independently at the privileged tool boundary.