const textArea = document.querySelector('#chat-text-area');
const inputFieldEnterKeyPreventVal = document.querySelector('#input');

textArea.addEventListener('click', (e) => {
    // e.preventDefault();
    return false;
});

textArea.addEventListener('keydown', (e) => {
    e.preventDefault();
});


// disable "enter" keypress in input field
// inputFieldEnterKeyPreventVal.bind('keypress', (e) => {
//     if (e.keyCode == 13) {
//         e.preventDefault();
//         return false;
//     }
// });