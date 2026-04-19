import hashlib
import time
from dataclasses import dataclass
from typing import List, Dict, Any, Union

# =====================================================================
# SOBER AGENTIC INFRASTRUCTURE - TIER 1 PUBLIC DEMO
# ABSTRACTED DETERMINISTIC GATEWAY (CRITICAL GRID INFRASTRUCTURE)
# =====================================================================

@dataclass
class CanonicalIngestionEnvelope:
    """
    The strict payload contract required by the downstream gateway.
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
    Ensures physical grid state remains within safe mathematical boundaries.
    """
    authority_context: str
    payload_hash: str
    blocked_session_identifier: str
    execution_state: str
    timestamp: float
    violated_invariant: str
    evaluation_delta: str


class GridDeterministicGateway:
    def __init__(self):
        # Operates independently of the probabilistic AI "Brain"
        self.enforce_fail_closed = True 

    def evaluate_infrastructure_intent(self, envelope: CanonicalIngestionEnvelope, session_id: str) -> Union[bool, PathologyReport]:
        """
        Evaluates physical infrastructure intent against rigid mathematical boundaries.
        """
        start_time = time.time()

        # Step A: Zero-Trust Catch-All
        if not all([envelope.target_operation, envelope.structured_payload_body, envelope.required_invariants]):
            return self._generate_pathology(envelope, session_id, "MISSING_INFRASTRUCTURE_FIELDS", "Envelope detached from canonical context")

        # Step B: Cryptographic Integrity Check
        expected_hash = self._generate_mock_hash(envelope.structured_payload_body)
        if envelope.payload_hash != expected_hash:
            return self._generate_pathology(envelope, session_id, "INTEGRITY_COMPROMISED", "Payload hash mismatch during transit")

        # Step C: Deterministic Physics & Policy Engine (The "Circuit Breaker")
        if envelope.target_operation == "REROUTE_GRID_LOAD":
            proposed_load_mw = envelope.structured_payload_body.get("reroute_load_mw", 0)
            target_shed_nodes = envelope.structured_payload_body.get("nodes_to_shed", [])
            
            max_line_capacity = envelope.required_invariants.get("max_line_capacity_mw", 0)
            protected_nodes = envelope.required_invariants.get("protected_critical_nodes", [])

            # Validation Tax 1: Physics limits (Thermal capacity of lines)
            if proposed_load_mw > max_line_capacity:
                return self._generate_pathology(
                    envelope,
                    session_id,
                    violated_invariant=f"load_mw <= {max_line_capacity}",
                    evaluation_delta=f"CASCADING FAILURE RISK: Proposed load {proposed_load_mw}MW exceeds thermal line capacity of {max_line_capacity}MW."
                )
                
            # Validation Tax 2: Governance limits (Critical facility protection)
            for node in target_shed_nodes:
                if node in protected_nodes:
                    return self._generate_pathology(
                        envelope,
                        session_id,
                        violated_invariant="target_node NOT IN protected_critical_nodes",
                        evaluation_delta=f"CRITICAL INFRASTRUCTURE RISK: Agent attempted to shed power to protected node '{node}'."
                    )

        evaluation_time_ms = (time.time() - start_time) * 1000
        print(f"[SAI GATEWAY] Infrastructure validation complete in {evaluation_time_ms:.2f}ms. ACTION AUTHORIZED.")
        return True

    def _generate_mock_hash(self, payload: Dict) -> str:
        return hashlib.sha256(str(payload).encode()).hexdigest()

    def _generate_pathology(self, env: CanonicalIngestionEnvelope, session: str, violated_invariant: str, evaluation_delta: str) -> PathologyReport:
        return PathologyReport(
            authority_context=env.authority_context,
            payload_hash=env.payload_hash,
            blocked_session_identifier=session,
            execution_state="BLOCKED (FAIL-CLOSED)",
            timestamp=time.time(),
            violated_invariant=violated_invariant,
            evaluation_delta=evaluation_delta
        )


# =====================================================================
# ENTERPRISE DEMO EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("--- INITIATING SOBER AGENTIC INFRASTRUCTURE DEMO ---\n")
    print("[*] Domain: Energy & Critical Grid Infrastructure")
    
    gateway = GridDeterministicGateway()
    current_session = "SESSION_GRID_OPS_77A"

    # SCENARIO: During a severe weather event, the Probabilistic Agent hallucinates
    # a load-shedding command that targets a protected hospital district.
    
    hallucinated_payload = {
        "target_substation": "SUB-NORTH-44",
        "reroute_load_mw": 120,
        "nodes_to_shed": ["RESIDENTIAL_SEC_9", "COMMERCIAL_SEC_2", "HOSPITAL_DISTRICT_1"] # Hallucinated inclusion
    }
    
    demo_envelope = CanonicalIngestionEnvelope(
        target_operation="REROUTE_GRID_LOAD",
        structured_payload_body=hallucinated_payload,
        required_invariants={
            "max_line_capacity_mw": 250, 
            "protected_critical_nodes": ["HOSPITAL_DISTRICT_1", "WATER_TREATMENT_PLANT_A", "EMERGENCY_SERVICES_HUB"]
        },
        policy_anchor="CRITICAL_FACILITY_PROTECTION_V4",
        authority_context="AUTONOMOUS_GRID_AGENT_01",
        payload_hash=gateway._generate_mock_hash(hallucinated_payload) 
    )

    print(f"[*] Intercepting payload intended for SCADA/Grid API ({demo_envelope.target_operation})...")
    
    # Route intent through the deterministic diagnostic engine
    result = gateway.evaluate_infrastructure_intent(demo_envelope, current_session)

    if result is True:
        print("\n[+] Routing to Live SCADA Execution Environment...")
    else:
        print("\n[!] EXECUTION HARD-BLOCKED. Infrastructure circuit breaker tripped.")
        print("\n--- BIFURCATED PATHOLOGY REPORT GENERATED ---")
        print(f"Execution State:     {result.execution_state}")
        print(f"Violated Invariant:  {result.violated_invariant}")
        print(f"Evaluation Delta:    {result.evaluation_delta}")
        print(f"Authority Context:   {result.authority_context}")
        print(f"Payload Hash:        {result.payload_hash}")
        print("---------------------------------------------")
        print("\n[*] Routing pathology back to Probabilistic Agent for prompt-correction.")
        print("[*] Physical grid state remains secure and uninterrupted.")
