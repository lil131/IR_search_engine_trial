const userQuery = "user query";
const movie = {
    movieID: "00000",
    movieName: "Title",
    posterURL: "images/image_1.jpg",
    pulishDate: "2010-10-09",
    rating: "9.0",
    description: "one long sentence",
    director: "xxx",
};
const movies = [movie, movie, movie];


const currentURL = "fashion.html";
const query = window.location.search.substr(1);
const decodedQ = decodeURIComponent(query);
document.getElementById("user-query").placeholder = decodedQ;

function submitQuery(){
  const userQuery = document.getElementById("user-query").value;
  const encodedQuery = encodeURIComponent(userQuery);
  const redirectURL = currentURL + '?' + encodedQuery;
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

// fetch(url)
//   .then((res) => res.json()) 
//   .then(function(data) {
//     let movies = data.results; 
//     return
     movies.map(function(movie) { 
        console.log(movie);
      let div1 = createNode('div');
      div1.className = 'col-md-12';
      append(movieList, div1);

      let div2 = createNode('div');
      div2.className = 'blog-entry ftco-animate d-md-flex fadeInUp ftco-animated';
      append(div1, div2);

      let div3 = createNode('div');
      div3.className = 'text text-2 pl-md-4';

      let div4 = createNode('div'),
          a_img = createNode('a'),
          a_btn = createNode('a'),
          a_title = createNode('a'),
          h3 = createNode('h3'),
          p1 = createNode('p'),
          p_des = createNode('p'),
          p_more = createNode('p'),
          span1 = createNode('span'),
          span2 = createNode('span');
      moviePageURL = url + movie.movieID;
      
      div4.className = 'meta-wrap';
      a_img.className = 'img img-2';
      a_img.href = moviePageURL;
      a_img.style = 'background-image: url(' + movie.posterURL + ');';
      a_btn.className = 'btn-custom';
      a_btn.href = moviePageURL;
      a_btn.innerHTML = 'Read More >';
      h3.className = 'mb-2';
      a_title.href = moviePageURL;
      a_title.innerHTML = movie.movieName;
      p1.className = 'meta';
      p_des.className = 'mb-4';
      p_des.innerHTML = movie.description;
      span1.innerHTML = 'Publish Date: ' + movie.publishDate;
      span2.innerHTML = 'Rating: ' + movie.rating;
      append(p1, span1);
      append(p1, span2);
      append(div4, p1);
      append(h3, a_title);
      append(div3, h3);
      append(div3, div4);
      append(div3, p_des);
      append(p_more, a_btn);
      append(div3, p_more);
      append(div2, a_img);
      append(div2, div3);
      
    })
//     })
//   })
// .catch(function(error) {
//     console.log(error);
//   });