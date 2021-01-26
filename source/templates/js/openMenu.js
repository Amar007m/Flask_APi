// this is to open and close the menu on mobile devices

let menu = document.querySelector(".menu");

document.getElementById("dropdown").addEventListener("click", () => {
	menu.style.width = "100%";
});

document.querySelector(".closetbn").addEventListener("click", () => {
	menu.style.width = "0%";
});
