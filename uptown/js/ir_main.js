console.log("test");
const redirectURL = "fashion.html";

// const btn = document.getElementById("submit-btn");
// btn.addEventListener("submit",function(e) {
//     // event.preventDefault();
//     const userQuery = document.getElementById("user-query").value;
//     if (userQuery.length < 1) return;
//     const encodedQuery = encodeURIComponent(userQuery);
//     location.replace(redirectURL + '?' + encodedQuery);
// });

// window.location.href = window.location.href;
function submitQuery(){
    console.log("click")
    const userQuery = document.getElementById("user-query").value;
    
    if (userQuery.length < 1) {
        return;
    }
    const encodedQuery = encodeURIComponent(userQuery);
    window.location.href = redirectURL + '?' + encodedQuery;
}