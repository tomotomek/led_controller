const magic_home = require('magic-home');
const express = require('express');
const bodyParser = require('body-parser');
const FastAverageColor = require('fast-average-color');

const PORT = 31480;
const app = express();
const fac = new FastAverageColor();

app.listen(PORT, () => {
	console.log(`Server is listening on port: ${PORT}`)
});
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/', (req, res) => {
	const img = req.body.img;
	//const color = fac.getColor(img);

	console.log(img);
	res.end('received');
});
