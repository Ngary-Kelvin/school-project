from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store quotations
quotations = []

# Dictionary to store client data
clients = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/maasai_mara')
def maasai_mara():
    # Route for Maasai Mara page
    return render_template('maasai_mara.html')

@app.route('/lake_nakuru')
def lake_nakuru():
    # Route for Lake Nakuru page
    return render_template('lake_nakuru.html')

@app.route('/oldonyo_sabuk')
def oldonyo_sabuk():
    # Route for Oldonyo Sabuk page
    return render_template('oldonyo_sabuk.html')

@app.route('/tsavo')
def tsavo():
    # Route for Tsavo page
    return render_template('tsavo.html')

@app.route('/generate_quotation', methods=['GET', 'POST'])
def generate_quotation_form():
    if request.method == 'POST':
        park_choice = request.form['park_choice']
        num_people = int(request.form['num_people'])
        num_days = int(request.form['num_days'])
        accommodation_choice = request.form['accommodation_choice']
        transportation_choice = request.form['transportation_choice']
        ages = [int(request.form[f'age{i}']) for i in range(1, 6) if request.form.get(f'age{i}')]

        quotation = generate_quotation_text(park_choice, num_people, num_days, accommodation_choice, transportation_choice, ages)
        
        # Store the quotation in the list
        quotations.append(quotation)

        return render_template('success.html', quotation=quotation)
        
    return render_template('generate_quotation.html')



# Display the client registration form
@app.route('/client_registration', methods=['GET', 'POST'])
def show_registration_form():
    return render_template('client_registration.html')

# Process client registration and store client details
@app.route('/register_client', methods=['POST'])
def register_client():
    # Generate a unique client_id (you can use a UUID or any unique identifier)
    client_id = generate_client_id()

    if request.method == 'POST':
        # Get client registration data from the form
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        national_id = request.form['national_id']
        nationality = request.form['nationality']
        # Other registration data...

        # Store client details in the dictionary using client_id as the key
        clients[client_id] = {
            "Name": name,
            "Phone_number": phone_number,
            "Email": email,
            "Password": password,
            "Gender": gender,
            "National ID / Passport": national_id,
            "Nationality": nationality,
            # Other client details...
        }

        # Redirect to the client details page after registration
        clients[client_id] = client_id

        return redirect(url_for('client_details', client_id=len(clients) - 1))
    # Handle GET request to display the registration form
    return render_template('registration_form.html')

@app.route('/client_details/<int:client_id>')
def client_details(client_id):
    # Display client details for a specific client ID
    client = clients.get(client_id)
    if client:
        return render_template('client_details.html', client=client)
    else:
        return "Client not found."


@app.route('/quotations')
def list_quotations():
    # Display a list of quotations
    return render_template('quotations.html', quotations=quotations)


# Generate a unique client ID
def generate_client_id():
    # Replace this with your logic to generate a unique client ID
    # For example, you can use UUID4 or increment a counter
    # Here, we are using a simple counter for demonstration purposes.
    if 'client_id_counter' not in app.config:
        app.config['client_id_counter'] = 1  # Initialize the counter

    # Increment the counter and use it as the client ID
    client_id = app.config['client_id_counter']
    app.config['client_id_counter'] += 1

    return client_id


def generate_quotation_text(park_choice, num_people, num_days, accommodation_choice, transportation_choice, ages):
    # Calculate the quotation based on the received data
    # Define costs for accommodation and transportation
    accommodation_costs = {
        "Luxury Lodges": 15000,
        "Tented Camps": 9000,
        "Budget Camps": 5000,
    }
    transportation_costs = {
        "Private Safari Vehicle": 3000,
        "Shared Safari Vehicle": 1000,
    }
    accommodation_cost = accommodation_costs.get(accommodation_choice, 0)
    transportation_cost = transportation_costs.get(transportation_choice, 0)

    total_cost = (accommodation_cost + transportation_cost) * num_people * num_days

    quotation = f"Quotation for {num_people} people for {num_days} days at {park_choice} ({num_people} x {num_days} days):\n"
    quotation += f"Accommodation: {accommodation_cost} Ksh per day\n"
    quotation += f"Transportation: {transportation_cost} Ksh per day\n"
    quotation += f"Total Cost: {total_cost} Ksh\n"

    for i, age in enumerate(ages, start=1):
        if age < 7:
            quotation += f"Person {i} (Age {age}): Free accommodation\n"
        else:
            quotation += f"Person {i} (Age {age}): Additional accommodation cost for adults\n"

    return quotation


if __name__ == '__main__':
    app.run(debug=True)
