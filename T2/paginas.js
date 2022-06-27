function anteriorBoton(){
    //console.log("anterior")
    div = document.getElementsByClassName("activo")[0];
    id_prev = parseInt(div.id) - 1 ;
    if(0 <= id_prev){
        div.className ="rectangulo_contenido  no_activo" ;
        document.getElementById(id_prev).className="rectangulo_contenido activo" ;
    }


}

function siguienteBoton(fin){
    //console.log("siguiente")

    div = document.getElementsByClassName("activo")[0] ;
    siguiente = div.nextElementSibling;


    id_prox = parseInt(div.id) + 1 ;
    if(fin >= id_prox){
        //console.log(id_prox);
        div.className ="rectangulo_contenido  no_activo" ;
        siguiente.className = "rectangulo_contenido activo" ;

    }
}

function redirigirPag(num){
    //num me devuelve el numero en la lista de toodos los elementos que tengo
    //console.log("redirigir");
    window.location.href = "informacionActividad.py"+'?id='+num;
    // Simulate a mouse click:
    //window.location.href = "http://www.w3schools.com";

    // Simulate an HTTP redirect:
    //window.location.replace("http://www.w3schools.com");
}


function obtenerValorURL(){
    const queryString = window.location.search;  // ?id=2
    //console.log(queryString);


    //const urlParams = new URLSearchParams(queryString);
    //urlParams.get('id')
}


function ver_imagen(pathfoto){
    //console.log(pathfoto);
  
    document.getElementsByClassName("en-grande")[0].style.display = "block";
    document.getElementsByClassName("en-grande")[0].innerHTML =
    `<img class="centrar" src="../imagenes/${pathfoto}" width="800" height="600"></img>
      <br>
      <button onclick="desaparecer()"> Cerrar </button>`;
  }

function desaparecer(num) {
   document.getElementsByClassName("en-grande")[0].style.display = "none";
}

