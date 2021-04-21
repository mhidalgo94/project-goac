var dtabla;
// Data Table de Usuarios
function updatetable(){
    dtabla = $('#dtable').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "language": {
            "sProcessing":     "Procesando...",
                        "sLengthMenu":     "Mostrar _MENU_ registros",
                        "sZeroRecords":    "No se encontraron resultados",
                        "sEmptyTable":     "Ningún dato disponible en esta tabla =(",
                        "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                        "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
                        "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
                        "sInfoPostFix":    "",
                        "sSearch":         "Buscar:",
                        "sUrl":            "",
                        "sInfoThousands":  ",",
                        "sLoadingRecords": "Cargando...",
                        "oPaginate": {
                            "sFirst":    "Primero",
                            "sLast":     "Último",
                            "sNext":     "Siguiente",
                            "sPrevious": "Anterior"
                        },
                        "oAria": {
                            "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
                        },
                        "buttons": {
                            "copy": "Copiar",
                            "colvis": "Visibilidad"
                        }
        },
        ajax: {
            url : window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ''
        },
        columns:[
            {'data': 'id'},
            {'data': 'nombre'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [-1],
                class : 'is-center',
                orderable: false,
                render: function(data,type,row){
                    var btn = '<button style="border:none;cursor:pointer;" class="tag is-warning is-normal" rel="edit" id="'+row.id+'"><i class="fas fa-edit"></i></button>'
                    btn += '<button style="border:none;cursor:pointer;" class="tag is-danger is-noram" rel="delete" id="'+row.id+'"><i class="fas fa-trash"></i></button>'
                    return btn
                }
            },
            
        ],
        initComplete: function(settings, json,data){
        }
    });
}

$(function (){
    updatetable();

    $('#update').on('click', function(){
        updatetable();
    });

    // Boton para eliminar
    $('#dtable').on('click', 'button[rel="delete"]' , function(){
        var id = $(this).attr('id');
        var parameters = {'action':'eliminar','id': parseInt(id) }        
        confirm(window.location.pathname, 'Advertencia','Estas seguro que deseas eliminar esta caregoría?','warning' ,parameters, function(){
            Swal.fire({
                title : 'Notificación!',
                text : 'Categoría ha sido eliminada correctamente',
                icon: 'success',
                timer: 3000,
                onClose: () => {
                    updatetable();
                }
            });
            // updatetable();
        });
    });
    $('#dtable').on('click', 'button[rel="edit"]' , function(){
        $('#title-modal').html('<i class="fas fa-edit mr-1"></i>Editar Categoría');
        $('input[name="action"]').val('edit-catinvest');
        const datos = dtabla.row($(this).parents('tr')).data();
        $('input[name="id"]').val(datos.id);
        $('input[name="nombre"]').val(datos.nombre);
        $('#modal-categoriainv').addClass('is-active');
    });

    $('#form-1').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this); //$(this).serializeArray();
        Swal.fire({
            title: 'Confirmación!',
            text: "Seguro de realizar esta acción",
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
                    data: parameters,
                    dataType: 'json',
                    processData: false,
                    contentType: false,
                }).done(function (data) {
                    if (!data.hasOwnProperty('error')) {
                        Swal.fire({
                            title: 'Notificación!',
                            text: 'Cambios realizados correctamente',
                            icon: 'success',
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
                    $('#modal-categoriainv').removeClass('is-active');
                    $('#form-1').trigger('reset');
                });
            }
        });
    });

    $('#add-categoria').on('click', function () {
        $('#title-modal').html('<i class="fas fa-plus mr-1"></i>Crear Categoria');
        $('input[name="action"]').val('create-catinvest');
        $('#modal-categoriainv').addClass('is-active');
        $('#id_nombre').focus();

    });
    $('#modal-close').on('click', function () {
        $('#modal-categoriainv').removeClass('is-active');
        $('#form-1').trigger('reset');
    });
    
});
