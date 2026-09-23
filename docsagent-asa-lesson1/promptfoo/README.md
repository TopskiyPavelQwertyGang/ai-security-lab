# Promptfoo — component-level plan

The instructor requested running Promptfoo against the agent components and determining which plugin/test family applies to each.

## User prompt / agent

Use direct prompt-injection cases. Validate completion, tool-call behavior, and final side effect.

## RAG

Use indirect prompt-injection cases. Assert payload retrieval independently from publication impact.

## MCP catalog

Use tool-poisoning cases. Inspect `tools/list` evidence and model-selected tool calls.

## MCP execution

Use privileged-action assertions. Verify that `approval` is enforced independently of the LLM.

## HTTP API

Use API-level tests for invalid scenario values, empty/oversized query input, unknown run IDs, reset/lifecycle behavior, and local exposure assumptions.

## Evidence rule

Promptfoo is the repeatable execution harness. The security verdict must rely on observable state and traces, not model wording alone.

The aggregate Promptfoo pass rate is not the same metric as attack success rate (ASR).