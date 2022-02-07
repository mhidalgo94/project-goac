var dtabla = $('#dtable');
function updatetable() {
    dtabla.DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        scrollX: true,
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla =(",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "<button class='button is-link is-loading is-inverted is-outlined'>Cargando</button>",
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

        ajax: {
            url: window.location.pathname,
            type: 'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data: {
                'accion': 'buscar_archivos'
            },
            dataSrc: ''
        },
        columns: [
            { 'data': 'estacion' },
            { 'data': 'fecha' },
            { 'data': 'tiempo' },
            { 'data': 'dc' },
            { 'data': 'dw' },
            { 'data': 'dnt' },
            { 'data': 'eoa' },
            { 'data': 'eoan' },
            { 'data': 'id' },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'is-center',
                orderable: false,
                render: function (data, type, row) {
                    
                    let html = '<button style="border:none;cursor:pointer;" class="tag is-warning is-normal" rel="edit" id="'+data+'"><i class="fas fa-edit"></i></button>'
                    html += '<button style="border:none;cursor:pointer;" class="tag is-danger is-noram" rel="delete" id="'+row.id+'"><i class="fas fa-trash"></i></button>'
                    return html;
                }
            },
        ],
        initComplete: function (settings, json, data) {
        }


    });
    


}

function filter(estacion,fechaInicial,fechaFinal){
    dtabla.DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        scrollX: true,
        order:false,
        paging:false,
        ordering:false,
        info:false,
        dom:"Bfrtip",
        buttons: [
            { extend: 'excelHtml5', text: 'Excel <i class="fas fa-file-download"></i>', title: function (){
                let inicial = fechaInicial.substr(0,10).split("-").join("");
                let final = fechaFinal.substr(0,10).split("-").join("");
                return `SEOC${estacion}${inicial}-${final}`;
            },titleAttr: 'Excel', className: 'buttons is-primary is-small' },
            { extend: 'csvHtml5', text: 'CSV <i class="fas fa-file-download"></i>', title:function(){
                let inicial = fechaInicial.substr(0,10).split("-").join("");
                let final = fechaFinal.substr(0,10).split("-").join("");
                return `SEOC${estacion}${inicial}-${final}`;
            },titleAttr: 'CSV', className: 'buttons is-success is-small' },
        ],
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla =(",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "<button class='button is-link is-loading is-inverted is-outlined'>Cargando</button>",
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
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data: {
                "accion": "filter",
                "fechaInicial": fechaInicial,
                "fechaFinal": fechaFinal,
                "estacion":estacion,
            },
            dataSrc: ''
        },
        columns: [
            { 'data': 'estacion' },
            { 'data': 'fecha' },
            { 'data': 'tiempo' },
            { 'data': 'dc' },
            { 'data': 'dw' },
            { 'data': 'dnt' },
            { 'data': 'eoa' },
            { 'data': 'eoan' },
            { 'data': 'id' },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'is-center',
                orderable: false,
                render: function (data, type, row) {
                    
                    let html = '<button style="border:none;cursor:pointer;" class="tag is-warning is-normal" rel="edit" id="'+data+'"><i class="fas fa-edit"></i></button>'
                    html += '<button style="border:none;cursor:pointer;" class="tag is-danger is-noram" rel="delete" id="'+row.id+'"><i class="fas fa-trash"></i></button>'
                    return html;
                }
            },
        ],
        initComplete: function (settings, json, data) {

        }
    });

    
}

$("#form-filter").on("submit",function (ev){
    ev.preventDefault();
    let data = new FormData(ev.target);
    let estacion = data.get('estacion');
    let fechaInicial =data.get('fechaInicial');
    let fechaFinal = data.get('fechaFinal');


    if(estacion.length == 0 || fechaFinal.length == 0 || fechaFinal.length == 0){
        Swal.fire({
                title: 'Alerta!',
                text: 'Seleccione un rango de fecha a seleccionar',
                icon: 'warning',
                timer: 3000,
            });
    } else{
        filter(estacion,fechaInicial,fechaFinal)

    }


})

$(function () {


    $('#update').on('click', function () {
        updatetable();
    });

    $('#dtable').on('click', 'button[rel="edit"]', function(){
        var id_ = $(this).attr('id');
        location.href = "/dashboart/servicios/seoc/edit-seoc/"+id_+"/";
    });

    // Boton para eliminar archivo
    $('#dtable').on('click', 'button[rel="delete"]' , function(){
        var id = $(this).attr('id');
        var parameters = {'accion':'eliminar','id': parseInt(id) }        
        confirm(window.location.pathname, 'Advertencia','Estas seguro que deseas eliminar estos datos del servidor?','warning' ,parameters, function(){
            Swal.fire({
                title : 'Notificación!',
                text : 'Los datos han sido eliminado correctamente',
                icon: 'success',
                timer: 3000,
                onClose: () => {
                    updatetable();
                }
            });
            // updatetable();
        });
    });

    // Calendario Bulma pra boton de busqueda por fecha
    var filterDate1 = bulmaCalendar.attach("#filter-date1", {
        type:"datetime",
        dateFormat: 'DD-MM-YYYY',
        showHeader:false,
        showClearButton: false,
        showFooter: true,
        showClearButton:false,
        validateLabel:"Validar",
        todayLabel:"Hoy",
        cancelLabel:"Cancelar",

    });
    var filterDate2 = bulmaCalendar.attach("#filter-date2", {
        type:"datetime",
        dateFormat: 'DD-MM-YYYY',
        showHeader:false,
        showClearButton: false,
        showFooter: true,
        showClearButton:false,
        validateLabel:"Validar",
        todayLabel:"Hoy",
        cancelLabel:"Cancelar",
    });

    // Iniciar tabla
    updatetable();


});

