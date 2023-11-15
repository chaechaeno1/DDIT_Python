
const Animal = require('./Animal');

class Human extends Animal{
	
	constructor() {
		super();
		this.flag_tool = false;
	}
	
		momstouch() {
			this.flag_tool = true;
	}
	
}

module.exports = Human;

if (require.main === module) {
	var hum = new Human();
	console.log(hum.full);
	console.log(hum.flag_tool);
	hum.eat(9);
	hum.momstouch();
	console.log(hum.full);
	console.log(hum.flag_tool);
}
