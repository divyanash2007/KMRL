import joblib

model = joblib.load("document_classifier.joblib")

while True:
    text = input("\nEnter a document paragraph (or 'exit'): ")

    if text.lower() == "exit":
        break

    prediction = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities) * 100

    print("\nPredicted Category:", prediction)
    print("Confidence:", round(confidence, 2), "%")

    print("\nAll Category Probabilities:")

    for category, probability in zip(
        model.classes_, probabilities
    ):
        print(f"{category}: {probability * 100:.2f}%")
