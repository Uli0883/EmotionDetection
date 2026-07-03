import json
import requests

def emotion_detector(text_to_analyze):
    """
    Versión simulada para pruebas (sin conexión a la API).
    """
    if not text_to_analyze or text_to_analyze.strip() == '':
        return {
            'error': 'Invalid text! Please try again.',
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Simulación de respuesta según el texto
    text_lower = text_to_analyze.lower()
    if 'happy' in text_lower or 'love' in text_lower or 'joy' in text_lower:
        return {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95, 'sadness': 0.0, 'dominant_emotion': 'joy'}
    elif 'angry' in text_lower or 'hate' in text_lower:
        return {'anger': 0.95, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'anger'}
    elif 'sad' in text_lower or 'depressed' in text_lower:
        return {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.95, 'dominant_emotion': 'sadness'}
    elif 'scared' in text_lower or 'fear' in text_lower:
        return {'anger': 0.0, 'disgust': 0.0, 'fear': 0.95, 'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'fear'}
    elif 'disgust' in text_lower or 'awful' in text_lower:
        return {'anger': 0.0, 'disgust': 0.95, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'disgust'}
    else:
        return {'anger': 0.1, 'disgust': 0.1, 'fear': 0.1, 'joy': 0.1, 'sadness': 0.1, 'dominant_emotion': 'joy'}

def format_output(text_to_analyze):
    result = emotion_detector(text_to_analyze)
    if result.get('dominant_emotion'):
        return (f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']}, "
                f"'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}.")
    else:
        return "Invalid text! Please try again."