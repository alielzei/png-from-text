var express = require('express');
var app = express();

var port = process.env.PORT || 3000;

app.get('/', function(req, res){

	let text = req.query.text || 'api',
			size = req.query.size || 10,
			font = req.query.font || 'helvetica';

	let spawn = require("child_process").spawn,
			py = spawn('python', ["./image.py", text, size, font]);

	var dataString = '';

	py.stdout.on('data', function(data){
  	dataString += data.toString();
	});

	py.stdout.on('end', function(data){
		res.send('<img src="data:image/png;base64,' + dataString + '" >');
	});
 
});

app.listen(port, function(){
	console.log('app online')
});



