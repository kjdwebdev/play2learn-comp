/*
Used this when testing to make sure the quote was changing at the correct interval
setInterval(myTimer, 1000);

function myTimer() {
  const date = new Date();
  document.getElementById("demo").innerHTML = date.toLocaleTimeString();
}
*/

/* 1 second = 1000 milliseconds */
/* Set a timeout, not an interval, every time you call the function. 
Timeouts are executed once. If you set a new interval every time, you'll be piling up function calls exponentially, 
quickly making your page unresponsive by overwhelming the CPU.
*/

let $counter = 0;
$quotes = ["It is engaging, especially when it comes to learning, as I have a very short attention span.--Carolina",
    "I love that my students love it so much! I love that they are able to practice their skills in a fun and easy way.---Ms. Teacher",
    "Math Facts is so much fun to play.---Pete",
    "Math Facts has a great interface for users- it's really easy to use and beginner-friendly.---Mark"];

const $target = document.querySelector('#quote>p');

function quoteLoop(){
    $target.innerHTML=$quotes[$counter];
    /* when you get to the end of the quotes start again */
    if($counter == $quotes.length - 1){
        $counter = 0;
    }
    else {
        $counter++;
    }
    setTimeout(quoteLoop, 10000);
    
}

window.addEventListener("load", quoteLoop);