class Animal{

  constructor() {
    this.full = 1;
  }

  eat(amount) {
    this.full += amount;
  }

}


module.exports = Animal; //Animal이름을 가진 객체를 내보낸다.


//https://smilejsu.tistory.com/2452

if (require.main === module) {
	var ani = new Animal();
	console.log("1",ani.full);
	ani.eat(9);
	console.log("1",ani.full);
}