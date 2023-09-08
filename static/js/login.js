const msg =  document.getElementById('alert')
const alertMsg = document.getElementById('alert-msg')


if( alertMsg.innerHTML != ''){
    msg.style.visibility = 'visible'
}

console.log(msg.innerHTML);