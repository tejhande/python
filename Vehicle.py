import re
import requests

# Prompt the user to input the registration number
# registration_number = input("Enter the vehicle registration number (e.g., MH14GT7518): ")
registration_number = "MH14GT7518"
# Validate the registration number using a regular expression
# if not re.match(r"^[A-Z]{2}\d{1,2}[A-Z]{1,2}\d{1,4}$", registration_number):
#     print("Invalid registration number. Please enter a valid number in the format 'MH14GT7518'.")
#     exit()

# Set the base URL for the VAHAN API
base_url = "https://vahan.parivahan.gov.in/nrservices/faces/user/citizen/searchstatus.xhtml"

# Send a GET request to the VAHAN API with the registration number
response = requests.get(f"{base_url}api/vehicle_details_with_owner/{registration_number}")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Write the vehicle details to a text file
    with open(f"{registration_number}.txt", "w") as file:
        file.write(f"Vehicle Make: {data['vehicle']['make']}\n")
        file.write(f"Vehicle Model: {data['vehicle']['model']}\n")
        file.write(f"Registration Date: {data['registration']['registeredAt']}\n")
        file.write(f"Owner's Name: {data['owner']['name']}\n")
        file.write(f"Owner's Address: {data['owner']['address']}\n")
        
    print(f"Vehicle details written to {registration_number}.txt")
    
else:
    print(f"Failed to fetch vehicle details for {registration_number}. Error code:", response.status_code)
