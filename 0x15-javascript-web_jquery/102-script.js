// Language translator - greeting
$(document).ready(function() {
  $('#btn_translate').click(function() {
    var languageCode = $('#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode,
      dataType: 'json',
      success: function(data) {
        $('#hello').text(data.hello);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error fetching translation:', textStatus, errorThrown);
        $('#hello').text('Error: Translation failed');
      }
    });
  });
});
