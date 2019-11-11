const magic_home = require('magic-home');
const express = require('express');
const bodyParser = require('body-parser');

const PORT = 31480;
const app = express();

app.listen(PORT, () => {
	console.log(`Server is listening on port: ${PORT}`)
});
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/', (req, res) => {
	const img = req.body.RGBcolor;
	console.log(img);
	res.end('received');
});
