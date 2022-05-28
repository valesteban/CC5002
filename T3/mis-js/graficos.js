//GRAFICO 1
// el primero es un gráfico de líneas que informa la cantidad de actividades
//por día. En el eje X muestra los días y en el eje Y muestra la cantidad de actividades. 
document.addEventListener('DOMContentLoaded', function () {
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
            
            data: [1, 0, 42,43,6,33,87]
        }],
    });
});

//GRAFICO 2
//El segundo gráfico es un gráfico de torta que muestra el total de actividades por tipo
document.addEventListener('DOMContentLoaded', function () {
    let chart = Highcharts.chart("contenido-grafico-2", {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Cantidad de Actividades por Tipo'
        },
        xAxis: {
            categories: ['tipo1', 'tipo2', 'tipo3','tipo4','tipo5']
        },
        series: [{
            
            data: [22,55,3,20,0]
        }],
    });
});

//GRAFICO 3
//El tercer gráfico es uno de barras que muestra tres barras por cada punto del eje X. El eje X son los
//meses y para cada mes muestra una barra con la cantidad de actividades que se inician en la
//mañana (antes de las 11:00), la cantidad de actividades que se inician al mediodía (entre las
//11:00 y 14:59) y la cantidad de actividades que se inician en la tarde (desde las 15:00) . El eje Y
//indica la cantidad.

document.addEventListener('DOMContentLoaded', function () {
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
            data: [12,11,45,22,22,1, 0, 4,55,65,34,12,3]
        }, {
            name: 'Mediodía',
            data: [12,11,45,22,22,1, 0, 4,55,65,34,12,3]
        },{
            name:'Tarde',
            data:[12,11,45,22,22,1, 0, 4,55,65,34,12,3]
        }]
    });
});