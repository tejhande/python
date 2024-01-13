import sqlite3
import re

# Connect to the "History" file in the default Google Chrome profile folder
conn = sqlite3.connect(r'C:\Users\tejas\AppData\Local\Google\Chrome\User Data\Default\History')

# Create a cursor object to execute SQL statements
c = conn.cursor()

# Print the number of URLs in the "urls" table
num_urls = c.execute('SELECT COUNT(1) FROM urls').fetchone()[0]
print("Number of URLs in history:", num_urls)

# Compile a regular expression pattern to extract the domain name from URLs
domain_pattern = re.compile(r"https?://([^/]+)/")

# Initialize a dictionary to store the frequency count of domain names
domains = {}

# Initialize a flag and an ID variable to start the loop
result = True
last_id = 0

# Loop through the rows in the "urls" table, 1000 rows at a time, starting from the last ID that was processed
while result:
    # Reset the flag and the list of IDs to delete
    result = False
    ids_to_delete = []
    
    # Retrieve 1000 rows at a time, starting from the last ID that was processed
    for row in c.execute('SELECT id, url, title FROM urls WHERE id > ? LIMIT 1000', (last_id,)):
        # Update the flag and the last ID variable
        result = True
        last_id = row[0]
        
        # Extract the domain name from the URL using the regular expression pattern
        match = domain_pattern.search(row[1])
        if match:
            domain = match.group(1)
            domains[domain] = domains.get(domain, 0) + 1
            
            # If the domain name contains "godinabox", add the ID of the row to the list of IDs to delete
            if "godinabox" in domain:
                ids_to_delete.append((row[0],))
    
    # Delete the rows with the IDs in the list from the "urls" table, if there are any
    if ids_to_delete:
        c.executemany('DELETE FROM urls WHERE id=?', ids_to_delete)
        conn.commit()

# Close the database connection
conn.close()

# Sort the domain names by frequency count
sorted_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)

# Print the frequency count of domain names and save it to a text file
with open('domain_count.txt', 'w') as f:
    f.write("Frequency count of domain names:\n")
    for domain, count in sorted_domains:
        f.write(f"{domain}: {count}\n")
        print(domain, count)
