import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')

df = pd.read_csv(r"D:\Engineering\CDAC_ALL_MODULES\NLP\DisneylandReviews.csv")
print(df.head())