
//flask,django의 라이브러리와 같은...



const express = require('express')
const app = express()
const port = 3000


var bodyParser = require('body-parser');	// 모듈 import. Express v4.16.0이상은 생략 가능

app.use(bodyParser.json());	// json 등록
app.use(bodyParser.urlencoded({ extended : false }));

//ejs 추가
app.set('view engine', 'ejs');
app.set('views', './views');
/*app.set('view engine', 'pug');*/



app.get('/', (req, res) => {
  res.send('Hello EXPRESS!')
})

app.get('/param', (req, res) => {
  var menu = req.query.menu
  res.send('PARAM:' + menu)
})

app.post('/post', (req, res) => {
	const menu = req.body.menu
	console.log(menu)
  	res.send('Post:'+menu)
})

app.get('/forw', (req, res) => {
	var a = "홍길동";
	var b = ['유관순','윤석열'];
	var c = [
		{e_id:'1', e_name:'1', gen:'1', addr:'1'},
		{e_id:'2', e_name:'2', gen:'2', addr:'2'}		
	];
	res.render('forw',{a:a,b:b,c:c});
  	
	
	//res.sendFile(__dirname +'/forw.html') -> 적절하지않은 방법
	//__dirname은 server.js의 경로를 불러오는 것
	//'/'는 최상단이라는 의미
})



//pug
/*app.get('/pug', (req, res) => {

	res.render('pug');
  	
})*/




app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})