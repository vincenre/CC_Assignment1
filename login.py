from flask import Flask, redirect, url_for, request, render_template
application = Flask(__name__)


@application.route('/success/<result>')
def success(result):
    return 'Result is %s' % result

@application.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        number = request.form['number']
        nmbr = int(number)
        temp = nmbr
        rev = 0
        while(nmbr>0):
              dig=nmbr%10
              rev=rev*10+dig
              nmbr = nmbr//10
        if(temp==rev):
              result ='a PALINDROME'
              return redirect(url_for('success',result=result))
        else:
            result ='not a PALINDROME'
            return redirect(url_for('success',result=result))
    return render_template('index.html')



if __name__ == '__main__':
   application.run(host='0.0.0.0')
