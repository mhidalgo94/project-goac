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
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data: {
                'action': 'searchdata'
            },
            dataSrc: ''
        },
        columns:[
            {'data': 'id'},
            {'data': 'user'},
            {'data': 'key'},
            {'data': 'fecha_modificacion'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [-1],
                class : 'is-center',
                orderable: false,
                render: function(data,type,row){
                    var btn = '<button style="border:none;cursor:pointer;" class="tag is-warning is-normal mr-1" rel="update" id="'+data+'"><i class="fas fa-sync"></i></button>'
                    btn += '<button style="border:none;cursor:pointer;" class="tag is-danger is-noram" rel="delete" id="'+data+'"><i class="fas fa-trash"></i></button>'
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
        confirm(window.location.pathname, 'Advertencia','Estas seguro que deseas eliminar esta API Key?','warning' ,parameters, function(){
            Swal.fire({
                title : 'Notificación!',
                text : 'API Key ha sido eliminada correctamente',
                icon: 'success',
                timer: 3000,
                onClose: () => {
                    updatetable();
                }
            });
        });
    });
    $('#dtable').on('click', 'button[rel="update"]' , function(){
        var id = $(this).attr('id');
        var parameters = {'action':'update','id': parseInt(id) }
        confirm(window.location.pathname, 'Advertencia','Estas seguro que deseas actualizar esta API Key?','warning' ,parameters, function(){
            Swal.fire({
                title : 'Notifición!',
                text : 'API Key actualizada correctamente',
                icon: 'success',
                timer: 3000,
                onClose: () => {
                    updatetable();
                }
            });
        });
    });
    
});
