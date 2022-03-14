from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from applicationinsights.flask.ext import AppInsights

app = Flask(__name__)
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'YOUR_INSTRUMENTATION_KEY'
appinsights = AppInsights(app)
# define log level to DEBUG
app.logger.setLevel(logging.DEBUG)

# force flushing application insights handler after each request
@app.after_request
def after_request(response):
    appinsights.flush()
    return response

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/alive')
def alive():
   print('App is very much alive')
   app.logger.debug('This is a debug log message for alive')
   return render_template('alive.html')



@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
