from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Function to simulate WiFi signal strength
def simulate_wifi_signal():
    return random.randint(30, 100)

# Function to classify the signal
def classify_signal(signal_strength):
    if signal_strength > 75:
        return "Good Signal"
    elif 50 <= signal_strength <= 75:
        return "Moderate Signal"
    else:
        return "Weak Signal"

# Home route (Ensure 'templates/index.html' exists)
@app.route('/')
def index():
    return render_template("index.html")

# API route to get WiFi signal strength
@app.route('/api/wifi')
def api_wifi():
    signal_strength = simulate_wifi_signal()
    classification = classify_signal(signal_strength)
    return jsonify({
        "signal_strength": signal_strength,
        "classification": classification
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
