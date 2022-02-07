function temp(ta) {
    $('#temp').highcharts({
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false
        },
        title: {
            text: 'Temperatura',
            x: 0,
            y: 30
        },
        pane: {
            startAngle: -140,
            endAngle: 140,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },

        // the value axis
        yAxis: {
            min: 0,
            max: 40,
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',

            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ta+" °C",
                x: 0,
                y: 60,
                floating: true
            },
            plotBands: [{
                from: 0,
                to: 20,
                color: '#0099ff' // blue
            }, {
                from: 20,
                to: 30,
                color: '#DDDF0D' // yellow
            }, {
                from: 30,
                to: 40,
                color: '#DF5353' // red
            }]
        },
        credits: { enabled: false },
        exporting: { enabled: false },
        series: [{
            name: 'Temperatura',
            data: [ta],
            dataLabels:{
                enabled: false
            },
            tooltip: {
                valueSuffix: ' °C'
            }
        }]


    });
}

function humedad(hr) {
    $('#humedad').highcharts({

        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false
        },

        title: {
            text: 'Humedad Relativa',
            x: 0,
            y: 30
        },

        pane: {
            startAngle: -160,
            endAngle: 160,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },

        // the value axis
        yAxis: {
            min: 0,
            max: 100,
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',

            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: hr+"%",
                x: 0,
                y: 60,
                floating: true
            },
            plotBands: [{
                from: 0,
                to: 40,
                color: '#cccc00' // blue
            }, {
                from: 40,
                to: 70,
                color: '#99ff99' // yellow
            }, {
                from: 70,
                to: 100,
                color: '#00cc33' // red
            }]
        },
        credits: { enabled: false },
        exporting: { enabled: false },
        series: [{
            name: 'Humedad Relativa',
            data: [hr],
            dataLabels:{
                enabled: false
            },
            tooltip: {
                valueSuffix: ' %'
            }
        }]


    });
}

function presion(pr) {
    $('#presion').highcharts({
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false
        },
        title: {
            text: 'Presión',
            x: 0,
            y: 30
        },
        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 2,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
        // the value axis
        yAxis: {
            min: 960,
            max: 1024,

            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 5,
            minorTickPosition: 'inside',
            minorTickColor: '#666',

            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 8,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text:  Math.round(pr)+"hPa",
                dataLabels:{
                    enabled: false
                },
                x: 0,
                y: 60,
                floating: true
            }

        },
        credits: { enabled: false },
        exporting: { enabled: false },
        series: [{
            name: 'Presion',
            data: [pr],
            dataLabels:{
                enabled: false
            },
            tooltip: {
                valueSuffix: ' hPa'
            }
        }]

    });
}

function vientoR(vv,dv) {
    var chart = new Highcharts.Chart({
        chart: {
            renderTo: 'vientoR',
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false
        },

        title: {
            text: 'Viento',
            y: 25
        },

        pane: {
            startAngle: 0,
            endAngle: 360,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
        // the value axis
        yAxis: {
            min: 0,
            max: 360,
            tickPixelInterval: 15,
            tickWidth: 1,
            tickPosition: 'outside',
            tickLength: 6,
            tickColor: '#999',
            labels: {
                step: 3,
                rotation: 'auto'
            },
            title: {
                text: vv+"km/h",
                x: 0,
                y: 64
            },
            plotBands: [{
                label: {
                    text: '<b>E</b>',
                    x: 35,
                    y: 60,
                },
                from: 0,
                to: 90,
                color: '#55BF3B' // green
            }, {
                label: {
                    text: '<b>S</b>',
                    x: -54,
                    y: 33
                },
                from: 90,
                to: 180,
                color: '#DDDF0D' // yellow
            }, {
                label: {
                    text: '<b>O</b>',
                    x: 10,
                    y: -55
                },
                from: 180,
                to: 270,
                color: '#DF5353' // red
            },
            {
                label: {
                    text: '<b>N</b>',
                    x: 95,
                    y: -20
                },
                from: 270,
                to: 360,
                color: '#000000' // black
            }]
        },
        credits: { enabled: false },
        exporting: { enabled: false },
        series: [{
            name: 'Dirección del Viento',
            data: [dv],
            tooltip: {
                valueSuffix: '°'
            }
        }]

    });
}

function lluviaW(ri) {
    $('#lluviaW').highcharts({
        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false
        },
        title: {
            text: 'Intensidad lluvia \n',
            x: 0,
            y: 30
        },
        pane: {
            startAngle: -120,
            endAngle: 120,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 2,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },
        // the value axis
        yAxis: {
            min: 0,
            max: 30,
            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 3,
            minorTickPosition: 'inside',
            minorTickColor: '#666',
            tickPixelInterval: 30,
            tickWidth: 3,
            tickPosition: 'inside',
            tickLength: 13,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ri+"mm/h",
                x: 0,
                y: 60,
                floating: true
            },
            plotBands: [{
                from: 0,
                to: 30,
                color: '#0099ff' // blue
            }]


        },
        credits: { enabled: false },
        exporting: { enabled: false },
        series: [{
            name: 'Intensidad de la Lluvia',
            data:[ri],
            dataLabels:{
                enabled: false
            },
            tooltip: {
                valueSuffix: ' mm/h'
            }
        }]

    });
}

function lluvia48(rc) {
        let max = Math.round(rc.rc__sum) + 5;
        $('#lluvia24').highcharts({
            chart: {
                type: 'gauge',
                plotBackgroundColor: null,
                plotBackgroundImage: null,
                plotBorderWidth: 0,
                plotShadow: false
            }, 
            title: {
                text: 'Acumulado en 48h',
                x: 0,
                y: 30
            },
            pane: {
                startAngle: -120,
                endAngle: 120,
                background: [{
                    backgroundColor: {
                        linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                        stops: [
                            [0, '#FFF'],
                            [1, '#333']
                        ]
                    },
                    borderWidth: 0,
                    outerRadius: '109%'
                }, {
                    backgroundColor: {
                        linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                        stops: [
                            [0, '#333'],
                            [1, '#FFF']
                        ]
                    },
                    borderWidth: 2,
                    outerRadius: '107%'
                }, {
                    // default background
                }, {
                    backgroundColor: '#DDD',
                    borderWidth: 0,
                    outerRadius: '105%',
                    innerRadius: '103%'
                }]
            },     
            // the value axis
            yAxis: {
                min: 0,
                max: max,
                minorTickInterval: 'auto',
                minorTickWidth: 1,
                minorTickLength: 3,
                minorTickPosition: 'inside',
                minorTickColor: '#666',
                tickPixelInterval: 30,
                tickWidth: 3,
                tickPosition: 'inside',
                tickLength: 13,
                tickColor: '#666',
                labels: {
                    step: 2,
                    rotation: 'auto'
                },
                title: {
                    text: Math.round(rc.rc__sum*100)/100+"mm",
                    x: 0,
                    y: 60,
                floating: true
                },
                plotBands: [{
                    from: 0,
                    to: max,
                    color: '#0099ff' // blue
                }]
    
                
            },
                credits:{ enabled: false},
                exporting:{ enabled: false},
            series: [{
                name: 'Acumulado últimas 48 horas',
                data: [rc.rc__sum],
                dataLabels:{
                    enabled: false
                },
                tooltip: {
                    valueSuffix: ' mm'
                },                
            }]
        
        });
}

// Comportamiento ultimas 48 horas 
function comportamiento48h(hr,pr,ta,rc,fecha_final,fecha_inicial ){
    Highcharts.setOptions({
        lang: {
            shortMonths: ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
            weekdays: ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"],
            resetZoom: "Quitar Zoom"
        }
    });
    
    $('#48horas').highcharts({
        chart: {
            zoomType: 'x',
            alignTicks: false
        },
        title: {
            text: 'Comportamiento en las últimas 48 horas',
        },
        subtitle: {
            text: ''
        },
        xAxis: [{
            type: 'datetime',
            maxZoom: 0.5 * 3600 * 1000,
            min:fecha_inicial,
            max: fecha_final,
            // tickInterval: 48 * 3600 * 1000,
        }],
        yAxis: [
        { // Primary yAxis    
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[2]
                }
            },
            max: 40,
            min: 0,
                    
            title: {
                text: 'Temperatura (°C)',
                style: {
                    color: Highcharts.getOptions().colors[2]
                }
            },
            
        },
        { // Secondary yAxis      
            max: 110,
            min: 0,
            gridLineWidth: 0,
            title: {                
                text: 'Humedad Relativa (%)',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            },
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            },
            opposite: true
        },
        { // Tertiary yAxis       
            gridLineWidth: 0,
            title: {
                text: 'Presión (hPa)',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            opposite: true
            },
        { // Secondary yAxis
            max: 110,
            min: 0,
            gridLineWidth: 0,
            title: {                
                text: 'Lluvia (mm)',
                style: {
                    color: Highcharts.getOptions().colors[5]
                }
            },
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[5]
                }
            }
        }
    ],
        tooltip: {
            shared: true
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        credits: {
            enabled: true,
            text:"GOAC",
            href:"http://www.goac.cu",
            position:{
                x:-100,
                y:-25,
            },
            style:{
                fontSize:"12px",
            }
        },
        exporting: {
            enabled:true,
            buttons:{
                contextButton: {
                menuItems: ['downloadPNG',]
                },
            }
        },
        series: [{
            name: 'Humedad Relativa',
            type: 'spline',
            yAxis: 1,
            data: hr,
            pointInterval: 1 * 300 * 1000,
            marker: {
                enabled: false
            },
            tooltip: {
                valueSuffix: ' %'
            }

        }, {
            name: 'Presión',
            type: 'spline',
            yAxis: 2,
            data: pr,
            pointInterval: 1 * 300 * 1000,
            marker: {
                enabled: false
            },
            dashStyle: 'shortdot',
            tooltip: {
                valueSuffix: ' hPa'
            }

        }, {
            name: 'Temperatura',
            type: 'spline',
            data: ta,
            pointInterval: 1 * 300 * 1000,
            marker: {
                enabled: false
            },
            tooltip: {
                valueSuffix: ' °C'
            }
        }
    , {
            name: 'Lluvia',
            type: 'spline',
            yAxis: 3,
            data: rc,
            pointInterval: 1 * 300 * 1000,
            zIndex: -1,
            tooltip: {
                valueSuffix: ' mm'
            }
        }]
    });
}


function velocidad_direccion(vv, dv, fecha_inicial, fecha_final) { 
    Highcharts.setOptions({
       lang: {
           shortMonths: ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
           weekdays: ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"],
           resetZoom: "Quitar Zoom"
       }
    });
   $('#viento').highcharts({
       chart: {
           zoomType: 'x',
           alignTicks: false
       },
       title: {
           text: 'Comportamiento del viento en las últimas 48 horas',
           
       },
       subtitle: {
           text: ''
       },
       exporting: {
            enabled:true,
            buttons:{
                contextButton: {
                menuItems: ['downloadPNG',]
                },
            }
        },
       xAxis: [{
            type: 'datetime',
            maxZoom: 0.5 * 3600 * 1000,
            min:fecha_final,
            max: fecha_inicial,
       }],
       yAxis: [{ // Primary yAxis
                max: 360,
                min: 0,
                tickLength: 20,
                tickInterval: 90,
                gridLineWidth: 1,
           labels: {
               format: '{value}°',
               style: {
                   color: Highcharts.getOptions().colors[1]
               }
           },
           title: {
               text: 'Dirección',
               style: {
                   color: Highcharts.getOptions().colors[1]
               }
              
           }
       }, { // Secondary yAxis
            min: 0,
            gridLineWidth: 0,
             
           title: {
               text: 'Velocidad (km/h)',
               style: {
                   color: Highcharts.getOptions().colors[0]
               }
           },
           labels: {
               format: '{value}',
               style: {
                   color: Highcharts.getOptions().colors[0]
               }
           },
            opposite: true
       }],
       tooltip: {
           shared: true
       },
       legend: {
          layout: 'horizontal',
       align: 'center',
    //    x: 0,
       verticalAlign: 'bottom',
    //    y: 20,
    //    floating: true,
       backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
       },       
       credits: {
            enabled: true,
            text:"GOAC",
            href:"http://www.goac.cu",
            position:{
                x:-100,
                y:-20,
            },
            style:{
                fontSize:"12px",
            }
        },
       series: [
        {
           name: 'Velocidad',
           type: 'column',
           yAxis: 1,
           zIndex: -1,
           data: vv,
           pointInterval: 1 * 300 * 1000,
           tooltip: {
               valueSuffix: ' km/h'
           }

       }, {
           name: 'Dirección',
           type: 'line',
           data: dv,
           marker: {
            enabled: false
             },
           pointInterval: 1 * 300 * 1000,
           
           tooltip: {
               valueSuffix: '°'
           }
       }]
   });
}

function call_ajax(){
    $.ajax({
        url : window.location.pathname,
        type: 'POST',
        data: {
            'accion': 'get_data',
        },
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            const gauge = data.gauge;
            const gauge_mm_acomulado = data.mm_acomulado;
            const grafica_48 = data.acomulado48;
            const vel_dir_48 = data.acomulado48;
            temp(gauge.ta);
            presion(gauge.pr);
            humedad(gauge.hr);
            vientoR(gauge.vv,gauge.dv);
            lluviaW(gauge.ri);
            lluvia48(gauge_mm_acomulado);
            comportamiento48h(grafica_48.hr,grafica_48.pr,grafica_48.ta,grafica_48.rc, data.fecha_inicial_final.fecha_final, data.fecha_inicial_final.fecha_inicio);
            velocidad_direccion(vel_dir_48.vv,vel_dir_48.dv,data.fecha_inicial_final.fecha_final, data.fecha_inicial_final.fecha_inicio);
            let fechaHtml = `Fecha: ${gauge.fecha} ${gauge.hora}`;
            $('#fecha').html(fechaHtml);
            $('#buscar').removeClass('is-loading');
            return false;
        }
        let fechaHtml = `No hay registros en la base datos`;
        $('#fecha').html(fechaHtml);
        $('#buscar').removeClass('is-loading');

    }).fail(function (data){

    }).always(function (data){
        
    })
}

function buscar_ajax(fecha){
    if (!$('#buscar').hasClass('is-loading')){
        $('#buscar').addClass('is-loading');
    }
    $.ajax({
        url : window.location.pathname,
        type: 'POST',
        data: {
            'accion': 'buscar_fecha',
            'fecha': fecha,
        },
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            const gauge = data.gauge;
            const gauge_mm_acomulado = data.mm_acomulado;
            const grafica_48 = data.acomulado48;
            const vel_dir_48 = data.acomulado48;
            temp(gauge.ta);
            presion(gauge.pr);
            humedad(gauge.hr);
            vientoR(gauge.vv,gauge.dv);
            lluviaW(gauge.ri);
            lluvia48(gauge_mm_acomulado);
            comportamiento48h(grafica_48.hr,grafica_48.pr,grafica_48.ta,grafica_48.rc, data.fecha_inicial_final.fecha_final, data.fecha_inicial_final.fecha_inicio);
            velocidad_direccion(vel_dir_48.vv,vel_dir_48.dv,data.fecha_inicial_final.fecha_final, data.fecha_inicial_final.fecha_inicio);
            let fechaHtml = `Fecha: ${gauge.fecha} ${gauge.hora}`;
            $('#fecha').html(fechaHtml);
            $('#buscar').removeClass('is-loading');

            return false;
        }
        $('#buscar').removeClass('is-loading');
        Swal.fire({
            title: 'Avertencia!',
            text: data.error,
            icon: 'warning',
            confirmButtonText: 'OK'
        });
    }).fail(function (data){

    }).always(function (data){
        
    })
}

$(function (){
    call_ajax();
    
    $('#buscar').on('click', function () {
        let fecha = $("#input-fecha").val();
        if (fecha == '') {
            Swal.fire({
                title: 'Advertencia!',
                text: 'Ingrese una fecha para la búsqueda.',
                icon: 'warning',
                confirmButtonText: 'OK'
            });
        } else {
            buscar_ajax(fecha);
        }
    });

});