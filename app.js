function handleClickSearch() {

    const query = d3.select('#search_query').property("value");

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
                console.log(songData)
         

                document.getElementById("search_num").innerHTML = "Your new song recommendation is " + songData['Song'] + " by " + songData['Artist'];
          })

          .catch(function (err) {
            console.log(err);
          });
    }
}
// Attach function to button click
d3. select("#search-btn").on("click", handleClickSearch);
