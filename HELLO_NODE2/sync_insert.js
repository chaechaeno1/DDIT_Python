const mysql      = require('sync-mysql'); //import 역할

const connection = new mysql({
  host     : 'localhost',
  user     : 'root',
  password : 'python',
  database : 'python',
  port : 3305 //기본 포트가 3306이므로 포트 지정도 해주어야 한다.
});

var result = connection.query('INSERT INTO emp VALUES (4, 4, 4, 4)');
console.log(result);

connection.dispose(); // 닫아주는 것