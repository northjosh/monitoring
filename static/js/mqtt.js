
const url = ''

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
      // Publish a message to a topic
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



