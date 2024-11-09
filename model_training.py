
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


data = [
    ("SELECT * FROM users WHERE username = 'admin' --", "unsafe"),
    ("DROP TABLE users", "unsafe"),
    ("SELECT password FROM users WHERE username='admin'", "unsafe"),
    ("' OR 1=1 --", "unsafe"),
    ("'; DROP TABLE users --", "unsafe"),
    ("Hello, how are you?", "safe"),
    ("I would like to know more about your services.", "safe"),
    ("This is just a test message.", "safe"),
    ("SELECT * FROM users WHERE id = 1", "safe"),
    ("Please let us know if you have any questions.", "safe"),
    ("Can I see the latest report?", "safe"),
    ("SELECT * FROM users WHERE id = 1", "safe"),
    ("SELECT * FROM products WHERE id = 5;", "safe"),
    ("SELECT * FROM orders WHERE customer_id = 123;", "safe"),
    ("UPDATE users SET password = 'newpassword' WHERE id = 1;", "safe")
]


texts, labels = zip(*data)


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)


model = MultinomialNB()
model.fit(X, labels)

with open("sql_injection_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model saved as sql_injection_model.pkl")
