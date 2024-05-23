document.addEventListener('DOMContentLoaded', function() {

    var images = ['../img/7.jpg', '../img/4.png', '../img/5.webp', '../img/6.webp'];

    function changeBackground() {
        var randomIndex = Math.floor(Math.random() * images.length);
        var randomImage = images[randomIndex];
        document.querySelector('body').style.backgroundImage = 'url(' + randomImage + ')';
    }
    changeBackground();
    setInterval(changeBackground, 3000); 
});
