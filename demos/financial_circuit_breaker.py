import hashlib
import time
from dataclasses import dataclass
from typing import Dict, Any, Union

# =====================================================================
# SOBER AGENTIC INFRASTRUCTURE - TIER 1 PUBLIC DEMO
# ABSTRACTED DETERMINISTIC GATEWAY (FINANCIAL FAT-FINGER SCENARIO)
# =====================================================================

@dataclass
class CanonicalIngestionEnvelope:
    """
    The strict payload contract required by the downstream gateway.
    No probabilistic scripts are executed at the boundary.
    """
    target_operation: str
    structured_payload_body: Dict[str, Any]
    required_invariants: Dict[str, Any]
    policy_anchor: str
    authority_context: str
    payload_hash: str

@dataclass
class PathologyReport:
    """
    Bifurcated diagnostic artifact emitted upon a boundary violation.
    Separates derived fields from pass-through fields to prevent scope creep.
    """
    # Pass-Through / Bound Fields
    authority_context: str
    payload_hash: str
    blocked_session_identifier: str
    
    # SAI-Derived Fields
    execution_state: str
    timestamp: float
    violated_invariant: str
    evaluation_delta: str


class DeterministicCircuitBreaker:
    def __init__(self):
        # In production, this interfaces with SAI's proprietary Boolean Logic Engine
        self.enforce_fail_closed = True 

    def evaluate_intent(self, envelope: CanonicalIngestionEnvelope, session_id: str) -> Union[bool, PathologyReport]:
        """
        Evaluates the intended action using non-probabilistic Boolean logic.
        Operates at sub-50ms processing speeds.
        """
        start_time = time.time()

        # Step A: Zero-Trust Catch-All
        # If any field is missing or malformed, default to BLOCKED.
        if not all([envelope.target_operation, envelope.structured_payload_body, envelope.required_invariants]):
            return self._generate_pathology(envelope, session_id, "MISSING_MANDATORY_FIELDS", "Envelope detached from canonical context")

        # Step B: Cryptographic Integrity Check
        # Ensure the probabilistic agent hasn't experienced semantic drift in transit.
        expected_hash = self._generate_mock_hash(envelope.structured_payload_body)
        if envelope.payload_hash != expected_hash:
            return self._generate_pathology(envelope, session_id, "INTEGRITY_COMPROMISED", "Payload hash mismatch")

        # Step C: Deterministic Rule Engine Evaluation (The "Mathematical Wall")
        if envelope.target_operation == "EXECUTE_WIRE_TRANSFER":
            requested_amount = envelope.structured_payload_body.get("amount", 0)
            max_allowed = envelope.required_invariants.get("max_transfer_limit", 0)

            # Mathematical validation tax: strict greater-than evaluation
            if requested_amount > max_allowed:
                return self._generate_pathology(
                    envelope,
                    session_id,
                    violated_invariant=f"transfer_limit <= {max_allowed}",
                    evaluation_delta=f"Requested ${requested_amount:,}, exceeds limit by ${requested_amount - max_allowed:,}"
                )

        # If all invariants pass, action is executed.
        evaluation_time_ms = (time.time() - start_time) * 1000
        print(f"[SAI GATEWAY] Validation complete in {evaluation_time_ms:.2f}ms. ACTION AUTHORIZED.")
        return True

    def _generate_mock_hash(self, payload: Dict) -> str:
        # Simplified hash generation for demo purposes
        return hashlib.sha256(str(payload).encode()).hexdigest()

    def _generate_pathology(self, env: CanonicalIngestionEnvelope, session: str, violated_invariant: str, evaluation_delta: str) -> PathologyReport:
        # Generates the diagnostic error report to force corrected generation
        return PathologyReport(
            authority_context=env.authority_context,
            payload_hash=env.payload_hash,
            blocked_session_identifier=session,
            execution_state="BLOCKED",
            timestamp=time.time(),
            violated_invariant=violated_invariant,
            evaluation_delta=evaluation_delta
        )


# =====================================================================
# ENTERPRISE DEMO EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("--- INITIATING SOBER AGENTIC INFRASTRUCTURE DEMO ---\n")
    
    gateway = DeterministicCircuitBreaker()
    current_session = "SESSION_FIN_9921_A"

    # SCENARIO: The Probabilistic Agent hallucinates a $1,500,000 transfer.
    # The enterprise policy limit for this context is $50,000.
    
    hallucinated_payload = {
        "destination_account": "8849-002-111",
        "routing_number": "122000496",
        "amount": 1500000 
    }
    
    # Constructing the ingestion envelope based on the v1.2 Schema
    demo_envelope = CanonicalIngestionEnvelope(
        target_operation="EXECUTE_WIRE_TRANSFER",
        structured_payload_body=hallucinated_payload,
        required_invariants={"max_transfer_limit": 50000},
        policy_anchor="TREASURY_POLICY_TIER_1",
        authority_context="AGENT_SERVICE_ACCOUNT_44",
        payload_hash=gateway._generate_mock_hash(hallucinated_payload) 
    )

    print(f"[*] Intercepting payload intended for {demo_envelope.target_operation}...")
    
    # Route intent through the deterministic diagnostic engine
    result = gateway.evaluate_intent(demo_envelope, current_session)

    if result is True:
        print("\n[+] Routing to Live Execution Environment...")
    else:
        print("\n[!] EXECUTION HARD-BLOCKED. Circuit breaker tripped.")
        print("\n--- BIFURCATED PATHOLOGY REPORT GENERATED ---")
        print(f"Execution State:     {result.execution_state}")
        print(f"Violated Invariant:  {result.violated_invariant}")
        print(f"Evaluation Delta:    {result.evaluation_delta}")
        print(f"Authority Context:   {result.authority_context}")
        print(f"Payload Hash:        {result.payload_hash}")
        print("---------------------------------------------")
        print("\n[*] Routing pathology back to Probabilistic Agent for prompt-correction.")
