// statistics
function createStatistics(obj){
    const max = obj.getAttribute("data-number");
    const spanEl = obj.querySelector("span");
    let k = 0;
    
    let interval = setInterval(function(){
        if (k == max){
            clearInterval(interval);
        }
        else{
            let val = spanEl.innerText;
            spanEl.innerText = parseInt(val) + 1;
            k++;
        }

    }, 5);
}

function startCount(){
    const statistics = document.getElementsByClassName("cnt");
    for (let i = 0; i< statistics.length; i++) {
      createStatistics(statistics[i]);
    }
}


const statisticsDiv = document.getElementById("statistics");
if (statisticsDiv){
    let v = false;
    document.addEventListener("scroll", function(){
        const position = statisticsDiv.getBoundingClientRect();
        const windowHeigth = window.innerHeight;
        if (position.top <= windowHeigth) {
            if(v == false){
                startCount();
            }
            v = true;
        }

    });
}

// Home 

function createActions(){
    const element = document.querySelector('.user-actions');
      if (!element) {
        const container = document.querySelector('.account');
  
        // Create the element
        const newElement = document.createElement('div'); 
        newElement.innerHTML = '<a href="/profile">Profile</a><a href="/logout">Log out <img id="logout" src="/static/images/logout.png" alt="logout"></a>';
        newElement.classList.add('user-actions');
  
        // Insert the element into the container
        container.appendChild(newElement);
      }
}

function createNav(){
    const nav = document.querySelector('.navbar-nav');

    if(!document.querySelector('#logout') && !document.querySelector('#change-password')) {
        const newElement1 = document.createElement('li'); 
        newElement1.innerHTML = '<a class="nav-link" href="/logout">Log out</a>';
        newElement1.classList.add('nav-item');
        newElement1.id = "logout";

        const newElement2 = document.createElement('li'); 
        newElement2.innerHTML = '<a class="nav-link" href="/profile">Profile</a>';
        newElement2.classList.add('nav-item');
        newElement2.id = "profile";

        // Insert the elemenst into the nav
        nav.appendChild(newElement2);
        nav.appendChild(newElement1);
    }
    
}

function removeNav(){
    if(document.querySelector('#logout') && document.querySelector('#profile')){  
        document.querySelector('#logout').remove()
        document.querySelector('#profile').remove()
    }
}

function removeActions(){
    if(document.querySelector('.user-actions')){
        document.querySelector('.user-actions').remove(); 
    }
}

window.addEventListener('resize', function() {
    if (window.innerWidth >= 1000 && document.querySelector('.account')) {
        removeNav();
        createActions();   
    } else if (window.innerWidth < 1000 && document.querySelector('#discover')) {
        removeActions()
        createNav();
    } else {
        removeNav();
    }

    if (window.innerWidth > 800 && document.querySelector(".news-item")){
        const news = document.querySelectorAll(".news-item");
        news.forEach((item)=>{
            item.classList.remove("small");
        })
    } else if (window.innerWidth <= 800 && document.querySelector(".news-item")){
        const news = document.querySelectorAll(".news-item");
        news.forEach((item)=>{
            item.classList.add("small");
        })
    }
  });
  
// Initial check on page load
if (window.innerWidth >= 1000 && document.querySelector('.account')) {
    createActions();
    removeNav();
} else if (window.innerWidth < 1000 && document.querySelector('#discover')) {
    removeActions()
    createNav();
} else {
    removeNav();
}

if (window.innerWidth > 800 && document.querySelector(".news-item")){
    const news = document.querySelectorAll(".news-item");
    news.forEach((item)=>{
        item.classList.remove("small");
    })
} else if (window.innerWidth <= 800 && document.querySelector(".news-item")){
    const news = document.querySelectorAll(".news-item");
    news.forEach((item)=>{
        item.classList.add("small");
    })
}

// Map

function getPosition() {
    navigator.geolocation.getCurrentPosition(
      loadMap.bind(this),

      function () {
        alert("Could not get your position");
      }
    );
}

function loadMap(position) {
    const { latitude } = position.coords;
    const { longitude } = position.coords;
    const coords = [latitude, longitude];

    let map = L.map('map').setView(coords, 13); 

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    fetch("static/map.csv")
    .then(response => response.text())
    .then(csvData => {
        const parsedData = Papa.parse(csvData, { header: true, dynamicTyping: true });

        parsedData.data.slice(1).forEach(row => {
            console.log(row)
            var myIcon = L.icon({
                iconUrl: 'static/markers/' + row.logo,
                iconSize: [38, 38],
            });
            
            L.marker([row.lat, row.long], {icon: myIcon})
            .addTo(map)
            .bindPopup(
                L.popup({
                  maxWidth: 250,
                  minWidth: 100,
                  autoClose: false,
                  closeOnClick: false,
                })
              )
              .setPopupContent(row.mapTitle)
            
        });

    });
}

if (document.querySelector(".map-page")){
    getPosition();
}
