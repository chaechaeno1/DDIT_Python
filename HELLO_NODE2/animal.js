class Animal{

  constructor() {
    this.full = 1;
  }

  eat(amount) {
    this.full += amount;
  }

}


module.exports = Animal;