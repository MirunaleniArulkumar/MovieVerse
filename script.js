console.log("Movie Search Engine Loaded!");
// Getting HTML elements
const searchButton = document.getElementById("search-btn");
const movieInput = document.getElementById("movie-input");
const movieResult = document.getElementById("movie-result");
let currentSearch = "";

// Function to search a movie
function searchMovie() {

    let movieName = movieInput.value;
    currentSearch = movieName;
    movieResult.innerHTML = `
        <div class = "loading">
            Searching....
        </div>
    `;

    // Check if input is empty
    if (movieName.trim() === "") {
        movieResult.innerHTML = `
            <div class="movie-card">
                <h2>Please enter a movie name</h2>
            </div>
        `;
        return;
    }
    movieResult.innerHTML = `
        <div class = "movie-card">
            <h2>Searching...</h2>
        </div>
    `;
    
    fetch(`https://www.omdbapi.com/?apikey=bac9ddd7&s=${movieName}`)
        .then(function(response) {
            return response.json();
        })
        .then(function(movie) {

            if (movie.Response === "True") {

    movieResult.innerHTML = "";

    movie.Search.forEach(function(item) {

        movieResult.innerHTML += `
            <div class="movie-card" 
onclick="getMovieDetails('${item.imdbID}')">
                <button id = "back-btn">Back to Results</button>
                <img src="${item.Poster}" width="180">
                <h2>${item.Title}</h2>
                <p>Year: ${item.Year}</p>
            </div>
        `;

    });

} else {

    movieResult.innerHTML = `
        <div class="movie-card">
            <h2>Movie not found 😢</h2>
        </div>
    `;

}

            // Clear input box
            movieInput.value = "";
        })
        .catch(function() {
            movieResult.innerHTML = `
                <div class="movie-card">
                    <h2>Something went wrong!</h2>
                    <p>Please check your internet connection and try again.</p>
                </div>
            `;
        });
}
function getMovieDetails(imdbID) {

    fetch(`https://www.omdbapi.com/?apikey=bac9ddd7&i=${imdbID}`)
        .then(function(response) {
            return response.json();
        })
        .then(function(movie) {

            movieResult.innerHTML = `
                <div class="movie-card">

                    <button id="back-btn">⬅ Back to Results</button>

                    <img src="${movie.Poster}" width="220">

                    <h2>${movie.Title}</h2>

                    <p><strong>⭐ IMDb Rating:</strong> ${movie.imdbRating}</p>

                    <p><strong>🎭 Genre:</strong> ${movie.Genre}</p>

                    <p><strong>🎬 Director:</strong> ${movie.Director}</p>

                    <p><strong>👥 Actors:</strong> ${movie.Actors}</p>

                    <p><strong>🌍 Language:</strong> ${movie.Language}</p>

                    <p><strong>📅 Released:</strong> ${movie.Released}</p>

                    <p><strong>⏱ Runtime:</strong> ${movie.Runtime}</p>

                    <p><strong>📝 Plot:</strong> ${movie.Plot}</p>

                </div>
            `;

            document.getElementById("back-btn").addEventListener("click", function() {

                movieInput.value = currentSearch;

                searchMovie();

            });

        });

}
// Search when button is clicked
searchButton.addEventListener("click", searchMovie);

// Search when Enter key is pressed
movieInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        searchMovie();
    }
});