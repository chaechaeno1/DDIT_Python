const mysql      = require('mysql'); //import 역할
const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'python',
  database : 'python',
  port : 3305 //기본 포트가 3306이므로 포트 지정도 해주어야 한다.
});


connection.connect(function(err) {
  console.log("start");
  var sql = "update emp set e_name = '2', gen = '3' where e_id = '1' ";
  connection.query(sql, function (err, result) {
    console.log("1 record updated");
	console.log(result.affectedRows);
  });
});

 console.log("end");