from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Allow frontend to talk to backend

# Load ML assets
model = joblib.load("stream_counselling_model.pkl")
encoder = joblib.load("stream_label_encoder.pkl")

# Feature engineering (same as training)
def calculate_features(math, english, science, failures):
    avg_score = (math + english + science) / 3
    academic_strength = avg_score / 100
    math_inclination = math / 100
    language_inclination = english / 100
    consistency = 1 / (1 + failures)

    return [
        academic_strength,
        consistency,
        math_inclination,
        language_inclination
    ]

# Counselling explanation
def counselling_reason(stream):
    if stream == "Science":
        return "Strong academic performance and mathematical ability suggest Science stream."
    elif stream == "Commerce":
        return "Balanced academic performance suggests Commerce stream."
    else:
        return "Language skills and overall profile suggest Arts or Humanities."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = calculate_features(
        data["math"],
        data["english"],
        data["science"],
        data["failures"]
    )

    prediction = model.predict([features])[0]
    stream = encoder.inverse_transform([prediction])[0]

    return jsonify({
        "recommended_stream": stream,
        "reason": counselling_reason(stream)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

