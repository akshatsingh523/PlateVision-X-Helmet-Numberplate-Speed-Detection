document.addEventListener('DOMContentLoaded', function() {

    var images = [
    "{% static 'img/7.jpg' %}",
    "{% static 'img/4.png' %}",
    "{% static 'img/5.webp' %}",
    "{% static 'img/6.webp' %}"
    ];

    function changeBackground() {
        var randomIndex = Math.floor(Math.random() * images.length);
        var randomImage = images[randomIndex];
        document.querySelector('.user-login-wrap').style.backgroundImage = 'url(' + randomImage + ')';
    }
    changeBackground();
    setInterval(changeBackground, 3000); 
});
