from flask import Flask, render_template, request, redirect
from display import display as d
from gpiozero import RGBLED, Button

led = RGBLED(red=18, green=14, blue=15)
button = Button(2)

disp_unit_1 = d.DispUnit(4,16,23,20,10,27,21,22)
disp_unit_2 = d.DispUnit(1,25,17,7,8,3,24,12)
disp = d.Display([disp_unit_1,disp_unit_2])

app = Flask(__name__)

number = 0
@app.route("/", methods=['GET', 'POST'])
def index():
    global number
    message = "Display your number"

    if request.method == 'POST':
        if request.form.get('add_one') == '+1':
            print("+1")
            number += 1
            pass
        elif request.form.get('add_five') == '+5':
            print('+5')
            number += 5
            pass
        elif request.form.get('sub_one') == '-1':
            print('-1')
            number -= 1
            pass
        elif request.form.get('sub_five') == '-5':
            print('-5')
            number -= 5
            pass
        else:
            pass

        num = request.form.get('count')
        if num is not None:
            number = int(num)
        print(num)

    elif request.method == 'GET':
        return(render_template('index.html', message=message))

    if number < 0:
        number = 0
    elif number > 99:
        number = 99

    disp.dispNumber(number)

    return(render_template('index.html', message='done'))
#@app.route("/", methods=('GET', 'POST'))
#def create():
#    message = "Test"

#    if request.form['submit_button'] == '+1':
#        print("+1")
#        pass
#    elif request.form['submit_button'] == '+5':
#        pass

#    print(request.form['title'])
#    disp.dispNumber(request.form['title'])
#    return(redirect("/"))

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")

