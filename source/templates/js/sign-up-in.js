// this scrpt will help us to sign in or sign up in case if the user is new to the platform

let signSection = $(`.sign-up`);
const btns = document.querySelectorAll('.btn');

function showSection () {
    signSection.style.width = '100%';  
}

document.querySelector('.closeSection').addEventListener('click', () => {
    signSection.style.width = '0%';
})

btns.forEach((btn) => btn.addEventListener('click', showSection));

