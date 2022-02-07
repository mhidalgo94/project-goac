$("#section-mediciones").show();
$("#mediciones").addClass('is-active');
$("#section-info").hide();

$('#mediciones').on('click', function () {
    $('li').removeClass('is-active');
    $(this).addClass('is-active')
    $("#section-info").hide();
    $("#section-mediciones").show();
});

$('#info').on('click', function () {
    $('li').removeClass('is-active');
    $(this).addClass('is-active')
    $("#section-mediciones").hide();
    $("#section-info").show();
});


//Grafica del Pyra y Par
//Poner la fecha en el subtitulo
var fecha = new Date();
var fecha_string = fecha.toLocaleDateString();
let default_date = `${fecha.getFullYear()}-${fecha.getMonth()+1}-${fecha.getDate()}`;

Highcharts.setOptions({
    lang: {
        shortMonths: ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
        weekdays: ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"],
        resetZoom: "Quitar Zoom"
    },
    global: {
          /**
           * Use moment-timezone.js to return the timezone offset for individual
           * timestamps, used in the X axis labels and the tooltip header.
           */
          getTimezoneOffset: function (timestamp) {
              d = new Date();
              timezoneOffset =  d.getTimezoneOffset()

              return timezoneOffset;
          }
      }
 });


function grafico_pyra_par(Pyra, Par, fecha_inicial, fecha_final, mensaje){
    let i = new Date(fecha_inicial);
    let f = new Date(fecha_final);
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
    Highcharts.chart('pyra-par', {
        chart: {
            type: 'area',
            zoomType: 'x'
        },
        title: {
                text: 'Gráfico diario Radiación Solar'
            },
        legend: {
            align: 'center',
            verticalAlign: 'bottom',
            borderWidth: 0,
        },
        exporting: {
            enabled:true,
            buttons:{
                contextButton: {
                menuItems: ['downloadJPEG',]
                },
            },
            scale:1,
            // width:'1924px',
            sourceWidth: 1000,
            sourceHeight: 600,
        },
        xAxis: [{
            type: 'datetime',
            // maxZoom: 60 * 1000,
            min: fecha_inicial,
            max: fecha_final,
            pointStart:fecha_inicial,
            // pointEnd:fecha_final,
            title: {
                style: style,
                text: mensaje,
                y: posicionY_text_ejx,
                x:posicionX_text_ejx,
            },
        }],
        yAxis: [{ // Valores yAxis
            gridLineWidth: 0,
            title: {
                text: 'Irradiancia Global (W/m²)',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            },
            labels: {
                format: '{value}',// W/m²',
                // style: {
                //     color: Highcharts.getOptions().colors[7]
                // }
            },
            min:0,
        }, { // Valores yAxis
            gridLineWidth: 1,
            title: {
                text: 'Irradiancia PAR (micromole / m²sr-1',
                // style: {
                //     color: Highcharts.getOptions().colors[4]
                // }
            },
            labels: {
                format: '{value}',// W/m²',
                // style: {
                //     color: Highcharts.getOptions().colors[1]
                // }
            },
            opposite: true,
            min:0,
            max:2600,
        }],
        tooltip: {
            shared: true,
            crosshairs: true
        },
        plotOptions: {
            area: {
                fillOpacity: 0.5
            }
        },
        credits: {
            enabled: true,
            text:"GOAC",
            href:"http://www.goac.cu",
            position:{
                x:-60,
                y:-60,
            },
            style:{
                fontSize:"12px",
            }
        },
        series: [{
            type:'area',
            yAxis: 0,
            name: 'Irradiancia Global (W/m²)',
            data: Pyra
        }, {
            type:'area',
            yAxis: 1,
            name: 'Radiación Fotosintéticamente Activa (micromole/m²sr-1)',
            data: Par
        }]
    });
}


function call_ajax(fecha){
    if (!$('#buscar').hasClass('is-loading')){
        $('#buscar').addClass('is-loading');
    }
    $.ajax({
        url : window.location.pathname,
        type: 'POST',
        headers:{
            'X-CSRFToken':csrftoken
        },
        data: {
            'accion': 'get_data',
            'fecha': fecha
        },
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            let {pyra, par, fecha_inicio_final, mensaje} = data;
            console.log(fecha_inicio_final);
            $('#buscar').removeClass('is-loading');
            let inicial = new Date(fecha_inicio_final.salida);
            let puesta = new Date(fecha_inicio_final.puesta);
            grafico_pyra_par(pyra, par, fecha_inicio_final.salida,fecha_inicio_final.puesta,mensaje);

            return false;
        }
        Swal.fire({
            title: 'Avertencia!',
            text: data.error,
            icon: 'warning',
            confirmButtonText: 'OK'
        });
        $('#buscar').removeClass('is-loading');

        // grafico_pyra_par([],[],0,0,data.mensaje);

    }).fail(function(err){
        $('#buscar').removeClass('is-loading');
        console.log(err);
    }).always(function (data){
        let last_pyra = data.pyra;
        let last_par = data.par;
        let h1_ultipar = document.getElementById('ultipar');
        let p_ultidatepar = document.getElementById('ultidatepar');
        let h1_ultipira = document.getElementById('ultipira');
        let p_ultidatepira = document.getElementById('ultidatepira');


        // Esto es para el cuadro fecha de los ultimos datos
        let h1_fecha = document.getElementById('fecha');
        let fechautc = data.fecha;
        if (fechautc === undefined){
            h1_fecha.innerHTML = `<b>Fecha: Sin Datos</b>`;
        }else{
            // const localDate = new Date(fechautc);
            h1_fecha.innerHTML = `<b>Fecha: ${fechautc}</b>`;
        }

        // Estas condiciones es para ingresar el ultimo dato de pira y par
        // En los cuadros top
        // Tambien esta incluido el datetime del valor
        
        if(last_par===0 || last_par===undefined){
            h1_ultipar.innerText = 'Sin Datos';
            p_ultidatepar.innerHTML = "";


        }else{
            let ultipar = last_par[last_par.length -1][1];
            let ultidatepar = new Date(last_par[last_par.length -1][0]);
            h1_ultipar.innerText = `${ultipar.toFixed(3)}`;
            p_ultidatepar.innerHTML = `${ultidatepar.toLocaleDateString()} ${ultidatepar.toLocaleTimeString()}`;
        }

        if(last_pyra===0 || last_pyra===undefined){
            h1_ultipira.innerText = 'Sin Datos';
            p_ultidatepira.innerHTML = "";

        }else{
            let ultipira = last_pyra[last_pyra.length-1][1];
            let ultidatepira = new Date(last_pyra[last_pyra.length-1][0]);
            h1_ultipira.innerText = `${ultipira.toFixed(3)}`;
            p_ultidatepira.innerHTML = `${ultidatepira.toLocaleDateString()} ${ultidatepira.toLocaleTimeString()}`;
        }


        

        
    })
}

call_ajax(default_date)


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
        call_ajax(fecha);
    }
});
