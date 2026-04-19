# 🛡️ Sober Agentic Infrastructure (SAI): Deterministic Gateway Demos

**The Trust Layer for Autonomous Action. Moving AI from probabilistic guessing to deterministic execution in high-stakes enterprise environments.**

---

## 🛑 The Enterprise Problem: The Liability Gap
Enterprise integration of autonomous AI agents is currently stalled. Foundational models are inherently probabilistic—they are guessing the next token. In high-stakes environments like Financial Infrastructure, Medical Logistics, and Industrial Safety, a 95% success rate equates to a 5% catastrophic failure rate. 

You cannot put a probabilistic engine in charge of enterprise workflows, financial routing, or data ingestion because eventually, it will hallucinate an action. This unpredictability creates an uninsurable "Liability Gap".

## ⚙️ The Solution: Operational Sobriety
Sober Agentic Infrastructure (SAI) provides the deterministic physics engine required to safely deploy autonomous AI. We do not "prompt-engineer" safety; we enforce it through a hard-coded logic layer that verifies system-state outcomes *before* execution. 

We mandate a strict separation of concerns: the probabilistic "Brain" (the AI Agent) is entirely severed from the deterministic "Hands" (the execution API).

## 📂 Repository Contents (Tier 1 Public Demos)
This repository contains abstracted structural demonstrations of the SAI gateway (The v1.2 Schema). It illustrates our fail-closed semantics and routing architecture.

* `📁 schemas/v1.2_schema_mock.json`: The Canonical Ingestion Envelope. The strict payload contract that mandates inclusion of target operations and governance policies.
* `📁 demos/financial_circuit_breaker.py`: A simulated demonstration of the "Fat-Finger" financial scenario, showcasing our Zero-Trust Catch-All and Pathology Report generation.

### 🚀 Running the Demo
To see the deterministic circuit breaker in action:
```bash
python demos/financial_circuit_breaker.py

---

## 📐 Architectural Mechanics: How It Works (FIG. 1)

```mermaid
graph TD
    classDef agent fill:#2d3748,stroke:#4a5568,stroke-width:2px,color:#fff;
    classDef gateway fill:#2b6cb0,stroke:#63b3ed,stroke-width:2px,color:#fff;
    classDef live fill:#2f855a,stroke:#68d391,stroke-width:2px,color:#fff;
    classDef blocked fill:#c53030,stroke:#fc8181,stroke-width:2px,color:#fff;
    classDef log fill:#4a5568,stroke:#a0aec0,stroke-width:2px,color:#fff;

    A[Probabilistic Agent 101]:::agent -->|Intended Action Captured| B[API Interceptor 102]:::gateway
    
    subgraph Deterministic Gateway boundary
        B --> C{Deterministic Circuit Breaker 103}:::gateway
        C -.-> D[Diagnostic Engine<br/>Rule Engine<br/>Immutable Guardrails]:::gateway
    end

    C -->|Authorized Action / 100% Validation| E[Live Execution Environment 104]:::live
    
    C -->|Violation / Blocked Intent| F[Immutable Audit Log 105]:::log
    
    F -->|Pathology Generated| G((Rehabilitation Loop)):::blocked
    G -.->|Forces Deterministic Prompt-Correction| A
