from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask',
        'pytest',
        'pylint'
    ],
    author='Uli0883',
    description='Detector de emociones con Watson NLP'
)