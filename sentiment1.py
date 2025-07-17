from newspaper import Article
from textblob import TextBlob
import nltk
nltk.download('punkt_tab')

url = 'https://en.wikipedia.org/wiki/Mathematics'

article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
senntiment = blob.sentiment.polarity
print(senntiment)
