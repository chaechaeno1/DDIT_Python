
//flask,django의 라이브러리와 같은...



const express = require('express')
const app = express()
const port = 3000


var bodyParser = require('body-parser');	// 모듈 import. Express v4.16.0이상은 생략 가능

app.use(bodyParser.json());	// json 등록
app.use(bodyParser.urlencoded({ extended : false }));



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
  res.send('forw');
})




app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})