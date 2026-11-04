
import re

RULES = {
    "Maintenance": [
        {
            "keywords": ["malfunction", "breakdown", "equipment failure"],
            "priority": "High"
        },
        {
            "keywords": ["repair", "maintenance", "servicing"],
            "priority": "Medium"
        },
    ],

    "Safety": [
        {
            "keywords": ["accident", "injury", "fire", "emergency exit"],
            "priority": "Critical"
        },
        {
            "keywords": ["hazard", "unsafe condition", "safety violation"],
            "priority": "High"
        },
    ],

    "Finance": [
        {
            "keywords": ["invoice", "payment", "reimbursement"],
            "priority": "Medium"
        },
        {
            "keywords": ["budget", "financial statement", "expenditure"],
            "priority": "Medium"
        },
    ],

    "Human Resources": [
        {
            "keywords": ["leave application", "salary revision", "employee benefits"],
            "priority": "Medium"
        },
        {
            "keywords": ["attendance", "employee transfer", "recruitment"],
            "priority": "Low"
        },
    ],

    "Operations": [
        {
            "keywords": ["train schedule", "service disruption", "platform allocation"],
            "priority": "High"
        },
        {
            "keywords": ["train frequency", "operational planning"],
            "priority": "Medium"
        },
    ],

    "Procurement": [
        {
            "keywords": ["purchase order", "vendor quotation", "tender"],
            "priority": "Medium"
        },
        {
            "keywords": ["vendor selection", "procurement request"],
            "priority": "Medium"
        },
    ],

    "Passenger Grievances": [
        {
            "keywords": ["passenger complaint", "refund", "ticket issue"],
            "priority": "Medium"
        },
        {
            "keywords": ["poor service", "staff behaviour", "passenger feedback"],
            "priority": "Low"
        },
    ],

    "Legal & Compliance": [
        {
            "keywords": ["legal notice", "court order", "lawsuit"],
            "priority": "Critical"
        },
        {
            "keywords": ["contract dispute", "regulatory violation", "compliance"],
            "priority": "High"
        },
    ],
}


def classify_document(text):

    text = text.lower()

    matched_rules = []

    for category, rules in RULES.items():

        for rule in rules:

            matched_keywords = [
                keyword
                for keyword in rule["keywords"]
                if keyword in text
            ]

            if matched_keywords:
                matched_rules.append({
                    "category": category,
                    "matched_keywords": matched_keywords,
                    "priority": rule["priority"]
                })

    if not matched_rules:
        return {
            "category": "Unclassified",
            "priority": "Unknown",
            "matched_rules": []
        }

    # Select the highest priority matching rule.
    priority_order = {
        "Critical": 4,
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    matched_rules.sort(
        key=lambda x: priority_order[x["priority"]],
        reverse=True
    )

    return {
        "category": matched_rules[0]["category"],
        "priority": matched_rules[0]["priority"],
        "matched_rules": matched_rules
    }


if __name__ == "__main__":

    while True:

        text = input("\nEnter document text (or exit): ")

        if text.lower() == "exit":
            break

        result = classify_document(text)

        print("\nClassification:", result["category"])
        print("Priority:", result["priority"])
        print("Matched rules:", result["matched_rules"])
