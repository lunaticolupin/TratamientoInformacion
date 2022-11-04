# Importar la libreria Pandas
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# Dividir los datos en conjunto de entrenamiento y de test
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Dataset de https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
df = pd.read_table('smsspamcollection/SMSSpamCollection',
                   sep='\t',
                   names=['label', 'sms_message'])
# Visualización de las 5 primeras filas
print(df.head())

