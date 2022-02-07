
$(function () {
    // Eliminar estacion
    $('button[rel="delete"]').on('click', function () {
        let codigo = $(this).val();
        let parameters = { 'accion': 'eliminar', 'codigo': parseInt(codigo) }
        Swal.fire({
            title: 'Avertencia!',
            text: 'Estas seguro desea eliminar la estación ' + codigo,
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
                            title: 'Notificación!',
                            text: `Estación "${codigo}" ha sido eliminada correctamente`,
                            icon: 'success',
                            timer: 3000,
                            onClose: () => {
                                window.location.reload()
                            }
                        });
                        return false;
                    }
                    mensaje_error(data.error);
                }).fail(function (data) {
                }).always(function (data) {
                });
            }
        })
    });

});