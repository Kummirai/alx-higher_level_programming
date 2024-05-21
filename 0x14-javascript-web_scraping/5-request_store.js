#!/usr/bin/node

let fs = remote('fs');
let request = require('request');

request.get(process,argv[2], function(ree, response, err, response, body) {
	if (err) throw err;
	else {
		fs.writeFile(process.argv[3], body, 'utf8');
	}
});
