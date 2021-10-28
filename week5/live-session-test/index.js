import Express from "express"
import * as path from 'path'
import { fileURLToPath } from "url"

const app = Express()
const port = 9000
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

app.use(Express.static('live-session-test'))

app.listen(port, () => console.log(`Listening on Port ${port}`))

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, './test.html'))
})
