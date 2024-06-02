send_value=document.querySelector(".send_value")
v200=document.querySelector(".v200")
v400=document.querySelector(".v400")
v600=document.querySelector(".v600")
v800=document.querySelector(".v800")
v1000=document.querySelector(".v1000")
v200.addEventListener('click', function(){
		a=v200.value
      send_value.innerHTML=a
})
v400.addEventListener('click', function(){
    a=v400.value
    send_value.innerHTML=a
})
v600.addEventListener('click', function(){
    a=v600.value
    send_value.innerHTML=a
})
v800.addEventListener('click', function(){
    a=v800.value
    send_value.innerHTML=a
})
v1000.addEventListener('click', function(){
    a=v1000.value
    send_value.innerHTML=a
})