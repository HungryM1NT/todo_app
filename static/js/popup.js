authShow('form-login', 'form-register', 'switch-button')

initializePopup('login-popup', 'show-login-popup');
initializePopup('note-create-popup', 'show-note-create-popup', 'note-create-cancel');
initializePopup('note-update-popup', null, 'note-update-cancel');

// add fields cleaning after closing 

function authShow(loginId, registerId, buttonClass) {
    const buttons = document.getElementsByClassName(buttonClass)
    const login = document.getElementById(loginId) 
    const register = document.getElementById(registerId)
    
    Array(...buttons).forEach(btn => {
        btn.addEventListener('click', () => {
            login.style.display = login.style.display === 'none' ? 'inline' : 'none'
            register.style.display = register.style.display === 'none' ? 'inline' : 'none'
        })
    })
}
 
function initializePopup(overlayId, popupShowButtonId=null, popupCancelButtonId=null) {
    try {
        const popupShowButton = document.getElementById(popupShowButtonId);

        const popupOverlay = document.getElementById(overlayId) 

        const overlays = document.getElementsByClassName('overlay');

        popupOverlay.addEventListener('click', (event) => {
            if (event.target === popupOverlay) {
                popupOverlay.style.display = 'none';
            }
        });

        let popupCancelButton
        if (popupCancelButtonId) {
            popupCancelButton = document.getElementById(popupCancelButtonId)
            popupCancelButton.addEventListener('click', () => {
                Array(...overlays).forEach(overlay => {
                    overlay.style.display = 'none';
                })
            });
        }

        if (popupShowButton) {
            popupShowButton.addEventListener('click', () => {
                popupOverlay.style.display = 'flex';
            });
        }
    } catch {
        return
    }
}
