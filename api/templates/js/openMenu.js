// this is to open and close the menu on mobile devices

let $ = (selector) => document.querySelector(selector); // this is to avoid writing document.querySelector again and again

let menu = $(`.menu`);

document.getElementById("dropdown").addEventListener("click", () => {
	menu.style.width = "100%";
});

document.querySelector(".closetbn").addEventListener("click", () => {
	menu.style.width = "0%";
});
