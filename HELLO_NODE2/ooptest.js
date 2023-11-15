//node.js class export 검색


//const Animal = require('./Animal'); //import와 비슷한 기능
//const Animal = require('./animal.js'); //import와 비슷한 기능

const Human = require('./Human');

	var hum = new Human();
	console.log(hum.full);
	console.log(hum.flag_tool);
	hum.eat(9);
	hum.momstouch();
	console.log(hum.full);
	console.log(hum.flag_tool);
