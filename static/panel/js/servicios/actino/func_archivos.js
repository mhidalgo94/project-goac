
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
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data: {
                'accion': 'buscar_archivos'
            },
            dataSrc: 'datos'
        },
        columns: [
            { 'data': 'archivo' },
            { 'data': 'tamano' },
            // {'data': 'doc'},
            { 'data': 'id' },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'is-centered pl-0 pr-0',
                orderable: false,
                render: function (data, type, row) {
                    let html = '';
                    // Boton lectura archivo
                    html += '<button class="button is-info is-small pt-0 pb-0 mr-1" rel="btn-view" val="' + row.archivo + '"><span class="icon is-small pt-0 pb-0 pl-0 pr-0"><i class="fas fa-search"></i></span></button>'
                    // Boton descargar archivo
                    html +='<a href="/static/servicios/actino/csv/' + row.archivo + '" class=" button is-info is-small pt-0 pb-0 pl-2 pr-2"><i class="fas fa-file"></i></a>'
                    // Boton eliminar archivo
                    html += '<button class="button is-danger is-small pt-0 pb-0 ml-1" rel="btn-del" val="' + row.archivo + '"><span class="icon is-small pt-0 pb-0 pl-0 pr-0"><i class="fas fa-trash"></i></span></button>'
                    return html;

                }
            },
        ],
        initComplete: function (settings, json, data) {
        }
    });
}

$(function () {
    updatetable();
    $('#update').on('click', function () {
        updatetable();
    });

    $('#dtable').on('click', 'button[rel="btn-view"]', function(){
        $(this).addClass('is-loading');
        let archivo = $(this).attr('val');
        let parameters = { 'accion': 'leer-archivo', 'archivo': archivo}
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data: parameters,
            dataType: 'json',
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                $('.is-loading').removeClass('is-loading');
                $('#modal-viewfile').addClass('is-active');
                $('#name-file').html(archivo);
                document.getElementById('file-lectura').innerText = data.lectura;
                document.getElementById('modal-download-file').href = `/static/servicios/actino/csv/${archivo}`
                return false;
            }
            $('.is-loading').removeClass('is-loading');
            mensaje_error(data.error);
        }).fail(function (data) {
        }).always(function (data) {
        });
    })

    $('#fileview-close').on('click', function () {
        $('#modal-viewfile').removeClass('is-active');
    });

    // Boton para eliminar archivo
    $('#dtable').on('click', 'button[rel="btn-del"]', function () {
        let archivo = $(this).attr('val');
        let parameters = { 'accion': 'eliminar', 'archivo': archivo ,'path': 'diario'}
        Swal.fire({
            title: 'Notificación!',
            text: `Estas seguro eliminar el archivo '${archivo}' ?`,
            icon: 'warning',
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
                        Swal.fire({
                            title: 'Correcto',
                            text: data,
                            icon: 'success',
                            confirmButtonText: 'OK',
                            timer: 3000,
                            onClose: () => {
                                updatetable();
                            }
                        });
                        return false;
                    }
                    mensaje_error(data.error);
                }).fail(function (data) {
                }).always(function (data) {
                });
            }
        });

    });

    $('#id_input_file').change(function(){
        let datos = new FormData(this.form);
        let archivo = this.files[0].name;

        Swal.fire({
            title: 'Notificación!',
            text: `Estas seguro subir el archivo '${archivo}' al servidor? `,
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
                    data: datos,
                    dataType: 'json',
                    processData: false,
                    contentType: false
                }).done(function (data) {
                    if (!data.hasOwnProperty('error')) {
                        Swal.fire({
                            title: 'Correcto',
                            text: data,
                            icon: 'success',
                            confirmButtonText: 'OK',
                            timer: 3000,
                            onClose: () => {
                                updatetable();
                            }
                        });
                        return false;
                    }
                    mensaje_error(data.error);
                }).fail(function (data) {
                }).always(function (data) {
                });
            }
        });
    });

});