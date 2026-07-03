from flask import Flask, request, render_template_string
from EmotionDetection.emotion_detection import format_output

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Detector de Emociones</title>
</head>
<body>
    <h1>Detector de Emociones</h1>
    <form method="POST">
        <input type="text" name="text" placeholder="Escribe algo..." required>
        <button type="submit">Detectar Emoción</button>
    </form>
    <p>{{ result }}</p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form.get('text', '')
        if text.strip():
            result = format_output(text)
        else:
            result = "Por favor, ingresa un texto válido."
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)