def get_suggestion(disease):

    suggestions = {
        "Flu": "Drink plenty of water and take proper rest.",
        "Cold": "Stay warm and drink hot fluids.",
        "Dengue": "Consult a doctor immediately and stay hydrated.",
        "Malaria": "Seek medical treatment as soon as possible.",
        "Migraine": "Take rest and avoid bright lights.",
        "Typhoid": "Maintain hygiene and consult a healthcare professional.",
        "Covid19": "Isolate yourself and consult a doctor.",
        "Allergy": "Avoid allergens and take prescribed medicines.",
        "Viral Fever": "Take rest and drink sufficient fluids.",
        "Stress": "Practice relaxation and get enough sleep."
    }

    return suggestions.get(disease, "Consult a healthcare professional.")


def generate_report(symptoms, disease, confidence):

    suggestion = get_suggestion(disease)

    report = f"""
===================================
      AI HEALTH REPORT
===================================

Symptoms:
{symptoms}

Predicted Disease:
{disease}

Confidence Score:
{confidence}%

AI Recommendation:
{suggestion}

Disclaimer:
This project is for educational purposes only.
Please consult a healthcare professional for medical advice.

===================================
"""

    with open("health_report.txt", "w") as file:
        file.write(report)

    print("Health Report Generated Successfully!")