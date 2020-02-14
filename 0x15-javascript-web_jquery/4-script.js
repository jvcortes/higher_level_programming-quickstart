$('DIV#toggle_header').click(function () {
  let header = $('HEADER');
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  }
});
