
     // Function to dynamically add age input fields
     document.getElementById('addAgeField').addEventListener('click', function () {
        const numPeople = document.getElementById('num_people').value;
        const ageFieldsContainer = document.getElementById('ageFields');
        ageFieldsContainer.innerHTML = ''; // Clear previous fields

        for (let i = 1; i <= numPeople; i++) {
            const ageLabel = document.createElement('label');
            ageLabel.setAttribute('for', `age${i}`);
            ageLabel.textContent = `Age for Person ${i}:`;

            const ageInput = document.createElement('input');
            ageInput.setAttribute('type', 'number');
            ageInput.setAttribute('id', `age${i}`);
            ageInput.setAttribute('name', `age${i}`);

            ageFieldsContainer.appendChild(ageLabel);
            ageFieldsContainer.appendChild(ageInput);
        }
    });

