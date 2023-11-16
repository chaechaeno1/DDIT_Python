const mysql      = require('sync-mysql'); //import 역할

const connection = new mysql({
  host     : 'localhost',
  user     : 'root',
  password : 'python',
  database : 'python',
  port : 3305 //기본 포트가 3306이므로 포트 지정도 해주어야 한다.
});

var result = connection.query('select * from emp');
console.log(result);
console.log("첫번째 row의 e_id : " + result[0].e_id);

connection.dispose(); // 닫아주는 것