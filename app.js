var express    = require('express');
var serveIndex = require('serve-index');
var app = express();

app.use(express.static(__dirname + '/assets'));

app.use('/', serveIndex('./assets', {
		'icons': true,
		'stylesheet': './public/css/index.css'
	}
));

app.listen( 7889 );
console.log("Yoyo, I'm at 7889");