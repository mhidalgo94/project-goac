

$("#div-gdiario").show();
$("#gdiario").addClass('is-active');
$("#div-ult30dias").hide();
$("#div-info").hide();


$('#gdiario').on('click', function () {
    $('li').removeClass('is-active');
    $(this).addClass('is-active')
    $("#div-gdiario").show();
    $("#div-ult30dias").hide();
    $("#div-info").hide();
});

$('#ult30dias').on('click', function () {
    $('li').removeClass('is-active');
    $(this).addClass('is-active')
    $("#div-ult30dias").show();
    $("#div-gdiario").hide();
    $("#div-info").hide();
});

$('#info').on('click', function () {
    $('li').removeClass('is-active');
    $(this).addClass('is-active')
    $("#div-info").show();
    $("#div-gdiario").hide();
    $("#div-ult30dias").hide();
});