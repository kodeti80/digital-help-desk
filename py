import csv
from datetime import datetime
from auto_suggest import get_suggestion

# Keyword-based simple categorization
def classify_issue(text):
    text = text.lower()
    if "food" in text or "waste" in text:
        return "Food Waste"
    elif "mental" in text or "stress" in text:
        return "Mental Health"
    elif "bully" in text or "online" in text:
        return "Digital Abuse"
    elif "career" in text or "job" in text:
        return "Education/Career"
    else:
        return "General"

print("📨 Enter your issue:")
issue = input("> ")
category = classify_issue(issue)
suggestion = get_suggestion(category)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

with open("issue_log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([timestamp, issue, category])

print(f"\n🗂️ Categorized as: {category}")
print(f"💡 Suggestion: {suggestion}")
