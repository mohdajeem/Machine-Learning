# Sample documents - A List
documents = [
    "The quick brown fox jumps over the lazy dog",
    "The dog is quick and it is jumping over a fox",
    "Foxes are quick and dogs are lazy"
]

print(documents,'\n')

# start
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

features_names = vectorizer.get_feature_names_out()

dense_matrix = tfidf_matrix.todense()

for doc, vec in zip(documents, dense_matrix):
    print(f"Documents : {doc}")
    print(f"Tf-Idf-vect : {vec}")
    print('\n')
