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
            {'data': 'titulo'},
            {'data': 'autor'},
            {'data': 'imagen'},
            {'data': 'doc'},
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
            {
                targets: [-2],
                class : 'is-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<a id="link-doc" href="' + row.doc[0] + '"><img src="' + row.doc[1] + '" class="image" style="width:28px; height: 28px;"></a>'
                }
            },
            {
                targets: [-3],
                class : 'is-center',
                orderable: false,
                render: function(data,type,row){
                    return '<img src="'+row.imagen+'" class="image" style="width: 48px; height: 48px;">'
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
        confirm(window.location.pathname, 'Advertencia','Estas seguro que deseas eliminar esta noticia?','warning' ,parameters, function(){
            Swal.fire({
                title : 'Notificación!',
                text : 'La Noticia ha sido eliminada correctamente',
                icon: 'success',
                timer: 3000,
                onClose: () => {
                    updatetable();
                }
            });
            // updatetable();
        });
    });
    $('#dtable').on('click', 'button[rel="edit"]', function(){
        var id_ = $(this).attr('id');
        location.href = "/dashboart/web/edit_noticias/"+id_+"/";
    });

    
});
