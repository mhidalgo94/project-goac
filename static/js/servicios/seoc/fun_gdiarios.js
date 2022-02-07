
function grafica_cmw(tiempo, eoa, eoan, mensaje) {
    let ejey_mensaje = -190;
    let ejex_mensaje = -10;
    let style = {"fontWeight": "bolder", "fontSize":"14px", "color": "#CB0000"};
    if (mensaje === ""){
        style = {},
        ejey_mensaje = 0;
        ejex_mensaje = 0;
        mensaje = 'Hora local';
    }
    $('#cmw').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Camagüey',
            y: 6
        },
        // Config eje x
        xAxis: {
            title: {
                text: 'Hora Local'
            },
            categories: tiempo,//Dhora,
            title: {
                style: style,
                text: mensaje,
                y: ejey_mensaje,
                x: ejex_mensaje
            }
        },
        // Desabilita el boton de exportacion
        exporting: {
            enabled:true,
            buttons:{
                contextButton: {
                menuItems: ['downloadPNG',]
                },
            }
        },
        yAxis: {
            min: 0,
            max: 1,
            title: {
                text: 'EOABA'
            }

        },
        legend: {
            align: 'center',
            x: 5,
            verticalAlign: 'bottom',
            y: 10,
            floating: false,
            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: false
        },
        tooltip: {
            formatter: function () {
                return '<b> Hora Local: ' + this.x + '</b><br/>' +
                    this.series.name + ': ' + this.y;
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled: false,
                    color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                    style: {
                        textShadow: '0 0 3px black'
                    }
                }
            }
        },

        credits: {
            enabled: true,
            text:"GOAC",
            href:"http://www.goac.cu",
            position:{
                x:-60,
                y:-50,
            },
            style:{
                fontSize:"12px",
            }
        },
        series: [{
            name: 'Aerosoles + Nubes',
            data: eoan,//Deoan,
        }, {
            name: 'Aerosoles',
            data: eoa//Deoa

        }]
    });
}

function grafica_jvn(tiempo, eoa, eoan, mensaje) {
    let ejey_mensaje = -190;
    let ejex_mensaje = -10;
    let style = {"fontWeight": "bolder", "fontSize":"14px", "color": "#CB0000"};
    if (mensaje === ""){
        style = {},
        ejey_mensaje = 0;
        ejex_mensaje = 0;
        mensaje = 'Hora local';
    }
    $('#jvn').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Jovellanos',
            y: 6
        },
        xAxis: {
            categories: tiempo,//Dhora,
            title:{
                style: style,
                text: mensaje,
                y: ejey_mensaje,
                x: ejex_mensaje,
            }
        },
        yAxis: {
            min: 0,
            max: 1,
            title: {
                text: 'EOABA'
            }

        },
        // Desabilita el boton de exportacion
        exporting: {
            enabled:true,
            buttons:{
                contextButton: {
                menuItems: ['downloadPNG',]
                },
            }
        },
        legend: {
            align: 'center',
            x: 5,
            verticalAlign: 'bottom',
            y: 10,
            floating: false,
            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: false
        },
        tooltip: {
            formatter: function () {
                return '<b> Hora Local: ' + this.x + '</b><br/>' +
                    this.series.name + ': ' + this.y;
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled: false,
                    color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                    style: {
                        textShadow: '0 0 3px black'
                    }
                }
            }
        },

        credits: {
            enabled: true,
            text:"GOAC",
            href:"http://www.goac.cu",
            position:{
                x:-60,
                y:-50,
            },
            style:{
                fontSize:"12px",
            }
        },
        series: [{
            name: 'Aerosoles + Nubes',
            data: eoan//Deoan
        }, {
            name: 'Aerosoles',
            data: eoa//Deoa

        }]
    });
}

function grafica_tcp(tiempo, eoa, eoan, mensaje) {
    let ejey_mensaje = -190;
    let ejex_mensaje = -10;
    let style = {"fontWeight": "bolder", "fontSize":"14px", "color": "#CB0000"};
    if (mensaje === ""){
        style = {},
        ejey_mensaje = 0;
        ejex_mensaje = 0;
        mensaje = 'Hora local';
    }
    $('#tpc').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Topes de Collantes',
            y: 6
        },
        xAxis: {
            categories: tiempo,//Dhora,
            title:{
                style: style,
                text: mensaje,
                y: ejey_mensaje,
                x: ejex_mensaje,
            }
        },
        yAxis: {
            min: 0,
            max: 1,
            title: {
                text: 'EOABA'
            }

        },
        // Desabilita el boton de exportacion
        exporting: {
            enabled:true,
            buttons:{
                contextButton: {
                menuItems: ['downloadPNG',]
                },
            }
        },
        legend: {
            align: 'center',
            x: 5,
            verticalAlign: 'bottom',
            y: 10,
            floating: false,
            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: false
        },
        tooltip: {
            formatter: function () {
                return '<b> Hora Local: ' + this.x + '</b><br/>' +
                    this.series.name + ': ' + this.y;
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled: false,
                    color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                    style: {
                        textShadow: '0 0 3px black'
                    }
                }
            }
        },

        credits: {
            enabled: true,
            text:"GOAC",
            href:"http://www.goac.cu",
            position:{
                x:-60,
                y:-50,
            },
            style:{
                fontSize:"12px",
            }
        },
        series: [{
            name: 'Aerosoles + Nubes',
            data: eoan//Deoan
        }, {
            name: 'Aerosoles',
            data: eoa//Deoa

        }]
    });
}

function grafica_lfe(tiempo, eoa, eoan, mensaje) {
    let ejey_mensaje = -190;
    let ejex_mensaje = -10;
    let style = {"fontWeight": "bolder", "fontSize":"14px", "color": "#CB0000"};
    if (mensaje === ""){
        style = {},
        ejey_mensaje = 0;
        ejex_mensaje = 0;
        mensaje = 'Hora local';
    }
    $('#lfe').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Santa Fé',
            y: 6
        },
        xAxis: {
            categories: tiempo,//Dhora,
            title:{
                style: style,
                text: mensaje,
                y: ejey_mensaje,
                x: ejex_mensaje
            }
        },
        yAxis: {
            min: 0,
            max: 1,
            title: {
                text: 'EOABA'
            },

        },
        // Desabilita el boton de exportacion
        exporting: {
            enabled:true,
            buttons:{
                contextButton: {
                menuItems: ['downloadPNG',]
                },
            }
        },
        legend: {
            align: 'center',
            x: 5,
            verticalAlign: 'bottom',
            y: 10,
            floating: false,
            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: false
        },
        tooltip: {
            formatter: function () {
                return '<b> Hora Local: ' + this.x + '</b><br/>' +
                    this.series.name + ': ' + this.y;
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled: false,
                    color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                    style: {
                        textShadow: '0 0 3px black'
                    }
                }
            }
        },

        credits: {
            enabled: true,
            text:"GOAC",
            href:"http://www.goac.cu",
            position:{
                x:-60,
                y:-50,
            },
            style:{
                fontSize:"12px",
            }
        },
        series: [{
            name: 'Aerosoles + Nubes',
            data: eoan//Deoan
        }, {
            name: 'Aerosoles',
            data: eoa//Deoa

        }]
    });
}


function call_ajax_data(accion, fecha){
    if (!$('#buscar').hasClass('is-loading')){
        $('#buscar').addClass('is-loading');
    }
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'accion': accion,
            'fecha': fecha,
        },
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            grafica_cmw(data.cmw.tiempo, data.cmw.eoa, data.cmw.eoan, data.cmw.mensaje);
    
            grafica_jvn(data.jvn.tiempo, data.jvn.eoa, data.jvn.eoan, data.jvn.mensaje);
     
            grafica_lfe(data.lfe.tiempo, data.lfe.eoa, data.lfe.eoan, data.lfe.mensaje);
    
            grafica_tcp(data.tcp.tiempo, data.tcp.eoa, data.tcp.eoan, data.tcp.mensaje);
            $('#buscar').removeClass('is-loading');
            return false;
        }
        $('#buscar').removeClass('is-loading');
    }).fail(function (data) {
    }).always(function (data) {
        
    });
}



$(function () {
    
    call_ajax_data('datos_graficos',fecha_hoy );

    $('#buscar').on('click', function () {
        const fecha = $("#input-fecha").val();
        const estacion = $('#estacion').val();
        if (fecha == '') {
            Swal.fire({
                title: 'Alerta!',
                text: 'Seleccione una fecha por favor',
                icon: 'warning',
                timer: 3000,
            });
            $("#alerta").html();
        } else {
            call_ajax_data('datos_graficos', fecha);
        }
    });

    // Calendario Bulma pra boton de busqueda por fecha
    var calendario = bulmaCalendar.attach("#input-fecha", {
        startDate: new Date(),
        dateFormat: 'YYYY-MM-DD',
        showClearButton: false,
        showHeader: false,
    });
});
