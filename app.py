#from flask import Flask
#from flask import render_template
#import pickle
#import numpy as np
#from flask import request
#
#model1 = pickle.load(open('place.pkl', 'rb'))
#
#app=Flask(__name__)
#
#@app.route('/')
#def index():
#    return render_template('place_web.html')
#
#@app.route('/result',methods=['POST'])
#def get_value():
#    company=(request.form['company'])
#    position=(request.form['position'])
#    passing_year=(request.form['passing_year'])
#    percentage=(request.form['percentage'])
#    a_i_rating=(request.form['a_i_rating'])
#        
#    arr = np.array([[company, position, passing_year, percentage, a_i_rating]])
#    prediction=model1.predict(arr)
#    print(prediction[0])
#    
#    return render_template('place_web.html',prediction=[prediction[0]])
#
#if __name__=="__main__":
#    app.run()



from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model
model = pickle.load(open('place.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main page with the input form
    return render_template('place_web.html')

@app.route('/result', methods=['POST'])
def get_value():
    # Collect input values from the form
    try:
        company = int(request.form['company'])
        position = int(request.form['position'])
        passing_year = int(request.form['passing_year'])
        percentage = float(request.form['percentage'])
        a_i_rating = float(request.form['a_i_rating'])

        # Prepare the input array for prediction
        arr = np.array([[company, position, passing_year, percentage, a_i_rating]])

        # Make prediction
        prediction = model.predict(arr)
        print(prediction[0])

        # Return the result to the HTML template
        return render_template('place_web.html', prediction=prediction[0])
    except Exception as e:
        # Error handling for debugging
        print("Error occurred:", e)
        return render_template('place_web.html', prediction="Error: Check input values or model")

if __name__ == "__main__":
    app.run()