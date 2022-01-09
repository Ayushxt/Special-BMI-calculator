#!python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    mess = ''
    prec = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
        if(bmi<=16):
            mess = "You are severely underweight"
            prec = "Eat more carbs and good fats with a good amount of protein. You can also do wieght training ,thanks"
        elif(bmi<=18.5):
            mess = "You are underweight"
            prec = "Eat more carbs and good fats with a good amount of protein. You can also do wieght training ,thanks"
        elif(bmi<=25):
            mess = "You are Healthy"
            prec = "Quite impressive, keept it up and stay healthy."
        elif(bmi<=30):
            mess = "you are overweight"
            prec = "Reduce the intake of carbohydrates and eat more protein and fuits and salad"
        else: 
            mess = "You are severely overweight"
            prec = "Sorry to say but you are health is at high risk, start working out and prefer not to eat junk food and eat heathy, consult a dietician"
    return render_template("bmi.html", bmi=bmi, message = mess, prec = prec)

def calc_bmi(Weight, Height):
    Height = Height/100
    BMI=Weight/(Height*Height)
    return BMI

if __name__ == '__main__':
    app.run()
