@app.route("/hello")
def hello_ssti():
	# fileupload_vulnerability
    if request.args.get('name'):
        name = request.args.get('name')
        template = f'''<div>
        <h1>Hello</h1>
        {name}
</div>
