//obtiene una cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
// Agarra los elementos html boton 'agregar al carrito'
var favoritos = document.getElementsByClassName('btn-outline-danger')

// recorre el array favoritos y actua al evento click del boton
for (var i = 0; i < favoritos.length; i++) {
    // Funcion al hacer click
    favoritos[i].addEventListener('click', function()  {
        alert('agregado a favoritos')
        // agarra el valor de los dataset
        var inmuebleId = this.dataset.inmueble;
        console.log(inmuebleId)

        enviarDatos(inmuebleId);

    })
}



function enviarDatos(inmuebleId){

    var url = 'http://127.0.0.1:8000/favoritos'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'id': inmuebleId})
    })
    .then((response) =>{
        return response.json()
    })
}
// crea un uuid para nuestro dispositivo
function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
    });
}

let device = getCookie('device')

if (device == null || device == undefined){
    device = uuidv4()
}

document.cookie ='device=' + device + ";domain=;path=/"
