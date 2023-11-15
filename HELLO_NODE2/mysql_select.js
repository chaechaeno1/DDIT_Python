const mysql      = require('mysql'); //import 역할
const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'python',
  database : 'python',
  port : 3305 //기본 포트가 3306이므로 포트 지정도 해주어야 한다.
});

connection.connect();

connection.query('SELECT * from emp', (error, rows, fields) => {
//  if (error) throw error;
  console.log(rows);
  //console.log(error);
  //console.log(fields);
});

connection.end();


