
$(function () {
    $('.select2').select2({
        placeholder: 'Selecciona el Miembro relacionado',
        width: '100%',
    });

    // Crear Miembros con ajax
    $('#form-0').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this); //$(this).serializeArray();
        Swal.fire({
            title: 'Confirmacion',
            text: "Estas seguro de editar esta investigacion",
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
                            text: 'Investigación ha sido editada correctamente',
                            icon: 'success',
                            timer: 3000,
                            onClose: () => {
                                location.href = '/dashboart/investigaciones/list_investigaciones/';
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
    // Crear Sociedad Cientifica con ajax modal
    $('#form-1').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this); //$(this).serializeArray();
        Swal.fire({
            title: 'Confirmacion',
            text: "Estas seguro de agregar nueva Categoria Investigacion",
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
                            title: 'Notificacion!',
                            text: 'Nueva Categoria creada correctamente',
                            icon: 'success',
                            timer: 3000,
                            onClose: () => {
                                location.reload();
                            }
                        });
                        return false;
                    }

                    mensaje_error(data.error);
                }).fail(function (data) {
                }).always(function (data) {
                    $('#modal-scientifica').removeClass('is-active');
                    $('form')[1].reset();
                });
            }
        });
    });

    $('#add-modal').on('click', function () {
        $('#modal-scientifica').addClass('is-active');
    });
    $('#modal-close').on('click', function () {
        $('#modal-scientifica').removeClass('is-active');
    });
});
