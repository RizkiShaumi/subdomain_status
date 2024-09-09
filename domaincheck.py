import requests
import csv

# List of subdomains to check
subdomains = [
"absen.garutkab.go.id",
        "satudata.archive.garutkab.go.id",
        "bakesbangpol.garutkab.go.id"
    ]

def check_subdomain(subdomain):
    try:
        response = requests.get(f"http://{subdomain}", timeout=5)
        if response.status_code == 200:
            return 'Active'
        else:
            return 'Inactive'
    except requests.RequestException as e:
        return 'Inactive'

# Open CSV file for writing
try:
    with open('C:/Users/Admin/Documents/Magan/subdomain_status_fix.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subdomain', 'Status'])

        # Check each subdomain and write the result to CSV
        for subdomain in subdomains:
            status = check_subdomain(subdomain)
            writer.writerow([subdomain, status])

    print("Subdomain status has been saved to subdomain_status.csv")

except IOError as e:
    print(f"Error writing to file: {e}")
