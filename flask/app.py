from flask import Flask, jsonify, request
from flask_cors import CORS
from googletrans import Translator
from summarizer import Summarizer
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify('ping pong!')

# 01_sentiment_analysis
@app.route('/sentiment_analysis', methods=['POST'])
def sentiment_analysis():
    try:
        data = request.get_json()
        input_text = data['text']
        sid = SentimentIntensityAnalyzer()
        sentiment_score = sid.polarity_scores(input_text)

        if sentiment_score['compound'] >= 0.1:
            sentiment = "Positive"
        elif sentiment_score['compound'] <= -0.1: 
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return jsonify({'sentiment': sentiment, 'sentiment_score': sentiment_score['compound']})
    except Exception as e:
        return jsonify({'error': str(e)})
    
# 02_name_entity_recognition
@app.route('/name_entity_recognition', methods=['POST'])
def name_entity_recognition():
    try:
        nlp = spacy.load("en_core_web_sm")

        data = request.get_json()
        input_text = data['text']
        doc = nlp(input_text)

        # Should return jsonify({})
        for ent in doc.ents:
            print(f"Entity: {ent.text}, Type: {ent.label_}")

    except Exception as e:
        return jsonify({'error': str(e)})
    
# 04_text_summarization
@app.route('/text_summarization', methods=['POST'])
def text_summarization():
    try:
        data = request.get_json()
        input_text = data['text']
        bert_model = Summarizer()
        summary = bert_model(input_text)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)})

# 05_language_translation
@app.route('/language_translation', methods=['POST'])
def language_translation():
    try:
        data = request.get_json()
        input_text = data['text']

        translator = Translator()
        translated_text = translator.translate(input_text, dest='fr').text

        return jsonify({'original': input_text, 'translated': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
