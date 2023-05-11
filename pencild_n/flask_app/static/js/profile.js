const input = document.querySelector('#profile-picture');

input.addEventListener('change', () => {
  const file = input.files[0];
  const formData = new FormData();
  formData.append('profile-picture', file);

  fetch('/user/profile/picture', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    const imageUrl = data.imageUrl;
    const img = document.querySelector('img');
    img.src = imageUrl;
  })
  .catch(error => console.error(error));
});