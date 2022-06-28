function redirigir(num) {
    //num me devuelve el numero en la lista de toodos los elementos que tengo
    //console.log("redirigir");
    window.location.href = "infoFoto.jsp"+'?id='+num;
}
$( document ).ready(function() {
    $("th").on("click", function(){

        let suClase = $(this).attr("class");
       /// alert(suClase);
        window.location.href = "infoFoto.jsp"+'?id='+ parseInt(suClase);
    });
});