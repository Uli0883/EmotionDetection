import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am so happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am so angry right now!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness(self):
        result = emotion_detector("I am so sad today.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I am scared of the dark.")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_disgust(self):
        result = emotion_detector("This food tastes awful.")
        self.assertEqual(result['dominant_emotion'], 'disgust')

if __name__ == '__main__':
    unittest.main()