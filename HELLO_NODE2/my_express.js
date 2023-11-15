
//flask,django의 라이브러리와 같은...



const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello EXPRESS!')
})

app.get('/param', (req, res) => {
  var menu = req.query.menu
  res.send('PARAM:' + menu)
})

app.get('/post', (req, res) => {
  res.send('Post:')
})


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})