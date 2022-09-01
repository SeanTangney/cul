// Code for changing country field placeholder/selected text colour

let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#5caac2');
}
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#6c757d');
    } else {
        $(this).css('color', '#6c757d');
    }
});