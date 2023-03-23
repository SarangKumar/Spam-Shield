const databaseFieldCount = document.querySelector("#database-field-count");
const feedbacks = document.querySelector("#feedbacks");
const users = document.querySelector("#users");

fVdatabaseFieldCount = databaseFieldCount.textContent;
fVfeedbacks = feedbacks.textContent;
fVusers = users.textContent;


function increment(selector, finalValue) {
  let i = 0;

  finalValue = Number(finalValue);
  
  let step;
  if (finalValue > 10000) { step = 50; }
  else if (finalValue > 5000) { step = 20; }
  else if (finalValue > 2000) { step = 10; }
  else if (finalValue > 500) { step = 5; }
  else { step = 1; }


  let counter = setInterval(function () {
    selector.textContent = i;
    i += step
    if (i > finalValue) {
      clearInterval(counter);
      selector.innerHTML += "<span class='plus'>+<span>";
    }
  }, 1);
}

// if (window.location.pathname === '/'){
// }
increment(databaseFieldCount, fVdatabaseFieldCount);
increment(feedbacks, fVfeedbacks);
increment(users, fVusers);




