def get_suggestion(category):
    suggestions = {
        "Food Waste": "Contact kitchen admin. Consider starting a leftover box.",
        "Mental Health": "Speak to a friend or counselor. Journaling may help.",
        "Digital Abuse": "Limit screen time. Report incidents to support helplines.",
        "Education/Career": "Explore internships. Build a strong resume and LinkedIn.",
        "General": "Be specific. Reach out to local support groups if needed."
    }
    return suggestions.get(category, "No suggestion available.")
