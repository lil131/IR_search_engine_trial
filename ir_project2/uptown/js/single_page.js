const movie = {
    id: "00000",
    name: "Title",
    rating: "9.0",
    description: "one long sentence",
    storyline: "storyline xxx",
    imdbURL: "https://www.google.com",
    poster: "images/image_1.jpg",
};


const poster = document.getElementById("poster");
// console.log(movieList);
function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}

const para = window.location.search.substring(1);

fetch("http://0.0.0.0:5000/searchone/" + para)
    .then((res) => res.json())
    .then(function(data) {
        let movie = data;
        console.log(movie)
        const movieInfo = document.getElementById("movie-info");
        let h2 = createNode('h2');
        h2.innerHTML = movie.name;
        append(movieInfo, h2);
        let p1 = createNode("p");
        p1.innerHTML = "Rating: " + movie.rating;
        append(movieInfo, p1);
        let p2 = createNode("p");
        p2.innerHTML = "Description: ";
        append(movieInfo, p2);
        let p_des = createNode("p");
        p_des.innerHTML = movie.description;
        append(movieInfo, p_des);
        let p3 = createNode("p");
        p3.innerHTML = "Storyline: ";
        append(movieInfo, p3);
        let p_sl = createNode("p");
        p_sl.innerHTML = movie.storyline;
        append(movieInfo, p_sl);
        let p4 = createNode("p");
        let a = createNode("a");
        a.innerHTML = "IMDb Link";
        a.href = movie.imdbURL;
        append(p4, a);
        append(movieInfo, p4);

        document.getElementById("poster").src = movie.poster;
    })
    .catch(function(error) {
        console.log(error);
    });