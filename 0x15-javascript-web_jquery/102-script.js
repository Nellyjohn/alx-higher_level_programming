$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.getJSON(apiUrl + '?lang=' + languageCode, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
