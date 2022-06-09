//OBTENER INFO POR MEDIO DE AJAX

var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function(){
    if (xhr.readyState===4 && xhr.status===200) {
        let response = JSON.parse(xhr.responseText);
        console.log(response);

        Grafico1(response["grafico1"])
       // console.log(response["grafico2"])
        Grafico2(response["grafico2"])
      //  console.log(response["grafico3"])
        Grafico3(response["grafico3"])


        

    }
}

document.addEventListener('DOMContentLoaded', function(){
    xhr.open("GET", '../cgi-bin/infoGraficos.py');
    xhr.send();
})


//GRAFICO 1
// el primero es un gráfico de líneas que informa la cantidad de actividades
//por día. En el eje X muestra los días y en el eje Y muestra la cantidad de actividades. 
function Grafico1(info){
    //console.log(info) //lista que s eagrega en el grafico 1
    let chart = Highcharts.chart("contenido-grafico-1", {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Cantidad de Actividades por Día'
        },
        xAxis: {
            categories: ['Lunes', 'Martes', 'Miercoles',"Jueves","Viernes","Sabado","Domingo"]
        },
        series: [{
            
            data: info
        }],
    });

}

//GRAFICO 2
//El segundo gráfico es un gráfico de torta que muestra el total de actividades por tipo
function Grafico2(info){
    let data = [] ;
    let i=0
    let valores = Object.keys(info).map(function(key){
        return info[key];
    });
    for ( x in info) {
        tupla = [x,valores[i]]
        data.push(tupla)
        i+=1
    }



    console.log(valores)
    let chart = Highcharts.chart("contenido-grafico-2", {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Cantidad de Actividades por Tipo'
        },
        xAxis: {
            categories:['tipo1', 'tipo2', 'tipo3','tipo4','tipo5','tipo5','tipo5']
        },
        series: [{
            
            data:data//[1, 1, 1,1 , 1, 1,1, 2, 1,1, 89] //[22,55,3,20,0]
        }],
    });

}

//GRAFICO 3
//El tercer gráfico es uno de barras que muestra tres barras por cada punto del eje X. El eje X son los
//meses y para cada mes muestra una barra con la cantidad de actividades que se inician en la
//mañana (antes de las 11:00), la cantidad de actividades que se inician al mediodía (entre las
//11:00 y 14:59) y la cantidad de actividades que se inician en la tarde (desde las 15:00) . El eje Y
//indica la cantidad.
function Grafico3(info){
    var mañana = Object.keys(info).map(function(key){
        return info[key][0];
    });
    var mediodia = Object.keys(info).map(function(key){
        return info[key][1];
    });
    var tarde = Object.keys(info).map(function(key){
        return info[key][2];
    });
    
    const chart = Highcharts.chart("contenido-grafico-3", {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Actividades por mes '
        },
        xAxis: {
            categories: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        },
        yAxis: {
            title: {
                text: 'Cantidad Actividades'
            }
        },
        series: [{
            name: 'Mañana',
            data: mañana
        }, {
            name: 'Mediodía',
            data: mediodia
        },{
            name:'Tarde',
            data:tarde
        }]
    });

}

