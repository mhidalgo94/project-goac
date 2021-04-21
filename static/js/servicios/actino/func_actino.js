var dataTable;
var grafica_global;
var grafica_directa;
var grafica_difusa;
var valor_verano = document.getElementById('horario_verano').value;
// Insertar datos al estado del tiempo
function EstadoTiempo(datos, info) {
    if (datos) {
        if (datos.global === "-999" || datos.global === "-999.0") {
            if (datos.fenom === '4') {
                document.getElementById('est_tiempo').style.display = 'none';
                document.getElementById('est_leyenda').style.display = 'none';
                document.getElementById('est_fenomeno').style.display = 'block';
                $('#text_fenomeno').text('Neblina');
            } else if (datos.fenom === '5') {
                document.getElementById('est_tiempo').style.display = 'none';
                document.getElementById('est_leyenda').style.display = 'none';
                document.getElementById('est_fenomeno').style.display = 'block';
                $('#text_fenomeno').text('Niebla');
            } else if (datos.fenom === '6') {
                document.getElementById('est_tiempo').style.display = 'none';
                document.getElementById('est_leyenda').style.display = 'none';
                document.getElementById('est_fenomeno').style.display = 'block';
                $('#text_fenomeno').text('Lluvia');
            } else if (datos.fenom === '7') {
                document.getElementById('est_tiempo').style.display = 'none';
                document.getElementById('est_leyenda').style.display = 'none';
                document.getElementById('est_fenomeno').style.display = 'block';
                $('#text_fenomeno').text('Chubascos');
            } else if (datos.fenom === '8') {
                document.getElementById('est_tiempo').style.display = 'none';
                document.getElementById('est_leyenda').style.display = 'none';
                document.getElementById('est_fenomeno').style.display = 'block';
                $('#text_fenomeno').text('Termenta con Precipitación');
            } else if (datos.fenom === '9') {
                document.getElementById('est_tiempo').style.display = 'none';
                document.getElementById('est_leyenda').style.display = 'none';
                document.getElementById('est_fenomeno').style.display = 'block';
                $('#text_fenomeno').text('Tormenta sin Precipitación');
            }
        } else {
            $('#et-aire').html(datos.temp_aire);
            $('#et-suelo').html(datos.temp_suelo);
            if (datos.humedad_relativa === "-999" || datos.humedad_relativa === "-999.0") {
                $('#et-hr').html("");
                $('#et-aire').html("");
            } else {
                $('#et-hr').html(datos.humedad_relativa);
                $('#et-aire').html(datos.temp_aire);
            }

            //Condiciones de suelo y viento
            if (datos.temp_suelo === '-999.0' || datos.temp_suelo === '-999') {
                $('#et-suelo').html("ND");
            } else {
                $('#et-suelo').html(datos.temp_suelo);
            }
            // Condiciones de nubosidad 
            if (parseInt(datos.nubosidad) <= 3) {
                document.getElementById('et-nubosidad').src = "/static/img/actino/sun.png";
            } else if (parseInt(datos.nubosidad) > 3 && parseInt(datos.nubosidad) < 7) {
                document.getElementById('et-nubosidad').src = "/static/img/actino/sun-cloud.png";
            } else if (parseInt(datos.nubosidad) >= 7) {
                document.getElementById('et-nubosidad').src = "/static/img/actino/cloud.png";
            }
            if (datos.vel_viento === '-999.0' || datos.vel_viento === '-999') {
                $('#et-velviento').html("");
            } else {
                $('#et-velviento').html(datos.vel_viento);
            }

            document.getElementById('est_tiempo').style.display = 'block';
            document.getElementById('est_leyenda').style.display = 'block';
            document.getElementById('est_fenomeno').style.display = 'none';
        }
        const sumar_hora = parseInt(valor_verano) + parseInt(datos.hora);
        $('#et-fecha').html("<i class='fas fa-calendar-alt mr-1 has-text-grey'></i>" + info.info.fecha + "<i class='fas fa-clock has-text-grey mr-1 ml-1'></i>" + sumar_hora + ":" + datos.min);
    }

}
// Cargar datos Tabla con dataTable
function datatable(json) {
    dataTable = $('#dtable').DataTable({
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "La tabla tiene _TOTAL_ registros",
            "sInfoEmpty": "Registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords":"<button class='button is-link is-loading is-inverted is-outlined'>Cargando</button>",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            },
            "buttons": {
                "copy": "Copiar",
                "colvis": "Visibilidad"
            }
        },
        "paging": false,
        "sort": false,
        "searching": false,
        "responsive": false,
        "destroy": true,
        "deferRender": false,
        'autoWidth': false,
        'scrollX': true,
        "data": json.datos,
        columns: [
            { 'data': 'hora' },
            { 'data': 'disco_solar' },
            { 'data': 'nubosidad' },
            { 'data': 'humedad_relativa' },
            { 'data': 'vel_viento' },
            { 'data': 'temp_aire' },
            { 'data': 'temp_suelo' },
            { 'data': 'directa' },
            { 'data': 'difusa' },
            { 'data': 'global' },
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'has-text-centered',
                orderable: false,
                render: function (data, type, row) {
                    const hora_suma = parseInt(row.hora) + parseInt(valor_verano);
                    const hora_min = hora_suma + ":" + row.min;
                    return hora_min;
                }
            },
            {
                targets: [1],
                class: 'has-text-centered',
                orderable: false,
                render: function (data, type, row) {
                    if (row.disco_solar === "0" || row.disco_solar === "1") {
                        let sol = "<figure class='image is-32x32 ml-0 mr-0'><img src='/static/img/actino/sun.png' alt='image'></figure>";
                        return sol
                    } else if (row.disco_solar === "2" || row.disco_solar === "3") {
                        let sol = "<figure class='image is-32x32 ml-0 mr-0'><img src='/static/img/actino/sun-cloud.png' alt='image'></figure>";
                        return sol
                    } else {
                        let sol = "<figure class='image is-32x32 ml-0 mr-0'><img src='/static/img/actino/sun-cancel.png' alt='image'></figure>";
                        return sol
                    }
                }
            },
            {
                targets: [6],
                class: 'has-text-centered',
                orderable: false,
                render: function (data, type, row) {
                    if (data === "-999.0" || data === '-999') {
                        let suelo = "<label class='tag is-normal has-background-grey'><b class='has-text-white'>ND</b></label>";
                        return suelo
                    } else {
                        return data;
                    }
                }
            },
        ],
        rowCallback: function (row, data, displayNum, displayIndex, dataIndex) {
            let hora_suma = parseInt(data.hora) + parseInt(valor_verano);
            let hora = hora_suma + ":" + data.min;
            // let hora = data.hora + ":" + data.min;
            let notas = data.notas;
            if (data.global === "-999" || data.global === "-999.0") {
                if (data.notas === '') {
                    if (data.fenom === "0") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>No hay observación</b></td>';
                    } else if (data.fenom === "1") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: Rocio</b></td>';

                    } else if (data.fenom === "2") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: Humo</b></td>';

                    } else if (data.fenom === "3") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: Bruma</b></td>';

                    } else if (data.fenom === "4") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: Neblina</b></td>';

                    } else if (data.fenom === "5") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: Niebla</b></td>';

                    } else if (data.fenom === "6") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: LLuvia</b></td>';

                    } else if (data.fenom === "7") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: Chubascos</b></td>';

                    } else if (data.fenom === "8") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: Tormenta con Precipitaciones</b></td>';

                    } else if (data.fenom === "9") {
                        row.innerHTML = '<td class="ha-text-white has-text-centered has-background-grey-light">' + hora + '</td><td colspan="9" class="has-text-danger-dark has-background-grey-light"><b>Fenómeno: Tormenta sin Precipitaciones</b></td>';
                    }
                } else {
                    row.innerHTML = '<td class="has-text-centered">' + hora + '</td><td><figure class="has-text-centered image is-32x32 ml-0 mr-0"><img src="/static/img/actino/sun-cancel.png" alt="image"></figure></td><td colspan="8" class="has-text-danger"><b>Nota:' + notas + '</b></td>';
                }

            }
        },
        initComplete: function (settings, xhr, data) {
            if ($('#buscar').hasClass('is-loading')){
                $('#buscar').removeClass('is-loading');
            }
        }
    });
}
function LimpiarTable() {
    let table = $('#dtable').DataTable({
        "paging": false,
        "sort": false,
        "searching": false,
        "responsive": false,
        "destroy": true,
        "deferRender": false,
        'autoWidth': false,
        'scrollX': true,
        "data": {},
    });
    // table.clear().draw();
}
function LimpiarEstadoTiempo() {
    $('#et-fecha').html("");
    $('#et-aire').html("");
    $('#et-suelo').html("");
    $('#et-hr').html("");
    $('#et-velviento').html("");
    document.getElementById('est_tiempo').style.display = 'block';
    document.getElementById('est_leyenda').style.display = 'block';
    document.getElementById('est_fenomeno').style.display = 'none';
}
function DetallesObservador(nombre, especialidad, xp, fecha_nac, img) {
    $('#nombre').html(nombre);
    $('#especialidad').html(especialidad);
    $('#xp').html(xp);
    $('#fecha_nac').html(fecha_nac);
    document.getElementById('img-obv').src = img;
}
// Iniciar grafico
// Grafico Radiacion Global
function GraficoRadGlobal(actual, fecha, historicos, ejeX) {
    grafica_global = Highcharts.chart('rad-global', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'Radiación Global'
        },
        subtitle: {
            text: 'Los valores medios históricos mostrados en la figura fueron calculados para todas las categorías de nubosidad. Estos valores corresponden al período 1981 - 2009',
            align: 'center',
            verticalAlign: 'bottom'
        },
        credits: {
            enabled: false
        },
        legend: {
            align: 'center',
            verticalAlign: 'bottom',
            borderWidth: 0,
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF'
        },
        xAxis: {
            categories: ejeX,
            max: ejeX.length - 1,
        },
        yAxis: {
            type: 'line',
            title: {
                text: 'Irradiancia W/m²'
            },
            min: 0,
        },
        plotOptions: {
            // Opacidad al relleno de historico
            area: {
                fillOpacity: 0.5
            },
        },
        // Desabilita el boton de exportacion
        exporting: {
            enabled: false
        },
        // Serie de datos del eje Y
        series: [{
            type: 'area',
            name: 'Históricos',
            data: historicos.slice(0,ejeX.length),
            color: '#2ee13d',
            marker: {
                enabled: false,
            },
            enableMouseTracking: true, // Abilitar datos sobre puntos
            gapSize: 0,

        }, {
            type: 'line',
            name: fecha,
            data: actual,//[0, 1, 4, null, 5, 2, 3, 7, 5, 2, 3, 7],
            color: '#1d71ef',
            // lineColor: 'transparent', // Quita las lineas de intercepcion
            marker: {
                enabled: true, // Abilitar los puntos de intercepcion
            },

            enableMouseTracking: true, // Abilitar datos sobre puntos
            gapSize: 0,
        }]
    });
}
// Grafico Radiacion Directa
function GraficoRadDirecta(actual, fecha, historicos, ejeX) {
    grafica_directa = Highcharts.chart('rad-directa', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'Radiación Directa'
        },
        subtitle: {
            text: 'Los valores medios históricos mostrados en la figura fueron calculados para todas las categorías de nubosidad. Estos valores corresponden al período 1981 - 2009',
            align: 'center',
            verticalAlign: 'bottom'
        },
        credits: {
            enabled: false
        },
        legend: {
            align: 'center',
            verticalAlign: 'bottom',
            borderWidth: 0,
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF'
        },
        xAxis: {
            categories: ejeX,
            max: ejeX.length - 1,
        },
        yAxis: {
            type: 'line',
            title: {
                text: 'Irradiancia W/m²'
            },
            min: 0,
        },
        plotOptions: {
            // Opacidad al relleno de historico
            area: {
                fillOpacity: 0.5
            },
        },
        // Desabilita el boton de exportacion
        exporting: {
            enabled: false
        },
        // Serie de datos del eje Y
        series: [{
            type: 'area',
            name: 'Históricos',
            data: historicos.slice(0,ejeX.length),
            color: '#2ee13d',
            marker: {
                enabled: false,
            },
            enableMouseTracking: true, // Abilitar datos sobre puntos
            gapSize: 0,

        }, {
            type: 'line',
            name: fecha,
            data: actual,//[0, 1, 4, null, 5, 2, 3, 7, 5, 2, 3, 7],
            color: '#1d71ef',
            // lineColor: 'transparent', // Quita las lineas de intercepcion
            marker: {
                enabled: true, // Abilitar los puntos de intercepcion
            },
            enableMouseTracking: true, // Abilitar datos sobre puntos
            gapSize: 0,
        }]
    });
}
// Grafico Radiacion Difusa
function GraficoRadDifusa(actual, fecha, historicos, ejeX) {
    grafica_difusa = Highcharts.chart('rad-difusa', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'Radiación Difusa'
        },
        subtitle: {
            text: 'Los valores medios históricos mostrados en la figura fueron calculados para todas las categorías de nubosidad. Estos valores corresponden al período 1981 - 2009',
            align: 'center',
            verticalAlign: 'bottom'
        },
        credits: {
            enabled: false
        },
        legend: {
            align: 'center',
            verticalAlign: 'bottom',
            borderWidth: 0,
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF'
        },
        xAxis: {
            categories: ejeX,
            max: ejeX.length - 1,
        },
        yAxis: {
            type: 'line',
            title: {
                text: 'Irradiancia W/m²'
            },
            min: 0,
        },
        plotOptions: {
            // Opacidad al relleno de historico
            area: {
                fillOpacity: 0.5
            },
        },
        // Desabilita el boton de exportacion
        exporting: {
            enabled: false
        },
        // Serie de datos del eje Y
        series: [{
            type: 'area',
            name: 'Históricos',
            data: historicos.slice(0,ejeX.length),
            color: '#2ee13d',
            marker: {
                enabled: false, // Abilitar los puntos de intercepcion
            },
            enableMouseTracking: false, // Abilitar datos sobre puntos
            gapSize: 0,

        }, {
            type: 'line',
            name: fecha,
            data: actual,
            color: '#1d71ef',
            // lineColor: 'transparent', // Quita las lineas de intercepcion
            marker: {
                enabled: true, // Abilitar los puntos de intercepcion
            },
            enableMouseTracking: true, // Abilitar datos sobre puntos
            gapSize: 0,
        }]
    });
}

// Pedir datos con ajax al server
function call_ajax(action, estacion, fecha) {
    if (!$('#buscar').hasClass('is-loading')){
        $('#buscar').addClass('is-loading');
    }
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': action,
            'estacion': estacion,
            'fecha': fecha
        },
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            $("#alerta").html('');
            dataTable = datatable(data);
            EstadoTiempo(data.datos[data.datos.length - 1], data);
            // Grafica Radiacion Global
            GraficoRadGlobal(data.grafico_global, data.info.fecha, data.grafico_global_historicos, data.ejex_grafico);
            // Grafica Radiacion Directa
            GraficoRadDirecta(data.grafico_directa, data.info.fecha, data.grafico_directa_historicos, data.ejex_grafico);
            // Grafica Radiacion Difusa
            GraficoRadDifusa(data.grafico_difusa, data.info.fecha, data.grafico_difusa_historicos, data.ejex_grafico);
            // Div con la informacion de los Observadores
            DetallesObservador(data.info.nombre, data.info.cargo, data.info.xp, data.info.fecha_nac, data.info.imagen);
            return false;
        }
        // Variable especifica la estacion para enviar a la alerta
        let estacion = $('#estacion option:selected').text();
        // Mensaje de alerta
        let alerta = data.error + " -- (" + estacion + ")";
        $("#alerta").html(alerta);
        // Limpiar estado del tiempo
        LimpiarEstadoTiempo()
        // Limpiar la tabla
        LimpiarTable();
        // Limpiar cuadro Observador
        DetallesObservador('', '', '', '', '/static/img/empty.png');
        // limpiar grafica
        if (grafica_global !== undefined) {
            grafica_global.destroy();
            grafica_difusa.destroy();
            grafica_directa.destroy();
        }
        $('#buscar').removeClass('is-loading');


    }).fail(function (data) {
    }).always(function (data) {

    });
}

// Otras funciones relacionadas con la pestañas
// y la carga del calendario 
$(function () {
    // Activar las pestañas de inicio
    $("#div-mediciones").show();
    $("#mediciones").addClass('is-active');
    $("#div-servicios").hide();
    $("#div-historicos").hide();
    $("#div-info").hide();
    $("#div-contacto").hide();
    // Mostrar pestaña de servicios
    $('#servicios').on('click', function () {
        $('li').removeClass('is-active');
        $(this).addClass('is-active')
        $("#div-historicos").hide();
        $("#div-mediciones").hide();
        $("#div-info").hide();
        $("#div-contacto").hide();
        $("#div-servicios").show();
        $("#select-est").hide();
    });
    // Mostrar pestaña de historicos
    $('#historicos').on('click', function () {
        $('li').removeClass('is-active');
        $(this).addClass('is-active')

        $("#select-est").hide();
        $("#div-servicios").hide();
        $("#div-mediciones").hide();
        $("#div-info").hide();
        $("#div-contacto").hide();
        $("#div-servicios").hide();
        $("#div-historicos").show();

    });
    // Mostrar pestaña de mediciones
    $('#mediciones').on('click', function () {
        $('li').removeClass('is-active');
        $(this).addClass('is-active')

        $("#select-est").show();
        $("#div-servicios").hide();
        $("#div-info").hide();
        $("#div-historicos").hide();
        $("#div-contacto").hide();
        $("#div-servicios").hide();
        $("#div-mediciones").show();
    });
    // Mostrar pestaña de informacion
    $('#info').on('click', function () {
        $('li').removeClass('is-active');
        $(this).addClass('is-active')

        $("#select-est").hide();
        $("#div-servicios").hide();
        $("#div-mediciones").hide();
        $("#div-historicos").hide();
        $("#div-contacto").hide();
        $("#div-servicios").hide();
        $("#div-info").show();
    });
    // Mostrar pestaña de contacto
    $('#contacto').on('click', function () {
        $('li').removeClass('is-active');
        $(this).addClass('is-active')

        $("#select-est").hide();
        $("#div-servicios").hide();
        $("#div-mediciones").hide();
        $("#div-historicos").hide();
        $("#div-info").hide();
        $("#div-contacto").show();
    });
    $('#update').on('click', function () {
        const estacion = $('#estacion').val();
        const fecha = $("#input-fecha").val();

        if (fecha == '') {
            call_ajax('hoy', estacion, fecha);
        } else {
            call_ajax('buscar_fecha', estacion, fecha);
        }
    });
    $('#estacion').change(function () {
        const estacion = $('#estacion').val();
        const fecha = $("#input-fecha").val();

        if (fecha == '') {
            call_ajax('hoy', estacion, fecha);
        } else {
            call_ajax('buscar_fecha', estacion, fecha);
        }
    });

    $('#buscar').on('click', function () {
        const fecha = $("#input-fecha").val();
        const estacion = $('#estacion').val();
        if (fecha == '') {
            $("#alerta").html('Seleccione una fecha por favor');
        } else {
            call_ajax('buscar_fecha', estacion, fecha);
        }
    });

    // Llamar datatable al cargar la pagina
    call_ajax('hoy', $('#estacion').val(), '');
    // Calendario Bulma pra boton de busqueda por fecha
    var calendario = bulmaCalendar.attach("#input-fecha", {
        dateFormat: 'YYYY-MM-DD',
        showClearButton: false,
    });

});
