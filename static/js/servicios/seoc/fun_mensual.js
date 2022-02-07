
Highcharts.setOptions({
    lang: {
        shortMonths: ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
        weekdays: ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"],
        resetZoom: "Quitar Zoom"
    }
 });
 function grafica_cmw_mes(Deoa, Deoan, mensaje, min_max) {
    let style;
    let posicionY_text_ejx;
    let posicionX_text_ejx;
    if (mensaje === ""){
        posicionY_text_ejx = 0;
        posicionX_text_ejx = 0;
        mensaje = 'Hora y Fecha Local'
        style = {  "fontSize": "11px", "color": "#666666" }
    }else{
        style = { "fontWeight": "bolder", "fontSize": "14px", "color": "#CB0000" }
        posicionY_text_ejx = -190;
        posicionX_text_ejx = -10;
    }
    
    $('#mescmw').highcharts({
        chart: {
            zoomType: 'x',
            alignTicks: false
        },
        title: {
            text: 'Camagüey',
            y: 6
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
        xAxis: {

            type: 'datetime',
            maxZoom: 3600 * 60,
            title: {
                style: style,
                text: mensaje,
                y: posicionY_text_ejx,
                x:posicionX_text_ejx,
            },
            min:min_max.min,
            max: min_max.max
        },
        yAxis: {
            min: 0,
            max: 0.8,
            title: {
                text: ''
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
            shared: true
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
            type: 'column',
            name: 'Aerosoles + Nubes',
            data: Deoan

        }, {
            type: 'scatter',
            tooltip: {
                dateTimeLabelFormats: {
                    second: "%A, %b %e, %H:%M:%S",
                    minute: "%A, %b %e, %H:%M",
                    hour: "%A, %b %e, %H:%M",
                    day: "%A, %b %e, %Y",
                    week: "Week from %A, %b %e, %Y",
                    month: "%B %Y",
                    year: "%Y"
                },
                headerFormat: '<span style="font-size: 10px">{point.key}</span><br/>',
                pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name}: <b>{point.y}</b><br/>'

            },
            name: 'Aerosoles',
            data: Deoa
        }]
    });

}

function grafica_jvn_mes(Deoa, Deoan, mensaje, min_max) {
    let style;
    let posicionY_text_ejx;
    let posicionX_text_ejx;
    if (mensaje === ""){
        posicionY_text_ejx = 0;
        posicionX_text_ejx = 0;
        mensaje = 'Hora y Fecha Local'
        style = {  "fontSize": "11px", "color": "#666666" }
    }else{
        style = { "fontWeight": "bolder", "fontSize": "14px", "color": "#CB0000" }
        posicionY_text_ejx = -190;
        posicionX_text_ejx = -10;
    }
    $('#mesjvn').highcharts({
        chart: {
            zoomType: 'x',
            alignTicks: false
        },
        title: {
            text: 'Jovellanos',
            y: 6
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
        xAxis: {

            type: 'datetime',
            maxZoom: 3600 * 60,
            title: {
                style: style,
                text: mensaje,
                y: posicionY_text_ejx,
                x:posicionX_text_ejx,
            },
            min:min_max.min,
            max: min_max.max
        },
        yAxis: {
            min: 0,
            max: 0.8,
            title: {
                text: ''
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
            shared: true
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
            type: 'column',
            name: 'Aerosoles + Nubes',
            data: Deoan

        }, {
            type: 'scatter',
            tooltip: {
                dateTimeLabelFormats: {
                    second: "%A, %b %e, %H:%M:%S",
                    minute: "%A, %b %e, %H:%M",
                    hour: "%A, %b %e, %H:%M",
                    day: "%A, %b %e, %Y",
                    week: "Week from %A, %b %e, %Y",
                    month: "%B %Y",
                    year: "%Y"
                },
                headerFormat: '<span style="font-size: 10px">{point.key}</span><br/>',
                pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name}: <b>{point.y}</b><br/>'

            },
            name: 'Aerosoles',
            data: Deoa
        }]
    });

}

function grafica_lfe_mes(Deoa, Deoan, mensaje, min_max) {
    let style;
    let posicionY_text_ejx;
    let posicionX_text_ejx;
    if (mensaje === ""){
        posicionY_text_ejx = 0;
        posicionX_text_ejx = 0;
        mensaje = 'Hora y Fecha Local'
        style = {  "fontSize": "11px", "color": "#666666" }
    }else{
        style = { "fontWeight": "bolder", "fontSize": "14px", "color": "#CB0000" }
        posicionY_text_ejx = -190;
        posicionX_text_ejx = -10;
    }
    $('#meslfe').highcharts({
        chart: {
            zoomType: 'x',
            alignTicks: false
        },
        title: {
            text: 'Santa Fé',
            y: 6
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
        xAxis: {

            type: 'datetime',
            maxZoom: 3600 * 60,
            title: {
                style: style,
                text: mensaje,
                y: posicionY_text_ejx,
                x:posicionX_text_ejx,
            },
            min:min_max.min,
            max: min_max.max
        },
        yAxis: {
            min: 0,
            max: 0.8,
            title: {
                text: ''
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
            shared: true
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
            type: 'column',
            name: 'Aerosoles + Nubes',
            data: Deoan

        }, {
            type: 'scatter',
            tooltip: {
                dateTimeLabelFormats: {
                    second: "%A, %b %e, %H:%M:%S",
                    minute: "%A, %b %e, %H:%M",
                    hour: "%A, %b %e, %H:%M",
                    day: "%A, %b %e, %Y",
                    week: "Week from %A, %b %e, %Y",
                    month: "%B %Y",
                    year: "%Y"
                },
                headerFormat: '<span style="font-size: 10px">{point.key}</span><br/>',
                pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name}: <b>{point.y}</b><br/>'

            },
            name: 'Aerosoles',
            data: Deoa
        }]
    });

}
function grafica_tpc_mes(Deoa, Deoan, mensaje,min_max) {
    let style;
    let posicionY_text_ejx;
    let posicionX_text_ejx;
    if (mensaje === ""){
        posicionY_text_ejx = 0;
        posicionX_text_ejx = 0;
        mensaje = 'Hora y Fecha Local'
        style = {  "fontSize": "11px", "color": "#666666" }
    }else{
        style = { "fontWeight": "bolder", "fontSize": "14px", "color": "#CB0000" }
        posicionY_text_ejx = -190;
        posicionX_text_ejx = -10;
    }
    $('#mestcp').highcharts({
        chart: {
            zoomType: 'x',
            alignTicks: false
        },
        title: {
            text: 'Topes de Collantes',
            y: 6
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
        xAxis: {

            type: 'datetime',
            maxZoom: 3600 * 60,
            title: {
                style: style,
                text: mensaje,
                y: posicionY_text_ejx,
                x:posicionX_text_ejx,
            },
            min:min_max.min,
            max: min_max.max
        },
        yAxis: {
            min: 0,
            max: 0.8,
            title: {
                text: ''
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
            shared: true
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
            type: 'column',
            name: 'Aerosoles + Nubes',
            data: Deoan

        }, {
            type: 'scatter',
            tooltip: {
                dateTimeLabelFormats: {
                    second: "%A, %b %e, %H:%M:%S",
                    minute: "%A, %b %e, %H:%M",
                    hour: "%A, %b %e, %H:%M",
                    day: "%A, %b %e, %Y",
                    week: "Week from %A, %b %e, %Y",
                    month: "%B %Y",
                    year: "%Y"
                },
                headerFormat: '<span style="font-size: 10px">{point.key}</span><br/>',
                pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name}: <b>{point.y}</b><br/>'

            },
            name: 'Aerosoles',
            data: Deoa
        }]
    });

}
function call_ajax_data_mes(accion, fecha) {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'accion': 'datos_graficos_mes',
            'fecha_m': fecha,
        },
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            grafica_cmw_mes(data.cmwM.eoa, data.cmwM.eoan, data.cmwM.mensaje,data.cmwM.min_max);
            grafica_jvn_mes(data.jvnM.eoa, data.jvnM.eoan, data.jvnM.mensaje,data.jvnM.min_max);
            grafica_lfe_mes(data.lfeM.eoa, data.lfeM.eoan, data.lfeM.mensaje,data.lfeM.min_max);
            grafica_tpc_mes(data.tpcM.eoa, data.tpcM.eoan, data.tpcM.mensaje,data.tpcM.min_max);
            return false;
        }
        mensaje_error(data.error);

    }).fail(function (data) {
    }).always(function (data) {

    });


    $('form').on('submit', function (e) {
        e.preventDefault();
        if (!$('#buscar_gmensual').hasClass('is-loading')) {
            $('#buscar_gmensual').addClass('is-loading');
        }
        let parameter = $(this).serializeArray();
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: parameter,
            dataType: 'json'
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                console.log(data);
                grafica_cmw_mes(data.cmwM.eoa, data.cmwM.eoan, data.cmwM.mensaje,data.cmwM.min_max);
                grafica_jvn_mes(data.jvnM.eoa, data.jvnM.eoan, data.jvnM.mensaje,data.jvnM.min_max);
                grafica_lfe_mes(data.lfeM.eoa, data.lfeM.eoan, data.lfeM.mensaje,data.lfeM.min_max);
                grafica_tpc_mes(data.tpcM.eoa, data.tpcM.eoan, data.tpcM.mensaje,data.tpcM.min_max);

                return false;
            }
            mensaje_error(data.error);

        }).fail(function (data) {
        }).always(function (data) {
            $('#buscar_gmensual').removeClass('is-loading');
        });
    });

    $("#select_mes").change(function (){
        $('form').submit();
    });

    $("#select_anio").change(function (){
        $('form').submit();
    });


}
call_ajax_data_mes('call_ajax_data_mes', fecha_hoy);


