
from flask import Flask,render_template,request
import pandas as pd
import pickle

# Load the trained pipeline
model_pipeline2 = pickle.load(open('model_pipeline2.pkl', 'rb'))

application2 = Flask(__name__)
app = application2

@app.route('/')
def home():
    return render_template('home2.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Collect input from form
        features = {
            'name':[request.form['name']],
            'company': [request.form['company']],
            'year': [int(request.form['year'])],
            'kms_driven': [float(request.form['kms_driven'])],
            'fuel_type':[request.form['fuel_type']]
        }
        
        # Convert input into DataFrame
        input_df = pd.DataFrame(features)
        
        # Predict using the trained pipeline
        prediction = model_pipeline2.predict(input_df)
        
        # Render the result
        return render_template('result2.html', prediction_text=f'Predicted Price: ₹{int(prediction[0])}')
    return render_template('home2.html')

if __name__ == '__main__':
    app.run(debug=True)