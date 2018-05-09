from flask import Flask, Response
import json
import os

# app = Flask(__name__)

app = Flask(__name__, static_url_path='', static_folder='.')
app.add_url_rule('/', 'root', lambda: app.send_static_file('box_index.html'))


cur_dir = os.path.dirname(__file__)

data = json.load(open(os.path.join(cur_dir, 'box_of_rain_050718.json'), 'r'))



@app.route("/data")
def box_of_rain():
	return Response(data.dumps(),
	mimetype='application/json',
	headers={
	'Cache-Control': 'no-cache',
	'Access-Control-Allow-Origin': '*'
	}
	)

if __name__ == '__main__':
	app.run(port=8000)