var Mysql = require('sync-mysql');

class DaoEmp {
	
  	constructor() {
		this.conn = new Mysql({
		  host     : 'localhost', 	//db접속 주소
		  user     : 'root', 		//db접속id
		  password : 'python', 		//db접속pw
		  port	   : '3305',		//port번호
		  database : 'python' 		//db명
		});	
  	}

	selectList(){
		var sql = "SELECT * FROM emp";
		return this.conn.query(sql);
	}
	
	selectOne(e_id){
		var sql = `SELECT * FROM emp WHERE e_id = ${e_id}`;
		return this.conn.query(sql)[0];
	}
	
	insert(e_id, e_name, gen, addr){
		var sql = `insert into emp
						(e_id, e_name, gen, addr) 
					values
						('${e_id}','${e_name}','${gen}','${addr}')`;
		return this.conn.query(sql).affectedRows;
	}
	
	update(e_id, e_name, gen, addr){
		var sql = `UPDATE emp 
					SET 
						e_name = '${e_name}',
						gen = '${gen}',
						addr = '${addr}'
					WHERE 
						e_id='${e_id}'`;
		return this.conn.query(sql).affectedRows;
	}
	
	delete(e_id){
		var sql = `DELETE FROM emp 
					WHERE e_id='${e_id}'`;
		return this.conn.query(sql).affectedRows;
	}
}

module.exports = DaoEmp;

if(require.main === module){
	var de = new DaoEmp();
	//var cnt = de.delete("7");
	var list = de.selectList();
	//console.log("cnt",cnt);
	console.log("list",list);
}