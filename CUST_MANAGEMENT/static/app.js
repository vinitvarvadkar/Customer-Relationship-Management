var message_timeout = document.getElementById('message-timer')

setTimeout(function()
{
    // message_timeout.style.display ='none';

}, 2000)


document.addEventListener('DOMContentLoaded', function () {
    var message_timeout = document.getElementById('message-timer');

    if (message_timeout) {
        setTimeout(function () {
            message_timeout.style.transition = 'opacity 0.5s';
            message_timeout.style.opacity = '0';

            setTimeout(function () {
                message_timeout.style.display = 'none';
            }, 500); // Match the transition duration
        }, 2000);
    }
});




