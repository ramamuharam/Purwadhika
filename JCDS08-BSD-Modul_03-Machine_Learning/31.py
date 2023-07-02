from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('formulir.html')

@app.route('/hasil', methods=['GET', 'POST'])
def hasil():
    if request.method == 'POST':
        data = request.form
        x = model.predict([
            [float(data['SL']), float(data['SW']), float(data['PL']), float(data['PW'])]
        ])[0]
        return 'Prediksi = ' + str(x)

if __name__ == '__main__':
    model = joblib.load('modelJoblib')
    app.run(debug = True)