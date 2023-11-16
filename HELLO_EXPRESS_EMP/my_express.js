const express = require('express');
const DaoEmp = require('./daoemp.js');

const app = express();
const port = 3000;

const bodyParser = require('body-parser');	// 모듈 import. Express v4.16.0이상은 생략 가능

app.use(bodyParser.json());	// json 등록
app.use(bodyParser.urlencoded({ extended : false }));	// URL-encoded 등록

//app.set('view engine', 'pug');
app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/', (req, res) => {
	var de = new DaoEmp();
	let list = de.selectList();
	res.render('emp_list',{list:list});
})

app.get('/emp_list', (req, res) => {
	var de = new DaoEmp();
	let list = de.selectList();
	res.render('emp_list',{list:list});
})

app.get('/emp_detail', (req, res) => {
	var de = new DaoEmp();
	var e_id = req.query.e_id;
	let vo = de.selectOne(e_id);
	res.render('emp_detail',{vo:vo});
})

app.get('/emp_add', (req, res) => {
	res.render('emp_add');
})

app.post('/emp_add_act', (req, res) => {
	var de = new DaoEmp();
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var gen = req.body.gen;
	var addr = req.body.addr;
	let cnt = de.insert(e_id,e_name,gen,addr);
	res.render('emp_add_act',{cnt:cnt});
})

app.get('/emp_mod', (req, res) => {
	var e_id = req.query.e_id;
	var e_name = req.query.e_name;
	var gen = req.query.gen;
	var addr = req.query.addr;
	res.render('emp_mod',{e_id:e_id,e_name:e_name,gen:gen,addr:addr});
})

app.post('/emp_mod_act', (req, res) => {
	var de = new DaoEmp();
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var gen = req.body.gen;
	var addr = req.body.addr;
	let cnt = de.update(e_id,e_name,gen,addr);
	res.render('emp_mod_act',{cnt:cnt});
})

app.get('/emp_del_act', (req, res) => {
	var de = new DaoEmp();
	var e_id = req.query.e_id;
	let cnt = de.delete(e_id);
	res.render('emp_del_act',{cnt:cnt});
})

app.listen(port, () => {
 	console.log(`Example app listening on port ${port}`);
})


