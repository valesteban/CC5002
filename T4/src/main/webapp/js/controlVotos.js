//comentario_foto
//id	fecha	comentario	nota	foto_actividad

$("#votacion").ready(function (){
    let queryString = window.location.search;
    let urlParams = new URLSearchParams(queryString);
    let idFoto = urlParams.get('id')

    mostrarVotosCometarios(idFoto);

})


function mostrarVotosCometarios(id){
    //console.log("id Foto -> ",id);
    //console.log("id Foto -> ",id);
    $.get("vote_handler",{
        id:id
    },function (data){
        let suma  = 0;
        let total = 0;
        let response = JSON.parse(data);
        //console.log(response);
        //console.log(response["comentarios"]);

        $.each(response["notas"],function (i) {
            suma += response["notas"][i];
            total = 1 +parseInt(i);
        })
        $('ul li').remove();
        $.each(response["comentarios"],function (i) {
            $(".listaC").append("<li>"+response['comentarios'][i]+"</li>");
           // console.log(response["comentarios"][i]);

        })
        //console.log("suma-> ",suma);
        //console.log("total-> ",total);
        let actual = (suma/total).toFixed(2);
        $(".notaActual").html("Nota Actual: "+ actual)


      }).fail(function (a,b,c){console.log(a,b,c)})
}

$("#votacion").submit(function (event){
    event.preventDefault();
    let queryString = window.location.search;
    let urlParams = new URLSearchParams(queryString);
    let idFoto = urlParams.get('id')

    let nota = $("#nota").find(":selected").text();
    let comentario =  $("#comentario-foto").val();

    //obtener fechaactual YYYY-MM-DD HH:MI:SS
    let hoy = new Date();
    let fecha = hoy.getUTCFullYear() +"-"+ (hoy.getUTCMonth()+1) +"-"+ hoy.getUTCDate() + " " + hoy.getUTCHours() + ":" + hoy.getUTCMinutes() + ":" + hoy.getUTCSeconds();

   // console.log(nota);
   // console.log(comentario);
    $.post("vote_handler",{
            idFoto :idFoto,
            notaFoto: nota,
            comentarioFoto: comentario,
            fechaCometarioNota: fecha
        },
        function (data){
            console.log("Guardado exitoso");

            mostrarVotosCometarios(idFoto);

        }
    ).fail(function (a,b,c){console.log(a,b,c)})
})
