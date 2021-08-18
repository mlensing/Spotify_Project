function handleClickSearch() {

    const query = d3.select('#search_query').property("value");
    print(query);

    if (query) {
        console.log(query);
        document.getElementById("search_query").placeholder=query;

        var url = "https://spotify-heroku-api.herokuapp.com/api/search/"; 
        var updated_url = url + query;

        fetch(updated_url)
          .then(function (response) {
            return response.json();
          })
          .then(function (data) {

                songData = data;
                buildTable(songData);
                var num_query_results = songData.length;

                document.getElementById("search_num").innerHTML = "Your new song recommendation is " + songData;
          })

          .catch(function (err) {
            console.log(err);
          });
    }
}
// Attach function to button click
d3. select("#search-btn").on("click", handleClickSearch);
