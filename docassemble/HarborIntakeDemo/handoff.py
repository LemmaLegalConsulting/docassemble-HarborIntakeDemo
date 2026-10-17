"""Pure, offline adapter. No credentials, HTTP client, or live-send option."""
import hashlib
import json
from html import escape

def html_escape(value):
    return escape(str(value))

def build_payload(*, first, last, email, phone, contact_method, safe_contact, language, problem, details, housing_issue, deadline, household_size, monthly_income, documents):
    return {
        "schema": "harbor-demo-intake/v1",
        "client": {"first_name": first, "last_name": last, "email": email if contact_method == "Email" else None, "phone": phone if contact_method == "Phone" else None, "preferred_contact": contact_method, "safe_contact_instructions": safe_contact, "language": language},
        "matter": {"problem_type": problem, "description": details, "housing_issue": housing_issue if problem == "Housing" else None, "deadline": deadline or None, "priority": "Deadline review" if deadline else "Standard review"},
        "household": {"size": int(household_size), "monthly_income": float(monthly_income)},
        "documents": documents,
        "consent": {"simulation_authorized": True},
    }

def simulate_handoff(payload, consent):
    if not consent:
        raise ValueError("Consent is required before simulating a handoff")
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    fingerprint = hashlib.sha256(encoded.encode()).hexdigest()
    return {"simulation": True, "status": "accepted", "reference": "DEMO-" + fingerprint[:10].upper(), "payload_sha256": fingerprint, "destination": "Offline LegalServer adapter", "network_requests": 0, "payload": payload}

def pretty_json(value):
    return json.dumps(value, indent=2, ensure_ascii=False)
