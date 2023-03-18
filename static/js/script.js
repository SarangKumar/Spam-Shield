const links = document.querySelectorAll('.link');



console.log(links);

for(let i=0; i<links.length; i++) {

    links[i].addEventListener('click', (e)=>{
        // e.preventDefault();
        for(let j=0; j<links[i].length; j++){
            console.log(links[j])
            links[j].classList.remove('active');
        }
        links[i].classList.add('active')
    })
}


