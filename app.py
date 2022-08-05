from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def function_to_calculate():
    var_1 = request.form.get("var_1", type=float, default=0)
    var_2 = request.form.get("operation", type=str, default="")
    data=pd.read_csv("F:\studentmarks\student_scores.csv")
    data.shape
    (25,2)
    x=data.iloc[:,:-1].values
    y=data.iloc[:,1].values

    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    from sklearn.linear_model import LinearRegression
    mod=LinearRegression()
    mod.fit(x_train, y_train)


    operation = request.form.get("operation")

    if(operation == 'Daily'):
        y1_pred=mod.predict([[var_1]])
        result = y1_pred
    if(operation == 'Weekly'):
        y1_pred=mod.predict([[var_1/7]])
        result = y1_pred

    a=[99.9]
    if(result>a):
        result=a

    result = np.round_(result, decimals = 2)
    result=(', '.join(map(str, result)))
    entry=result
    # print(var_1)
    # print(var_2)
    return render_template('form.html',entered_value1=var_1,entered_value2=var_2, entry=entry)










if __name__ == '__main__':
    app.run(debug=True)
    