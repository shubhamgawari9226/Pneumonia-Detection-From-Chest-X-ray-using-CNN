let imagePreview = document.getElementById('image-preview');
let imageDisplay = document.getElementById('image-display');
let uploadCaption = document.getElementById('upload-caption');
let predResult = document.getElementById('pred-result');
let loader = document.getElementById('loader');

document.getElementById('file-upload').addEventListener('change', function (e) {
    let file = e.target.files[0];
    if (file) {
        let reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.src = e.target.result;
            imageDisplay.src = e.target.result;
            imagePreview.classList.remove('hidden');
            uploadCaption.classList.add('hidden');
            predResult.classList.add('hidden');
        };
        reader.readAsDataURL(file);
    }
});

function submitImage() {
    let fileInput = document.getElementById('file-upload');

    if (!fileInput.files[0]) {
        alert('Please select an image first!');
        return;
    }

    let reader = new FileReader();
    reader.onload = function (e) {
        let imageData = e.target.result;

        // Show loader
        loader.classList.remove('hidden');
        predResult.classList.add('hidden');

        // Send to server
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(imageData)
        })
            .then(response => response.json())
            .then(data => {
                // Hide loader
                loader.classList.add('hidden');

                // Show result
                predResult.textContent = `Prediction: ${data.result}`;
                predResult.classList.remove('hidden', 'result-normal', 'result-pneumonia');

                if (data.result === 'NORMAL') {
                    predResult.classList.add('result-normal');
                } else {
                    predResult.classList.add('result-pneumonia');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                loader.classList.add('hidden');
                predResult.textContent = 'Error occurred during prediction';
                predResult.classList.remove('hidden', 'result-normal', 'result-pneumonia');
                predResult.style.backgroundColor = '#f8d7da';
                predResult.style.color = '#721c24';
            });
    };

    reader.readAsDataURL(fileInput.files[0]);
}

function clearImage() {
    document.getElementById('file-upload').value = '';
    imagePreview.classList.add('hidden');
    imageDisplay.src = '';
    uploadCaption.classList.remove('hidden');
    predResult.classList.add('hidden');
    loader.classList.add('hidden');
}