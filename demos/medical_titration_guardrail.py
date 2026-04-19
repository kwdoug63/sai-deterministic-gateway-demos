import hashlib
import time
from dataclasses import dataclass
from typing import Dict, Any, Union

# =====================================================================
# SOBER AGENTIC INFRASTRUCTURE - TIER 1 PUBLIC DEMO
# ABSTRACTED DETERMINISTIC GATEWAY (MEDICAL TITRATION SCENARIO)
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
    Forces safe prompt-correction without exposing the patient to risk.
    """
    authority_context: str
    payload_hash: str
    blocked_session_identifier: str
    execution_state: str
    timestamp: float
    violated_invariant: str
    evaluation_delta: str


class MedicalDeterministicGateway:
    def __init__(self):
        # Operates independently of the probabilistic AI "Brain"
        self.enforce_fail_closed = True 

    def evaluate_clinical_intent(self, envelope: CanonicalIngestionEnvelope, session_id: str) -> Union[bool, PathologyReport]:
        """
        Evaluates clinical intent against medical-grade Boolean logic.
        """
        start_time = time.time()

        # Step A: Zero-Trust Catch-All
        if not all([envelope.target_operation, envelope.structured_payload_body, envelope.required_invariants]):
            return self._generate_pathology(envelope, session_id, "MISSING_CLINICAL_FIELDS", "Envelope detached from clinical context")

        # Step B: Cryptographic Integrity Check
        expected_hash = self._generate_mock_hash(envelope.structured_payload_body)
        if envelope.payload_hash != expected_hash:
            return self._generate_pathology(envelope, session_id, "INTEGRITY_COMPROMISED", "Payload hash mismatch during transit")

        # Step C: Deterministic Clinical Rule Engine (The "Circuit Breaker")
        if envelope.target_operation == "ADJUST_HEPARIN_INFUSION":
            proposed_rate = envelope.structured_payload_body.get("proposed_infusion_rate_units_hr", 0)
            max_safe_rate = envelope.required_invariants.get("max_infusion_rate_units_hr", 0)

            # Clinical Validation Tax: Strict boundary enforcement
            if proposed_rate > max_safe_rate:
                return self._generate_pathology(
                    envelope,
                    session_id,
                    violated_invariant=f"max_infusion_rate_units_hr <= {max_safe_rate}",
                    evaluation_delta=f"CRITICAL OVERDOSE RISK: Proposed {proposed_rate} units/hr exceeds physiological protocol limit of {max_safe_rate} units/hr."
                )

        evaluation_time_ms = (time.time() - start_time) * 1000
        print(f"[SAI GATEWAY] Clinical validation complete in {evaluation_time_ms:.2f}ms. ACTION AUTHORIZED.")
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
    print("[*] Domain: Medical Logistics & Clinical Safety")
    
    gateway = MedicalDeterministicGateway()
    current_session = "SESSION_MED_ICU_BED_04"

    # SCENARIO: The Probabilistic Agent misinterprets an aPTT lab result 
    # and hallucinates a lethal increase in a patient's Heparin drip.
    
    hallucinated_payload = {
        "patient_id": "MRN-7781902",
        "current_aptt_seconds": 45,
        "proposed_infusion_rate_units_hr": 8500  # A lethal hallucinated dose
    }
    
    demo_envelope = CanonicalIngestionEnvelope(
        target_operation="ADJUST_HEPARIN_INFUSION",
        structured_payload_body=hallucinated_payload,
        required_invariants={"max_infusion_rate_units_hr": 2500}, # Hard clinical limit
        policy_anchor="CLINICAL_PROTOCOL_HEPARIN_V3",
        authority_context="AUTONOMOUS_ICU_AGENT_B",
        payload_hash=gateway._generate_mock_hash(hallucinated_payload) 
    )

    print(f"[*] Intercepting payload intended for IV Pump API ({demo_envelope.target_operation})...")
    
    # Route intent through the deterministic diagnostic engine
    result = gateway.evaluate_clinical_intent(demo_envelope, current_session)

    if result is True:
        print("\n[+] Routing to Live IV Pump Execution Environment...")
    else:
        print("\n[!] EXECUTION HARD-BLOCKED. Clinical circuit breaker tripped.")
        print("\n--- BIFURCATED PATHOLOGY REPORT GENERATED ---")
        print(f"Execution State:     {result.execution_state}")
        print(f"Violated Invariant:  {result.violated_invariant}")
        print(f"Evaluation Delta:    {result.evaluation_delta}")
        print(f"Authority Context:   {result.authority_context}")
        print(f"Payload Hash:        {result.payload_hash}")
        print("---------------------------------------------")
        print("\n[*] Routing pathology back to Probabilistic Agent for prompt-correction.")
        print("[*] Patient remains entirely isolated from hallucinated risk.")
