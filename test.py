from flask import Flask , render_template , request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('TestModel.pkl','rb'))

@app.route('/')
def home():
    return render_template('FirstPage.html')


@app.route('/getData',methods=['POST'])
def home1():
    First_Name = request.form['First_Name']
    Last_Name = request.form['Last_Name']
    gender = request.form['Gender']
    gen = int(1) if gender=="Male" else int(0)
    married = request.form['Married']
    marr = int(1) if married=="Yes" else int(0)
    education = request.form['Education']
    edu = int(0) if education=="Graduate" else int(0)
    self_Employed = request.form['Self_Employed']
    slfEmp = int(1) if self_Employed=="Yes" else int(0)
    dependents = int(request.form['Dependents'])
    Loan_Amount_Term = int(request.form['Loan_Amount_Term'])
    Credit_History = int(request.form['Credit_History'])
    Property_Area = request.form['Property_Area']
    if Property_Area=="Rural":
        a=0
        b=0
    elif Property_Area=="Urban":
        a=0
        b=1
    else:
        a=1
        b=0
        
    ApplicantIncome = int(request.form['ApplicantIncome'])
    CoApplicantIncome = int(request.form['CoApplicantIncome'])
    loanAmount = int(request.form['loanAmount'])
    
    final_ApplicantIncome = np.sin(ApplicantIncome)
    final_LoanAmount = np.sin(loanAmount)
    final_CoapplicantIncome =np.log2((CoApplicantIncome+1)**(1/4))
    
    #output = model.predict([[360,0,0.573555,0.363171,2.800990,3,1,1,1,1,1,0]])
      #  model.predict ([[Loan_Amount_Term,Credit_History,final_ApplicantIncome,final_LoanAmount,final_CoapplicantIncome,dependents,gen,marr,edu,slfEmp,a,b]])
#output[0]

    #output = model.predict([[ApplicantIncome,loanAmount,Loan_Amount_Term,Credit_History,gen
    print([[Loan_Amount_Term,Credit_History,final_ApplicantIncome,final_LoanAmount,final_CoapplicantIncome,dependents,gen,marr,edu,slfEmp,a,b]])
    output = model.predict ([[Loan_Amount_Term,Credit_History,final_ApplicantIncome,final_LoanAmount,final_CoapplicantIncome,dependents,gen,marr,edu,slfEmp,a,b]])
    
    if output[0]==1:
        return render_template('FirstPage.html',prediction= "Output :  {} {} is Eligible for loan".format(First_Name,Last_Name))
    else:
        return render_template('FirstPage.html',prediction= "Output :  {} {} is Not Eligible for loan".format(First_Name,Last_Name))
    return ""

if __name__=="__main__":
    app.run(debug=True,use_reloader=False)