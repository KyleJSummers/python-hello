var Http = require("http");

Http.createServer(function(req, res) {

	res.writeHead(303, {"Location": "https://www.reddit.com"});
	res.end();

}).listen(8080);
