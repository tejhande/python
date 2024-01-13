import imaplib

# Connect to the Gmail IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to the Gmail account
mail.login("johnabraham427427@gmail.com", "Ileana Dcruz1")

# Select the mailbox to search in (e.g., "INBOX")
mail.select("INBOX")

# Ask the user for the year
year = input("Enter the year in YYYY format: ")

# Search for all emails marked as spam and older than the specified year
status, email_ids = mail.search(None, f"(X-GM-LABELS 'SPAM' BEFORE {year}-01-01)")
email_ids = email_ids[0].split()

# Delete all the emails
for email_id in email_ids:
    mail.store(email_id, "+FLAGS", "\\Deleted")

# Expunge the deleted emails
mail.expunge()

# Logout from the Gmail account
mail.logout()
