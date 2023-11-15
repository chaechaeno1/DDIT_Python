const mysql      = require('sync-mysql'); //import 역할

const connection = new mysql({
  host     : 'localhost',
  user     : 'root',
  password : 'python',
  database : 'python',
  port : 3305 //기본 포트가 3306이므로 포트 지정도 해주어야 한다.
});

var e_id = '3';
var e_name = '7';
var gen = '7';
var addr = '7';

var sql =`update emp set e_name = ${e_name}, gen = ${gen} where e_id = ${e_id}`;

var result = connection.query(sql);
console.log(result);

connection.dispose(); // 닫아주는 것