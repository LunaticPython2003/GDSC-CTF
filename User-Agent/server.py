from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def root():
    # Check if User-Agent header is set to 'GDSC'
    user_agent = request.headers.get('User-Agent')
    if user_agent != 'GDSC':
        return '''<html lang="en"><head>
      <title> What the User-Agent! </title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


</head>

<body>

    <div class="container">
      <div class="jumbotron">
        <p class="lead"></p>
		<div class="row">
			<div class="col-xs-12 col-sm-12 col-md-12">
				<h3 style="color:red">Only people who use the official PicoBrowser are allowed on this site!</h3>
			</div>
		</div>
		<br>
		
			<img src="/static/who_r_u.gif">
		
	</div>
    <footer class="footer">
        <p>© GDSC</p>
    </footer>

</div>
<script>
$(document).ready(function(){
    $(".close").click(function(){
        $("myAlert").alert("close");
    });
});
</script>


</body></html>
'''

    # Check if Accept header is set to '1'
    accept_header = request.headers.get('Accept')
    if accept_header != '1':
        return '''
<html lang="en"><head>
      <title> What the User-Agent! </title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


</head>

<body>

    <div class="container">
      <div class="jumbotron">
        <p class="lead"></p>
		<div class="row">
			<div class="col-xs-12 col-sm-12 col-md-12">
				<h3 style="color:red">Only people who use the official PicoBrowser are allowed on this site!</h3>
			</div>
		</div>
		<br>
		
			<img src="/static/i-accept-accept.gif">
		
	</div>
    <footer class="footer">
        <p>© GDSC</p>
    </footer>

</div>
<script>
$(document).ready(function(){
    $(".close").click(function(){
        $("myAlert").alert("close");
    });
});
</script>


</body></html>
'''

    return 'Welcome to the protected page!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
