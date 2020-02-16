$.get('https://swapi.co/api/films/?format=json',
  function (response, status) {
    for (const film of response.results) {
      $('UL#list_movies').append($('<li></li>').text(film.title));
    }
  }
);
