
# controllor class

from flask import Flask, request, render_template

# import redis client
import redis

# Create application object
app = Flask(__name__)
default_key = '1'
# create redis cache.
# we are going to run redis server in seperate container. 
# so for host refer "redis" container
cache = redis.StrictRedis(host='redis', port=6379, db=0)

# Register view for get and post
@app.route('/', methods=['GET', 'POST'])
def mainpage():

	key = default_key
	if 'key' in request.form:
	    key = request.form['key']

	if request.method == 'POST' and request.form['submit'] == 'save':
		cache.set(key, request.form['cache_value'])

	cache_value = None;
	if cache.get(key):
		#redis returns in bytestream. so convert to utf8
		cache_value = cache.get(key).decode('utf-8')

	return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
