const datePicker = document.getElementById('pickers')

const date = new Date()
const current = `${date.getFullYear()}-0${date.getMonth() + 1}-0${date.getDay()}`

datePicker.value = current 
datePicker.max = current


// datePicker.addEventListener('change', (e) =>{
//     console.log(e.srcElement.value);

// })


// console.log(current)





