$(function () {
    $('.select2').select2({
        placeholder: 'Selecciona la Sociedad Científica',
        width: '100%',
        height: '100%',
    });

    $('#add-modal').on('click', function () {
        $('#modal-scientifica').addClass('is-active');
    });
    $('#modal-close').on('click', function () {
        $('#modal-scientifica').removeClass('is-active');
    });
    $('#modal-cancel').on('click', function () {
        $('#modal-scientifica').removeClass('is-active');
    });
});
$('#form-0').on('submit', function (e) {
    e.preventDefault();
    var parameters = new FormData(this); //$(this).serializeArray();
    Swal.fire({
        title: 'Confirmación',
        text: "Estas seguro de editar este miembro",
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
                        text: 'Miembro ha sido editado correctamente',
                        icon: 'success',
                        timer: 3000,
                        onClose: () => {
                            location.href = '/dashboart/miembros/list_miembros/';
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

$('#form-1').on('submit', function (e) {
    e.preventDefault();
    var parameters = new FormData(this); //$(this).serializeArray();
    Swal.fire({
        title: 'Confirmación!',
        text: "Estas seguro de crear esta Sociedad Científica",
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
                    Swal.fire(
                        'Verificación!',
                        'Sus datos han sido enviado correctamente',
                        'success'
                    )
                    
                    return false;
                }

                mensaje_error(data.error);
            }).fail(function (data) {
                console.log(data);
            }).always(function (data) {
                $('#modal-scientifica').removeClass('is-active');
                $('form')[1].reset();
                window.location.reload();
            });
        }
    });
});