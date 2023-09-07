// const msg =  document.getElementById('alert')
const datePicker = document.getElementById('picker')

const date = new Date()
const current = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDay()}`

datePicker.value = current 
datePicker.max = current


datePicker.addEventListener('change', (e) =>{
    console.log(e.srcElement.value);

})





console.log(current)


// if( msg.innerHTML != ''){
//     msg.style.visibility = 'visible'
// }



