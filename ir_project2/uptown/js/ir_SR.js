// const userQuery = "user query";
// const movie = {
//     id: "00000",
//     name: "Title",
//     rating: "9.0",
//     description: "one long sentence",
//     storyline: "xxx",
//     imdbURL:,
//     poster: "images/image_1.jpg",
// };
// const movies = [movie, movie, movie];


const currentURL = "fashion.html";

const query = window.location.search.substr(1);
console.log("query: " + query)
const decodedQ = decodeURIComponent(query);
console.log("decodedQ: " + decodedQ)
document.getElementById("user-query").value = decodedQ;


function submitQuery() {
    const userQuery = document.getElementById("user-query").value;
    const encodedQuery = encodeURIComponent(userQuery);
    console.log("clicked")
    const redirectURL = currentURL + '?' + encodedQuery;
    console.log("clicked" + redirectURL)
    location.replace(redirectURL);
}

// function processQuery()
//   {
//     var parameter = window.location.search.substr(1); //substr() to rm '?'.
//     var decodedQuery = decodeURIComponent(parameter);
//     document.getElementById("user-query").placeholder = decodedQuery;
//   }


// const url = 'https://randomuser.me/api/?results=10';
// const movie_url = 'xxx/movieID=';
const url = window.location.search;


const movieList = document.getElementById("movie_list");
console.log(movieList);

function createNode(element) {
    return document.createElement(element);
}

function append(parent, element) {
    return parent.appendChild(element);
}
console.log("term" + decodedQ)
fetch("http://0.0.0.0:5000/search/" + decodedQ)
    .then((res) => res.json())
    .then(function(data) {
        let movies = data;

        movies.map(function(movie) {
            console.log(movie); //"http://google.com" //

            movie = JSON.parse(movie)
            console.log(movie.poster)

            let moviePageURL = "single.html?" + movie.id;

            let div1 = createNode('div');
            div1.className = 'col-md-12';
            append(movieList, div1);

            let div2 = createNode('div');
            div2.className = 'blog-entry ftco-animate d-md-flex fadeInUp ftco-animated';
            append(div1, div2);

            let a_img = createNode('a');
            a_img.className = 'img img-2';
            a_img.href = moviePageURL;
            poster_link = movie.poster
            poster_link = poster_link.replace("https", "http");
            a_img.style = 'background-image: url(' + poster_link + ');';
            append(div2, a_img);

            let div3 = createNode('div');
            div3.className = 'text text-2 pl-md-4';
            append(div2, div3);

            let h3 = createNode('h3');
            h3.className = 'mb-2';
            append(div3, h3);

            let a_title = createNode('a');
            a_title.href = moviePageURL;
            a_title.innerHTML = movie.name;
            append(h3, a_title);

            let div4 = createNode('div');
            div4.className = 'meta-wrap';
            append(div3, div4);

            let p1 = createNode('p');
            p1.className = 'meta';
            append(div4, p1);

            let span = createNode('span');
            span.innerHTML = 'Rating: ' + movie.rating;
            append(p1, span);

            let p_imdb = createNode('p');
            p_imdb.className = 'mb-4';
            append(div3, p_imdb);

            let p_more = createNode('p');
            append(div3, p_more);

            let a_btn = createNode('a');
            a_btn.className = 'btn-custom';
            a_btn.href = moviePageURL;
            a_btn.innerHTML = 'Read More >';
            append(p_more, a_btn);

        })
    })
    .catch(function(error) {
        console.log(error);
    });