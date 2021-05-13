$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    $.each(data.results, function (index) {
        $("<li> " + data.results[index].title + " </li>").appendTo("UL#list_movies");
    });
});
