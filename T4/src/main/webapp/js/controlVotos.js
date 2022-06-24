//comentario_foto
//id	fecha	comentario	nota	foto_actividad

$("#votacion").ready(function (){
    let queryString = window.location.search;
    let urlParams = new URLSearchParams(queryString);
    let idFoto = urlParams.get('id')
    console.log("id Foto -> ",idFoto);
    mostrarVotos(idFoto);
})

function mostrarVotos(id){
    $.get("vote_handler",{
        id:id
    },function (data){
        console.log("ffffddd");

    })
}
