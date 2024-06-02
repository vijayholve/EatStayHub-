let send_value=document.querySelector(".send_value")
let v200=document.querySelector(".v200")
let v400=document.querySelector(".v400")
let v600=document.querySelector(".v600")
let v800=document.querySelector(".v800")
let v1000=document.querySelector(".v1000")
var URL="{% url 'projects:Unread' %}"
v200.addEventListener('click', function(){
    
    var data = {'count': v200, 'X-csrfmiddlewaretoken': csrfmiddlewaretoken};
    $.post(URL, data);
})
v400.addEventListener('click', function(){
    // let a=v400.value
    send_value.innerHTML=v400.value
})
v600.addEventListener('click', function(){
    let a=v600.value
    send_value.innerHTML=v600.value
})
v800.addEventListener('click', function(){
    let a=v800.value
    send_value.innerHTML=a
})
v1000.addEventListener('click', function(){
    let  a=v1000.value
    send_value.innerHTML=a
})