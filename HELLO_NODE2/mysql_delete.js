const mysql      = require('mysql'); //import 역할
const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'python',
  database : 'python',
  port : 3305 //기본 포트가 3306이므로 포트 지정도 해주어야 한다.
});


connection.connect(function(err) {
  var sql = "DELETE FROM emp WHERE e_id = '4'";
  connection.query(sql, function (err, result) {
    console.log("1 record deleted");
	console.log("Number of records deleted: " + result.affectedRows);
  });
});



