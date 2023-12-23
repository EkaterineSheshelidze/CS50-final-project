/*statistics start*/
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
/*statistics end*/