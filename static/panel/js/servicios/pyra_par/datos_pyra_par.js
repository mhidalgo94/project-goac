function updatetable() {
    dtabla = $('#dtable').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
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
            data: {
                'accion': 'buscar_archivos'
            },
            dataSrc: ''
        },
        columns: [
            { 'data': 'id' },
            { 'data': 'fecha' },
            { 'data': 'tiempo' },
            { 'data': 'pyra' },
            { 'data': 'par' },
            { 'data': 'id' },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'is-center',
                orderable: false,
                render: function (data, type, row) {
                    let html = '<button style="border:none;cursor:pointer;" class="tag is-danger is-noram" rel="delete" id="'+row.id+'"><i class="fas fa-trash"></i></button>'
                    return html;

                }
            },
        ],
        initComplete: function (settings, json, data) {
        }
    });
}

$(function () {
    $('#update').on('click', function () {
        updatetable();
    });

    // Boton para eliminar archivo
    $('#dtable').on('click', 'button[rel="delete"]' , function(){
        var id = $(this).attr('id');
        var parameters = {'accion':'eliminar','id': parseInt(id) }        
        confirm(window.location.pathname, 'Advertencia','Estas seguro que deseas eliminar estos datos del servidor?','warning' ,parameters, function(){
            Swal.fire({
                title : 'Notifición!',
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
    // Iniciar tabla
    updatetable();


});