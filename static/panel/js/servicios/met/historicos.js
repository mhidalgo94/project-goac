function updatetable() {
    dtabla = $('#dtable').DataTable({
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
            { 'data': 'fecha' },
            { 'data': 'variable' },
            { 'data': 'nombre' },
            { 'data': 'tipo' },
            { 'data': 'unidad_medida' },
            { 'data': 'valor' },
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
            {
                targets: [1],
                class: 'is-center has-text-centered',
                orderable: false,
                render: function (data, type, row) {
                    
                    return row.variable;
                }
            },
            {
                targets: [2],
                class: 'is-center has-text-centered',
                orderable: false,
                render: function (data, type, row) {
                    let html = row.nombre;
                    if(row.nombre ===null){
                        html = '<span class="tag is-danger is-small"><b>Asignar</b></span>'
                    }
                    return html;
                }
            },
            {
                targets: [-3],
                class: 'is-center has-text-centered',
                orderable: false,
                render: function (data, type, row) {
                    let html = row.unidad_medida;
                    if(row.unidad_medida === null){
                        html = '<span class="tag is-danger is-small"><b>Asignar</b></span>'
                    }
                    return html;
                }
            },
            {
                targets: [-2],
                class: 'is-center has-text-centered',
                orderable: false,
                render: function (data, type, row) {
                    return row.valor;
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

    $('#dtable').on('click', 'button[rel="edit"]', function(){
        var id_ = $(this).attr('id');
        location.href = "/dashboart/servicios/met/edit-historicos_met/"+id_+"/";
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
        });
    });
    // Iniciar tabla
    updatetable();

    $('#modal-close').on('click', function(){
        $('#modal-historicos').removeClass('is-active');
    });

    $('#agregar').on('click', function(){
        $('#modal-historicos').addClass('is-active');
    })
    $('#clear-form').on('click', function(){
        $('form')[0].reset();
    });

    $('form').on('submit', function(e){
        e.preventDefault();
        let parameters = $(this).serializeArray();
        console.log(parameters);
        Swal.fire({
            title: 'Confirmación',
            text: "Estas seguro de enviar esta información",
            icon: 'info',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Seguro!',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.value) {
                $.ajax({
                    url: window.location.pathname,
                    type: 'POST',
                    headers:{
                        'X-CSRFToken':csrftoken,
                    },
                    data: parameters,
                    dataType: 'json'
                }).done(function (data) {
                    if (!data.hasOwnProperty('error')) {
                        Swal.fire(
                            'Verificación!',
                            'Sus datos han sido enviado correctamente',
                            'success'
                        )
                        $('#modal-historicos').removeClass('is-active');
                        updatetable();
                        return false;
                    }

                mensaje_error(data.error);
                }).fail(function (data) {
                }).always(function (data) {
                    $('form')[0].reset();
                    
                });
            }
        });
    });


});