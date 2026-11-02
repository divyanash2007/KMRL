import random
import pandas as pd
from pathlib import Path

random.seed(42)

templates = {
    "Maintenance": [
        "The {equipment} at {location} {issue}.",
        "A maintenance team is required to {action} the {equipment}.",
        "The inspection report indicates that the {equipment} needs {action}.",
        "A complaint has been received regarding the malfunctioning {equipment}.",
    ],
    "Safety": [
        "A {incident} was reported at {location}. Immediate safety measures are required.",
        "The safety inspection identified a {hazard} near {location}.",
        "An employee reported an unsafe condition involving {hazard}.",
        "The incident report recommends corrective safety measures to prevent accidents.",
    ],
    "Finance": [
        "The finance department has received an invoice for {amount} related to {expense}.",
        "A payment of {amount} is pending approval for {expense}.",
        "The monthly financial report shows an increase in {expense}.",
        "The department has requested reimbursement for {expense}.",
    ],
    "Human Resources": [
        "An employee has submitted a request for {hr_request}.",
        "The HR department is processing an employee {hr_request}.",
        "A staff member has raised a concern regarding {hr_issue}.",
        "The employee records need to be updated following {hr_event}.",
    ],
    "Operations": [
        "Train services at {location} experienced {operational_issue}.",
        "The operations team has revised the train {schedule_item}.",
        "Passenger movement at the station requires operational coordination.",
        "The daily operations report highlights {operational_issue}.",
    ],
    "Procurement": [
        "The department has requested quotations for purchasing {item}.",
        "A purchase order is required for {item}.",
        "The procurement team is evaluating vendor bids for {item}.",
        "The vendor selection process for {item} is awaiting approval.",
    ],
    "Passenger Grievances": [
        "A passenger has submitted a complaint regarding {complaint}.",
        "The customer service team received feedback about {complaint}.",
        "A commuter is requesting assistance with {complaint}.",
        "The grievance register contains a complaint about {complaint}.",
    ],
    "Legal & Compliance": [
        "The legal department has received a notice concerning {legal_issue}.",
        "The contract requires review to ensure compliance with {regulation}.",
        "A legal review has been requested regarding {legal_issue}.",
        "The compliance team identified a possible violation of {regulation}.",
    ],
}

values = {
    "equipment": ["escalator", "elevator", "rail track", "signalling system", "air conditioning unit", "station lighting", "platform screen door", "water pump"],
    "location": ["Platform 1", "Platform 2", "the station entrance", "the control room", "the depot", "the ticket counter"],
    "issue": ["has stopped working", "requires urgent repair", "is showing abnormal vibration", "failed during inspection"],
    "action": ["repair", "inspect", "replace", "service"],
    "incident": ["slip and fall", "electrical accident", "minor injury", "fire alarm activation"],
    "hazard": ["exposed electrical wire", "wet floor", "damaged handrail", "blocked emergency exit"],
    "amount": ["Rs. 25,000", "Rs. 1,50,000", "Rs. 75,000", "Rs. 10,000"],
    "expense": ["equipment servicing", "electricity bills", "staff travel", "contract payments"],
    "hr_request": ["leave application", "salary revision", "transfer request", "training request"],
    "hr_issue": ["workplace conduct", "attendance records", "staff allocation", "employee benefits"],
    "hr_event": ["a department transfer", "a new appointment", "employee resignation"],
    "operational_issue": ["a service delay", "schedule disruption", "increased passenger traffic", "a platform change"],
    "schedule_item": ["timetable", "service frequency", "platform allocation", "duty roster"],
    "item": ["electrical cables", "office computers", "safety equipment", "maintenance tools", "station furniture"],
    "complaint": ["delayed refund", "ticketing issue", "unclean station", "staff behaviour", "missing information"],
    "legal_issue": ["a contractual dispute", "a vendor agreement", "a compensation claim", "a court notice"],
    "regulation": ["government procurement rules", "labour regulations", "safety standards", "contractual obligations"],
}

rows = []
samples_per_category = 300

for category, category_templates in templates.items():
    for _ in range(samples_per_category):
        template = random.choice(category_templates)
        text = template.format(
            **{
                key: random.choice(options)
                for key, options in values.items()
                if "{" + key + "}" in template
            }
        )
        rows.append({
            "text": text,
            "category": category
        })

random.shuffle(rows)

df = pd.DataFrame(rows)
output_path = Path("data/synthetic_documents.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("Dataset created successfully!")
print("Total documents:", len(df))
print("\nCategory distribution:")
print(df["category"].value_counts())
print("\nSaved to:", output_path)
