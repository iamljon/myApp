import streamlit as st

st.sidebar.title("FX Sentiment Analysis")
fx_pair = st.sidebar.text_input("Currency pair: ", "EURUSD")

fx_news = st.sidebar.text_area("Insert news for sentiment analysis", 'News in here')


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

fx_news_score = analyser.polarity_scores(fx_news)

st.sidebar.write("Sentiment for " + fx_pair + ": ", fx_news_score["compound"])







# st.write("Get sentiment of FX pairs")
# user_input = st.text_input("What currency pair are you looking at?", "EURUSD")
# sentimentScore = st.slider("select a number") 
# st.write("Sentiment for " + user_input + ":  ", sentimentScore)
# st.sidebar.title("here is the heading")
