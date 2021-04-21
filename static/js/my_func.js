function mensaje_error(obj) {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align= left; list-decorator= none;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ':' + value + '</li>';
        });
        html += '</ul>';
    }
    else {
        html += '<p>' + obj + '</p>';
    }
    Swal.fire({
        title: 'Error',
        html: html,
        icon: 'error',
        confirmButtonText: 'OK'
    });

}
function confirm(url, titulo, contenido, icono, parameters, funcion) {
    Swal.fire({
        title: titulo,
        text: contenido,
        icon: icono,
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Seguro!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.value) {
            $.ajax({
                url: url,
                type: 'POST',
                data: parameters,
                dataType: 'json'
            }).done(function (data) {
                if (!data.hasOwnProperty('error')) {
                    funcion();
                    return false;
                }
                mensaje_error(data.error);
            }).fail(function (data) {
            }).always(function (data) {
                $('form')[0].reset();
            });
        }
    })
}



$(function () {
    $("#btn-navleft").on('click', function () {
        $('html').toggleClass('has-aside-mobile-expanded')
    })

    $('#btn-navbar-menu').on('click', function () {
        $('#navbar-menu').toggleClass('is-active')
    });

    $('li').on('click', function (e) {
        // console.log(e.currentTarget);
    });

    Array.from(document.getElementsByClassName('menu is-menu-main')).forEach(function (el) {
        Array.from(el.getElementsByClassName('has-dropdown-icon')).forEach(function (elA) {
            elA.addEventListener('click', function (e) {
                var dropdownIcon = e.currentTarget.getElementsByClassName('dropdown-icon')[0].getElementsByClassName('icon')[0];
                e.currentTarget.parentNode.classList.toggle('is-active');
                var child = dropdownIcon.firstChild;
                if (child.classList.contains('fa-plus')){
                    child.classList.replace('fa-plus', 'fa-minus');
                }else{
                    child.classList.replace('fa-minus', 'fa-plus');
                }

            });
        });
    });

});
