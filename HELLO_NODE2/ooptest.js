//node.js class export 검색


const Animal = require('./Animal'); //import와 비슷한 기능

var ani = new Animal();
console.log(ani.full);
ani.eat(9);
console.log(ani.full);

