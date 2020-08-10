 function image_onchage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#image_preview').attr('src', e.target.result);
            $('#image_preview_block').removeClass('hide');
            $('#image_label').addClass('hide');
        };
        reader.readAsDataURL(input.files[0]);
    }
    else {
        $('#image_preview_block').addClass('hide');
        $('#image_label').removeClass('hide');
    }
}

function close_image() {
    $('#id_image').click();
}
