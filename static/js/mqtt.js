
const url = 'wss://rff11281.ala.us-east-1.emqxsl.com:8084/mqtt'

const logs_container = document.getElementById('logs_container')


const options = {
  // Clean session
  clean: true,
  connectTimeout: 4000,
  // Authentication
  clientId: 'jujutsu',
  username: 'jujutsu',
  password: 'jujutsu',
}

const client  = mqtt.connect(url, options)

client.on('connect', function () {
  console.log('Connected')
  /
  client.subscribe('motion', function (err) {
    if (!err) {
      console.log("Subscribed")
    }
  })
})

// Receive messages
client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
//   alert(message.toString())

//   client.end()
})



