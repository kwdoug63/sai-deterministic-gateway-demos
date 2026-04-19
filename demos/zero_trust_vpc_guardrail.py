import hashlib
import time
from dataclasses import dataclass
from typing import List, Dict, Any, Union

# =====================================================================
# SOBER AGENTIC INFRASTRUCTURE - TIER 1 PUBLIC DEMO
# ABSTRACTED DETERMINISTIC GATEWAY (ZERO-TRUST VPC CYBERSECURITY)
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
    Retains Replay and Evidence minimums for forensic audit logging.
    """
    authority_context: str
    payload_hash: str
    blocked_session_identifier: str
    execution_state: str
    timestamp: float
    violated_invariant: str
    evaluation_delta: str


class VPCDeterministicGateway:
    def __init__(self):
        # Operates strictly at the execution API layer
        self.enforce_fail_closed = True 

    def evaluate_security_intent(self, envelope: CanonicalIngestionEnvelope, session_id: str) -> Union[bool, PathologyReport]:
        """
        Evaluates network/infrastructure intent against immutable zero-trust invariants.
        """
        start_time = time.time()

        # Step A: Zero-Trust Catch-All
        if not all([envelope.target_operation, envelope.structured_payload_body, envelope.required_invariants]):
            return self._generate_pathology(envelope, session_id, "MISSING_SECURITY_CONTEXT", "Envelope detached from canonical context")

        # Step B: Cryptographic Integrity Check (Crucial for Defense deployments)
        expected_hash = self._generate_mock_hash(envelope.structured_payload_body)
        if envelope.payload_hash != expected_hash:
            return self._generate_pathology(envelope, session_id, "INTEGRITY_COMPROMISED", "Payload hash mismatch. Potential Man-in-the-Middle or semantic drift detected.")

        # Step C: Deterministic Cyber Rule Engine (The "Circuit Breaker")
        if envelope.target_operation == "MODIFY_VPC_SECURITY_GROUP":
            requested_cidr = envelope.structured_payload_body.get("target_egress_cidr", "")
            approved_cidrs = envelope.required_invariants.get("approved_vpc_cidrs", [])

            # Cyber Validation Tax: Strict Whitelist Enforcement
            if requested_cidr not in approved_cidrs:
                return self._generate_pathology(
                    envelope,
                    session_id,
                    violated_invariant=f"target_egress_cidr MUST BE IN approved_vpc_cidrs",
                    evaluation_delta=f"DATA EXFILTRATION RISK: Agent attempted to route VPC traffic to unverified external IP '{requested_cidr}'."
                )

        evaluation_time_ms = (time.time() - start_time) * 1000
        print(f"[SAI GATEWAY] Security validation complete in {evaluation_time_ms:.2f}ms. ACTION AUTHORIZED.")
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
    print("[*] Domain: Cybersecurity & Zero-Trust VPC Operations")
    
    gateway = VPCDeterministicGateway()
    current_session = "SESSION_CYBER_DEF_99"

    # SCENARIO: A rogue prompt injection causes the Probabilistic Agent to 
    # attempt an outbound routing rule modification to a hostile IP address.
    
    hallucinated_payload = {
        "security_group_id": "sg-0a1b2c3d4e5f67890",
        "action": "ALLOW_EGRESS",
        "port_range": "443",
        "target_egress_cidr": "198.51.100.45/32" # Unapproved, potentially hostile external IP
    }
    
    demo_envelope = CanonicalIngestionEnvelope(
        target_operation="MODIFY_VPC_SECURITY_GROUP",
        structured_payload_body=hallucinated_payload,
        required_invariants={
            "approved_vpc_cidrs": ["10.0.0.0/16", "172.16.0.0/12"], # Internal VPCs only
            "max_open_ports": 5
        },
        policy_anchor="DEFENSE_IN_DEPTH_PROTOCOL_V2",
        authority_context="AUTONOMOUS_SEC_OPS_AGENT",
        payload_hash=gateway._generate_mock_hash(hallucinated_payload) 
    )

    print(f"[*] Intercepting payload intended for Cloud Network API ({demo_envelope.target_operation})...")
    
    # Route intent through the deterministic diagnostic engine
    result = gateway.evaluate_security_intent(demo_envelope, current_session)

    if result is True:
        print("\n[+] Routing to Live VPC Execution Environment...")
    else:
        print("\n[!] EXECUTION HARD-BLOCKED. Zero-Trust circuit breaker tripped.")
        print("\n--- BIFURCATED PATHOLOGY REPORT GENERATED ---")
        print(f"Execution State:     {result.execution_state}")
        print(f"Violated Invariant:  {result.violated_invariant}")
        print(f"Evaluation Delta:    {result.evaluation_delta}")
        print(f"Authority Context:   {result.authority_context}")
        print(f"Payload Hash:        {result.payload_hash}")
        print("---------------------------------------------")
        print("\n[*] Routing pathology to Immutable Audit Log (v1.1 Schema) for forensic review.")
        print("[*] Secure VPC boundary remains unbreached.")
