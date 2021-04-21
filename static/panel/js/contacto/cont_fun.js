
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
            {'data': 'subject'},
            {'data': 'correo'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [-1],
                class : 'is-center',
                orderable: false,
                render: function(data,type,row){
                    let btn = '<button style="border: none;cursor: pointer;" class="tag is-info is-normal ml-1" rel="info" id="'+row.id+'"><i class="fas fa-search"></i></button>'
                    btn += '<button style="border: none;cursor: pointer;" class="tag is-danger is-normal" rel="delete" id="'+row.id+'"><i class="fas fa-trash"></i></button>'
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
        confirm(window.location.pathname, 'Advertencia','Estas seguro que deseas eliminar este contacto?','warning' ,parameters, function(){
            Swal.fire({
                title : 'Notificación!',
                text : 'Datos de contacto han sido eliminado correctamente',
                icon: 'success',
                timer: 3000,
                onClose: () => {
                    updatetable();
                }
            });
            updatetable();
        });
    });
    $('#dtable').on('click', 'button[rel="info"]', function(){
        $('#modal-scientifica').addClass('is-active');
        let tr = dtabla.cell($(this).closest('td, li')).index();
        let datos = dtabla.row(tr.row).data();
        $('#nombre').append(datos.nombre);
        $('#correo').append(datos.correo);
        $('#titulo').append(datos.subject);
        $('#mensaje').append(datos.mensaje);
    });

    $('#modal-close').on('click', function () {
        $('#modal-scientifica').removeClass('is-active');
        $('#nombre').empty();
        $('#correo').empty();
        $('#titulo').empty();
        $('#mensaje').empty();
    });
    $('#modal-cancel').on('click', function () {
        $('#modal-scientifica').removeClass('is-active');
        $('#nombre').empty();
        $('#correo').empty();
        $('#titulo').empty();
        $('#mensaje').empty();
    });
});
