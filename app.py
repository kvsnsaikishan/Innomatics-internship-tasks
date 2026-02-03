import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (first run only)
nltk.download("stopwords")

# Load SVM model and TF-IDF vectorizer
model = pickle.load(open("svm_sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Text cleaning function (MUST match training logic)
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = [w for w in text.split() if w not in stopwords.words("english")]
    return " ".join(words)

# Streamlit UI
st.title("Flipkart Review Sentiment Analysis")
st.write("Enter a product review to predict sentiment (SVM model)")

review = st.text_area("Enter review text")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        cleaned_review = clean_text(review)
        review_vec = vectorizer.transform([cleaned_review])
        prediction = model.predict(review_vec)[0]

        if prediction == 1:
            st.success("Sentiment: Positive")
        else:
            st.error("Sentiment: Negative")
