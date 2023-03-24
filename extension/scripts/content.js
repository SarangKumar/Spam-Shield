const article = document.querySelectorAll("article");
console.log('asdf');

// `document.querySelector` may return null if the selector doesn't match anything.
if (article) {
    for (let i = 0; i < article.length; i++) {

        const text = article[i].textContent;
        article[i].style.position = "relative";

        const wordMatchRegExp = /[^\s]+/g; // Regular expression
        const words = text.matchAll(wordMatchRegExp);
        // matchAll returns an iterator, convert to array to get word count
        const wordCount = [...words].length;
        const readingTime = Math.round(wordCount / 200);
        const badge = document.createElement("p");

        // adding styling
        badge.style.cssText = `
        display:flex;
        justify-content:flex-end;
        padding:1rem;
        margin:0;
        position:relative;
        right:0;
        `

        // Use the same styling as the publish information in an article's header
        badge.classList.add("color-secondary-text", "type--caption");
        badge.textContent = `⏱️ ${readingTime} min read`;
        article[i].insertAdjacentElement("beforeend", badge);
    }
}


/*
setTimeout(()=>{
    
    const heading = document.createElement("h1")
    heading.textContent = 'HTMLLL';
    
    document.querySelector('body').insertAdjacentElement('afterbegin', heading)
},5000)
*/



// document.addEventListener("DOMContentLoaded", function () {
// });




// setTimeout(() => {
// }, 10000)



window.onload = () => {
    const mailBox = document.querySelectorAll('div[dir="ltr"]')

    if (mailBox.length > 0) {
        for (let i = 0; i < mailBox.length; i++) {
            const para = document.createElement('p');
            para.textContent = '😎 -from spam-alert';
            console.log(mailBox[i].textContent)

            mailBox[i].insertAdjacentElement('afterend', para);
        }

    }

}