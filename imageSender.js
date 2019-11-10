const request = require('request');
const screenshot = require('screenshot-node');
const nrc = require('node-run-cmd');
const average = require('image-average-color');
screenshot.saveScreenshot(300, 300, 1920, 1080, "imag.png", 
	(err)=>{
		if(err)
			console.log(err)
	});

let red, green, blue;
average('image.png', (err, color) => {
	if (err)
		console.log(err)
		return
	cponsole.log('take average');
	[red, green, blue, alpha] = color;
	console.log(color);
});


const out = nrc.run('average-color image.png');

request.post('http://localhost:31480', {
		json: {
			img: [red, green, blue]
		}
	}, (err, res, body) => {
	if (err){
		console.log(err);
		return;
	}
	//console.log(body)
});
