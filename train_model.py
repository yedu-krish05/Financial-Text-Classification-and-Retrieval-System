import joblib
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

def train():
    print("Fetching dataset...")
    # Using categories that might simulate different types of articles
    categories = ['comp.graphics', 'rec.autos', 'sci.space', 'talk.politics.mideast']
    data_train = fetch_20newsgroups(subset='train', categories=categories, remove=('headers', 'footers', 'quotes'))
    data_test = fetch_20newsgroups(subset='test', categories=categories, remove=('headers', 'footers', 'quotes'))

    print("Training model...")
    pipeline = make_pipeline(
        TfidfVectorizer(stop_words='english', max_features=5000),
        MultinomialNB()
    )

    pipeline.fit(data_train.data, data_train.target)

    print("Evaluating model...")
    predictions = pipeline.predict(data_test.data)
    report = classification_report(data_test.target, predictions, target_names=data_train.target_names)
    print("Classification Report:")
    print(report)

    model_data = {
        'pipeline': pipeline,
        'target_names': data_train.target_names
    }
    model_path = 'financial_model.pkl'
    joblib.dump(model_data, model_path)
    print(f"Model saved to {model_path}")

if __name__ == '__main__':
    train()
