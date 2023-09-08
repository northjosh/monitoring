
const url = 'wss://broker.hivemq.com:8884/mqtt'
// const url = 'ws://192.168.11.2'

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
  client.subscribe('jujutsu/motion', function (err) {
    if (!err) {
      console.log("Subscribed")
    }
  })
})

// Receive messages
client.on('message', function (topic, message) {
  // message is Buffer

  split = message.toString().split("::")

  // console.log(split[0]);
  // console.log(split[1]);

// Assuming you have a reference to the parent element with class "list"
  const parentElement = document.createElement('div');
  parentElement.className = 'list'

  const notificationElement = document.createElement('div');
  notificationElement.className = 'notification';

  const messageElement = document.createElement('div');
  messageElement.className = 'message';
  messageElement.textContent = split[1]; // Set the content dynamically

  const dateElement = document.createElement('div');
  dateElement.className = 'date';
  dateElement.textContent = split[0]; // Set the content dynamically

  parentElement.appendChild(notificationElement);
  parentElement.appendChild(messageElement);
  parentElement.appendChild(dateElement);

  logs_container.prepend(parentElement)
        
  console.log(message.toString())

//   client.end()
})