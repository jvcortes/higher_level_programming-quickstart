$.get('https://swapi.co/api/people/5/?format=json',
  function (response, status) {
    $('DIV#character').text(response.name);
  }
);
