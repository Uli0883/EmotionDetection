from flask import Flask, request, jsonify, render_template_string
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Detector de Emociones</title>
</head>
<body>
    <h1>Detector de Emociones</h1>
    <form id="emotionForm">
        <input type="text" id="textInput" placeholder="Escribe algo..." required>
        <button type="submit">Detectar Emoción</button>
    </form>
    <div id="result"></div>

    <script>
        document.getElementById('emotionForm').onsubmit = async function(e) {
            e.preventDefault();
            const text = document.getElementById('textInput').value;
            const response = await fetch('/emotionDetector', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });
            const data = await response.json();
            if (data.error) {
                document.getElementById('result').innerHTML = `<p style="color:red">${data.error}</p>`;
            } else {
                document.getElementById('result').innerHTML = `
                    <p>For the given statement, the system response is 'anger': ${data.anger}, 'disgust': ${data.disgust}, 'fear': ${data.fear}, 'joy': ${data.joy}, 'sadness': ${data.sadness}. The dominant emotion is ${data.dominant_emotion}.</p>
                `;
            }
        };
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    data = request.get_json()
    text = data.get('text', '')
    result = emotion_detector(text)
    if result.get('dominant_emotion'):
        return jsonify(result)
    else:
        return jsonify({'error': 'Invalid text! Please try again.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)