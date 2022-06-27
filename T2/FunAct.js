function validar() {
//    let error = "Fallo en: \n"

//     //region
//     let region = document.getElementsByName("region")[0].value;
//     if (region == 'Selecciona una región'){
//         error += " Región \n";
//     }

//     //comuna
//     let comuna = document.getElementsByName("comuna")[0].value;
//     if (comuna == 'Selecciona una comuna' ){
//         error += " Comuna \n";
//     }

//     //SECTOR
//     let sector = document.getElementsByName("sector")[0].value;
//     if (sector.length > 100 ){
//         error += " Sector \n"
//     }

//     //NOMBRE
//     let nombre = document.getElementById("nombre").value;
//     let largoNombre  =nombre.length;
//     if (largoNombre == 0 || largoNombre > 200 ){
//         error += " Nombre \n"
//     }

//     //EMAIL
//     let email = document.getElementById("email").value;
//     if( (/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(email) ) == false){
//        error += " Email \n" ;
//    }

//     //NUMERO CELULAR
//     let celular = document.getElementById("celular").value;
//     let expr = /\x2b569[0-9]+/;
//     if ((expr.test(celular) == false && celular.length !=0)|| celular.length > 12 ){
//         error += " Celular \n"; //acepta solo de tipo +569....
//     }

//     //CONTARCTAR POR
//     let box_contactos = document.getElementById("contactar-pors");
//     largo = document.getElementsByName("contactar-por").length; //numero de contactos
//     if (largo > 5){  //revisamos que no sean mas de 5
//         error += " Cantidad de Formas de Contactar \n ";
//     }

//     //revisar largo inputs contactar min 4 max 50
//     let aquierror = false;
//     for (let i = 0; i < largo ; i++) {
//         let contacto = box_contactos.getElementsByTagName('input')[i].value;
//         if ( contacto.length > 50 || contacto.length < 4     )
//             aquierror=true;
//     }
//     if (aquierror == true && largo > 1 ){
//         error += " Largos de los Contactos \n"
//     }
//     //NO PUSE REGES PAR AESTO PORQUE UNO PUEDE PONER CUALQUIER COSA EN UN ID DE USUARIO , PUEDE PONER NUMEROS, TECLAS ESPECIALES (/()$#"!)



//     //DÍA HORA INICIO
//     let inicio = document.getElementsByName("dia-hora-inicio")[0].value;
//     let hora_i = inicio.substring(inicio.lastIndexOf(' ')+1,inicio.length);
//     let fecha_i = inicio.substring(0,inicio.lastIndexOf(' '));

//     let pat_fecha = /^([0-9]{4}|[0-9]{2})-([0]?[1-9]|[1][0-2])-([0]?[1-9]|[1|2][0-9]|[3][0|1])$/;
//     let pat_hora = /^(0[0-9]|1[0-9]|2[0-3]|[0-9]):[0-5][0-9]$/;

//     if (!pat_hora.test(hora_i) || !pat_fecha.test(fecha_i) ){
//         error += " Fecha Inicio \n";
//     }

//     //DIA Y HORA DE TERMINO
//     let termino = document.getElementsByName("dia-hora-termino")[0].value;
//     let hora_t = termino.substring(inicio.lastIndexOf(' ')+1,inicio.length);
//     let fecha_t = termino.substring(0,inicio.lastIndexOf(' '));
//     if (!pat_hora.test(hora_t) || !pat_fecha.test(fecha_t) ){
//         error += " Fecha Termino \n";
//     }

//     //TEMA
//     let listaSelect = document.getElementsByName("tema");
//     let larloSelect = listaSelect.length;
//     let estabien1 = false;
//     //ver que hay como minimo una eleccion
//     for (let i=0;i<larloSelect ;i++){
//         if (listaSelect[i].value != "Selecciona un tipo de comida" ){
//             estabien1= true;
//         }
//     }
//     //si esque hay un select con opcion otro que se cumplan min3 max15
//     let inputsOtro = document.getElementById("box-tema").getElementsByTagName('input');
//     let largo2 = inputsOtro.length;
//     let bien = true;
//     for (let i=0; i<largo2 ;i++){
//         if (inputsOtro[i].className == "activo"){
//             let temita = inputsOtro[i].value;
//             if (temita.length < 3 || temita.length > 15){
//                 bien=false;
//             }
//         }
//     }

//     if (!bien || !estabien1){
//         error += " tema \n "
//     }

    //FOTO
//    let box_fotos = document.getElementById("box-foto");
//    files = box_fotos.getElementsByTagName('input') ;
//    let num_files = 0;
//    for (let i = 0; i < files.length; i++) {
//        if (files[i].value != ""){
//            num_files = num_files + 1;
//        }
//    }
//    if (num_files == 0 || files.length > 5) {
//        error += " Cantidad Archivos \n ";
//    }ti


    //if (error.length > 15) {
    //    console.log(error)
    //    document.getElementById("box-confirmacion").innerHTML =
    //       '<p>'+ error+' </p>'+
    //       ' <button type="button" onclick="noEnviarFormulario() ">Volver al Formulario</button>'
    //    return false;
    //}
    if(false){
        
    }
    else {
        document.getElementById("box-confirmacion").style.display = "none";
        return true;
    }


}
function seguro() {
    document.getElementById("box-confirmacion").style.display = "block";
}
function noEnviarFormulario() {
    document.getElementById("box-confirmacion").innerHTML=
        "<p >¿Está seguro que desea agregar este evento?</p> " +
        "<input id='botonFormulario' type='submit'value='Sí, estoy seguro'>" +
        "<button type='button' onclick='noEnviarFormulario()'>No,no estoy seguro, quiero volver al formulario</button>"
    document.getElementById("box-confirmacion").style.display = "none";

}
let chile = {
"regiones": [
    {
        "nombre": "Región Arica y Parinacota",
        "comunas": ["Arica", "Camarones", "Putre", "General Lagos"]
    },
    {
        "nombre": "Región de Tarapacá",
        "comunas": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]
    },
    {
        "nombre": "Región de Antofagasta",
        "comunas": ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro Atacama", "Tocopilla", "María Elena"]
    },
    {
        "nombre": "Región de Atacama",
        "comunas": ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"]
    },
    {
        "nombre": "Región de Coquimbo",
        "comunas": ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]
    },
    {
        "nombre": "Región de Valparaíso",
        "comunas": ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"]
    },
    {
        "nombre": "Región del Libertador Bernardo Ohiggins",
        "comunas": ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]
    },
    {
        "nombre": "Región del Maule",
        "comunas": ["Talca", "Constítución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "Retíro", "San Javier", "Villa Alegre", "Yerbas Buenas"]
    },
    {
        "nombre": "Región del Biobío",
        "comunas": ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío", "Quillón", "Ránquil", "San Nicolás", "Treguaco"]
    },
    {
        "nombre": "Región de La Araucanía",
        "comunas": ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria", ]
    },
    {
        "nombre": "Región de Los Ríos",
        "comunas": ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"]
    },
    {
        "nombre": "Región de Los Lagos",
        "comunas": ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutíllar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"]
    },
    {
        "nombre": "Región Aisén del General Carlos Ibáñez del Campo",
        "comunas": ["Coihaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O’Higgins", "Tortel", "Chile Chico", "Río Ibáñez"]
    },
    {
        "nombre": "Región de Magallanes y la Antártica Chilena",
        "comunas": ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "Antártíca", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
    },
    {
        "nombre": "Región Metropolitana de Santiago",
        "comunas": ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltíl", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]
    },
    {
        "nombre": "Región del Ñuble",
        "comunas": ["Cobquecura","Ñiquen","San Fabian","San Carlos","Quirihue","Ninhue","Trehuaco","San Nicolas","Coihueco","Chillan","Portezuelo","Pinto","Coelemu","Bulnes","San Ignacio","Ranquil","Quillon","El Carmen","Pemuco","Yungay","Chillan Viejo"]
    }

    ]
};


function mostrar_regiones() {
    console.log("funcion mostrar_regiones()")
    let comuna_seleccionada = document.getElementsByName("region")[0];    //con esto obtengo al linea html

    for (let i =0 ; i< chile["regiones"].length; i++) {
        comuna_seleccionada.innerHTML += '<option >' + chile["regiones"][i]["nombre"] + '</option>';
    }
}
function encontrar_enarreglo(chilearr,mi_region) {
    for (let i = 0; i < chilearr["regiones"].length; i++) {
        let reg = chilearr["regiones"][i].nombre;

        if (reg == mi_region) {
            return  chilearr["regiones"][i]["comunas"];  //si lo encuentra retorna lal ista de comunas
        }
    }
}

function mostrar_comunas2() {
    let reg_select = document.getElementsByName("region")[0]; //linea html
    reg_select.addEventListener("change",agregar_las_comunas);
}

function agregar_las_comunas() {
    let comunas_op = document.getElementsByName("comuna")[0];
    let comunas = encontrar_enarreglo(chile,this.value);
    comunas_op.innerHTML = "<option disabled selected>Selecciona una comuna</option>";

    for (let i =0; i< comunas.length ; i++){
        comunas_op.innerHTML += "<option>"+ comunas[i] +"</option>";
    }
}

function aparece_input() {
    red = document.getElementById("contactar-pors");
    if (red.getElementsByTagName("select").length <= 5 ) {
        let input = '<select  name="contactar-por">\n' +
            '                    <option disabled selected>Selecciona una opción</option>\n' +
            '                    <option> twiter </option>\n' +
            '                    <option> Instagram </option>\n' +
            '                    <option> facebook </option>\n' +
            '                    <option> tiktok </option>\n' +
            '                    <option> otra </option>\n' +
            '                </select>\n' +
            '                <input type="text" name="contactar-por-link">' +
            '                <br>    ';
        red.insertAdjacentHTML("beforeend", input);
    }
}

function funcion_hora_hoy(){
    let hoy = new Date();
    let fecha_hoy = hoy.getFullYear()+'-'+ addZ(hoy.getMonth() + 1)+
        '-'+ addZ(hoy.getDate());
    let hora_hoy =  addZ(hoy.getHours())+':'+ addZ(hoy.getMinutes());
    let hora_hoy2 =  addZ(versisepaso(hoy.getHours() + 3))+':'+ addZ(hoy.getMinutes());
    document.getElementsByName("dia-hora-inicio")[0].value = fecha_hoy +' '+ hora_hoy;
    document.getElementsByName("dia-hora-termino")[0].value = fecha_hoy +' '+ hora_hoy2;
}
function addZ(n){return n<10? '0'+n:''+n;}
function versisepaso(horas) {
    if (horas >24){
        //lo tenemos que arreglar
        return  horas -24;
    }
    return  horas;
}

function agregar_files() {

    let files = document.getElementById("box-foto");
    if(files.getElementsByTagName("input").length < 5){
        let input = '<input type="file" name="foto-actividad"  ><br>';
        files.insertAdjacentHTML("beforeend", input);
    }
}
function agregar_tema(){
    let temas = document.getElementById("box-tema");
    let input = '<div>' +
        '<select name="tema"  onchange="tema_otro()">\n' +
        '                  <option disabled selected>Selecciona un tipo de comida</option>\n' +
        '                  <option >Música </option>\n' +
        '                  <option >Deporte </option>\n' +
        '                  <option >Ciencias </option>\n' +
        '                  <option >Religion </option>\n' +
        '                  <option >Política </option>\n' +
        '                  <option >Tecnología </option>\n' +
        '                  <option >Juegos </option>\n' +
        '                  <option >Baile </option>\n' +
        '                  <option >Comida </option>\n' +
        '                  <option >Otro </option>\n' +
        '                </select>'+
        '<input class="no_activo" type="text" name="input"  ><br>'+
        ' </div>';
        temas.insertAdjacentHTML("beforeend", input);
}

function agregar_contactar(){
    let contactar = document.getElementById("contactar-pors");
    if (document.getElementsByName("contactar-por").length < 5 ) {
        let input = '<div>'+
        '<select name="contactar-por" >'+
            '<option disabled selected>Seleccione Forma de contacto</option>'+
            '<option>twiter</option>'+
            '<option>Telegram</option>'+
            '<option>Instagram</option>'+
            '<option>facebook</option>'+
            '<option>tiktok</option>'+
            '<option>otra</option>'+
        '</select>'+
        '<input type="text" name="contactar-por-link">'+
    '</div>';
    contactar.insertAdjacentHTML("beforeend", input);
    }

}

function tema_otro(){
    //alert("entro")
    let tema = document.getElementsByName("tema")[0];
    
    //alert(lista)
    ///alert(largolista)

    if (tema.value == "Otro"){
        console.log("aqui")
        let input =tema.nextElementSibling;
        input.className = "activo"
    }
    else{
        console.log("desactivamos la cuentios")
        let input =tema.nextElementSibling;
        input.className = "no_activo"

        }
    
   // let largo = document.getElementsByName("tema").length;
   // let tema = document.getElementsByName("tema")[largo-1].value;
   // let boxt = document.getElementById("box-tema");
   // console.log(tema)
  //  if (tema == 'Otro'){
  //      let input = '<input type="text" name="foto"  ><br>';
  //      boxt.insertAdjacentHTML("beforeend", input);
   // }
}

function redirigir(j) {

    nombreid =  "light_box"+j;
    box = document.getElementById(nombreid);
    document.getElementById("ListaSinDetalles").className = "rectangulo_contenido no_activo";
    document.getElementById(nombreid).className = nombreid + " activo";
}

//function ver_imagen(num){
    //document.getElementsByClassName("imagen")[num-1].width = 800;
    //document.getElementsByClassName("imagen")[num-1].height = 600;

//    document.getElementById("cajita-5").className= "activo caja_form"
//}

function ver_imagen(pathfoto, num){
      console.log(pathfoto);

    document.getElementsByClassName("en-grande")[num-1].style.display = "block";
    document.getElementsByClassName("en-grande")[num-1].innerHTML =
   `<img class="centrar" src=${pathfoto} width="800" height="600"></img>
    <br>
    <button onclick="desaparecer(${num})"> Cerrar </button>`;
}
function desaparecer(num) {
 document.getElementsByClassName("en-grande")[num-1].style.display = "none";
}

