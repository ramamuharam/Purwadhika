from flask import Flask
import joblib
app = Flask(__name__)

# home route
@app.route('/')
def home():
    return 'Prediksi [1,1,1,1] = ' + str(model.predict([[1, 1, 1, 1]])[0])

if __name__ == '__main__':
    model = joblib.load('modelJoblib')
    app.run(debug = True)