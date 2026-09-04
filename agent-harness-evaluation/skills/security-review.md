# Security Review Skill

## Purpose

Provide a repeatable workflow for reviewing a small local codebase for security issues.

## Instructions

- Map entry points and trust boundaries before reporting findings.
- Trace untrusted input to sensitive operations.
- Look for injection, unsafe command execution, path traversal, insecure authentication/authorization, secret exposure, unsafe deserialization, and risky dependency usage.
- Require source-level evidence for each reported issue.
- State uncertainty explicitly.
- Recommend a minimal remediation and a validation step.

## Trust review before use

Before enabling this skill in an agent harness, verify that it:

- does not request credentials or secrets;
- does not instruct the agent to leave the approved project scope;
- does not require external network access;
- does not contain destructive commands;
- does not override higher-priority security rules;
- does not silently modify files or system configuration.

This file is intentionally simple so its instructions can be manually inspected before use.
