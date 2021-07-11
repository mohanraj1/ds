from flask import Flask

# Create application object
app = Flask(__name__)

# View function - <url>/ --> calls helloworld method
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Initialize and starts flask appp 
if __name__ == '__main__':
    # Exposed at 0.0.0.0 - app server can be accessed by other containers
    # not using localhost or 127.0.0.1
    app.run(host='0.0.0.0')
