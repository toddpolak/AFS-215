const http = require('http')

const reqListener = (req, res) => {
    res.writeHead(200)
    res.end('Node JS Server')
}

// Test Server

const server = http.createServer(reqListener)
server.listen(3000, () => {
    console.log('The server is listening on port 3000 ..')
})