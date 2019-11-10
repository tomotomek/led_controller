const average = require('image-average-color');
const request = require('request');

let r, g, b;
function av(){
	average('image.png', (err, color) => {
		if (err) throw err;
		const [r, g, b, a] = color;
		return [r,g,b];
	});
}

const res = av();

console.log(res)
request.post('http://localhost:31480', {
	json: {
		img: [r, g, b]
	}
}, (err, res, body) => {
	if (err){
		console.log(err);
		return;
	}
});
