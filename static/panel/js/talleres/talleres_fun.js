
$(function (){
    $('.select2').select2({
        placeholder: 'Selecciona Participantes',
        width: '100%',
    });

    $("#div-taller").show();
    $("#div-prog").hide();
    $("#div-resumenes").hide();
    $("#div-participantes").hide();

    $('#taller').on('click', function(){
        $('li').removeClass('is-active');
        $(this).addClass('is-active')
        $("#div-prog").hide();
        $("#div-resumenes").hide();
        $("#div-participantes").hide();
        $("#div-taller").show();
    });
    $('#programas').on('click', function(){
        $('li').removeClass('is-active');
        $(this).addClass('is-active')
        
        $("#div-resumenes").hide();
        $("#div-participantes").hide();
        $("#div-taller").hide();
        $("#div-prog").show();

    });
    $('#resumenes').on('click', function(){
        $('li').removeClass('is-active');
        $(this).addClass('is-active')
        
        $("#div-taller").hide();
        $("#div-participantes").hide();
        $("#div-prog").hide();
        $("#div-resumenes").show();
    });
    $('#participantes').on('click', function(){
        $('li').removeClass('is-active');
        $(this).addClass('is-active')
        
        $("#div-taller").hide();
        $("#div-resumenes").hide();
        $("#div-prog").hide();
        $("#div-participantes").show();
    });

    $('#delete-taller').on('click', function(){
        var id = $(this).attr('rel');
        var parameters = {'action':'eliminar','pk': parseInt(id)}
        confirm(window.location.pathname, 'Advertencia','Estas seguro que deseas eliminar este taller?','warning' ,parameters, function(){
            Swal.fire({
                title : 'Notificación!',
                text : 'Taller ha sido eliminado correctamente',
                icon: 'success',
                timer: 3000,
                onClose: () => {
                    location.href= '/dashboart/talleres/list_talleres/';
                }

            });

        });
    });

});

