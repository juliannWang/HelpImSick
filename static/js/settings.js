
    const editEmailBtn = document.querySelector('#edit-email');
    const emailInput = document.querySelector('#email');

    const editPasswordBtn = document.querySelector('#edit-password');
    const passwordInput = document.querySelector('#password');

    const editNameBtn = document.querySelector('#edit-name');
    const nameInput = document.querySelector('#name');

    const editAboutBtn = document.querySelector('#edit-about');
    const aboutInput = document.querySelector('#about');

    const editCountryBtn = document.querySelector('#edit-country');
    const countryInput = document.querySelector('#country');

    const editLanguageBtn = document.querySelector('#edit-language');
    const languageInput = document.querySelector('#language');

    const editImageBtn = document.querySelector('#edit-image');
    const imageInput = document.querySelector('#image');

    editEmailBtn.addEventListener('click', () => {
      emailInput.disabled = false;
      emailInput.focus();
    });

    editPasswordBtn.addEventListener('click', () => {
      passwordInput.disabled = false;
      passwordInput.focus();
    });

    editNameBtn.addEventListener('click', () => {
      nameInput.disabled = false;
      nameInput.focus();
    });

    editAboutBtn.addEventListener('click', () => {
      aboutInput.disabled = false;
      aboutInput.focus();
    });

    editCountryBtn.addEventListener('click', () => {
      countryInput.disabled = false;
      countryInput.focus();
    });

    editLanguageBtn.addEventListener('click', () => {
      languageInput.disabled = false;
      languageInput.focus();
    });

    editImageBtn.addEventListener('click', () => {
      imageInput.click();
    });