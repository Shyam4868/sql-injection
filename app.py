
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

with open("sql_injection_model.pkl", "rb") as model_file:
    model, vectorizer = pickle.load(model_file)

def detect_sql_injection(input_text):
    input_vector = vectorizer.transform([input_text])
    prediction_prob = model.predict_proba(input_vector)[:, 1] 
    threshold = 0.5
    if prediction_prob >= threshold:
        return "unsafe"
    else:
        return "safe"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_sql_injection():
    input_text = request.form.get("input_text")
    result = detect_sql_injection(input_text)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
