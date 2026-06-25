from symptom_checker import predict_disease, get_confidence
from report_generator import generate_report

print("=" * 40)
print("      AI HEALTH SYMPTOM CHECKER")
print("=" * 40)

print("\nEnter Symptoms (1 = Yes, 0 = No)\n")

fever = int(input("Fever (0/1): "))
cough = int(input("Cough (0/1): "))
headache = int(input("Headache (0/1): "))
bodypain = int(input("Body Pain (0/1): "))
fatigue = int(input("Fatigue (0/1): "))

symptoms = [fever, cough, headache, bodypain, fatigue]

disease = predict_disease(symptoms)

confidence = get_confidence(symptoms)

print("\n" + "=" * 40)
print("RESULT")
print("=" * 40)

print("Predicted Disease :", disease)
print("Confidence Score  :", confidence, "%")

generate_report(symptoms, disease, confidence)

print("\nHealth report saved successfully!")