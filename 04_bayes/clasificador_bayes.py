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

# Conversion
df['label'] = df.label.map({'ham': 0, 'spam': 1})

# Visualizar las dimensiones de los datos
print(df.shape)

# Definir los documentos
documents = ['Hello, how are you!',
                'Win money, win from home.',
                'Call me now.',
                'Hello, Call hello you tomorrow?']

# Importar el contador de vectorizacion e inicializarlo
count_vector = CountVectorizer()

# Visualizar del objeto'count_vector' que es una instancia de 'CountVectorizer()'
print(count_vector)

count_vector.fit(documents)
names = count_vector.get_feature_names()
print(names)

doc_array = count_vector.transform(documents).toarray()
print(doc_array)

frequency_matrix = pd.DataFrame(data=doc_array, columns=names)
print(frequency_matrix)

X_train, X_test, y_train, y_test = train_test_split(df['sms_message'], df['label'], random_state=1)
print('Number of rows in the total set: {}'.format(df.shape[0]))
print('Number of rows in the training set: {}'.format(X_train.shape[0]))
print('Number of rows in the test set: {}'.format(X_test.shape[0]))

# Instantiate the CountVectorizer method
count_vector = CountVectorizer()

# Fit the training data and then return the matrix
training_data = count_vector.fit_transform(X_train)

# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
testing_data = count_vector.transform(X_test)

naive_bayes = MultinomialNB()
print(naive_bayes.fit(training_data, y_train))

predictions = naive_bayes.predict(testing_data)

print('Exactitud: ', format(accuracy_score(y_test, predictions)))
print('Precisión: ', format(precision_score(y_test, predictions)))
print('Sensibilidad: ', format(recall_score(y_test, predictions)))
print('F1 score: ', format(f1_score(y_test, predictions)))

# https://medium.com/datos-y-ciencia/algoritmos-naive-bayes-fudamentos-e-implementaci%C3%B3n-4bcb24b307f
