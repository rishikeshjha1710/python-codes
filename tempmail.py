import requests
import time

class TemporaryEmail:
    def __init__(self, domain='guerrillamail.com'):
        self.base_url = f'https://www.1secmail.com/api/v1/?action='
        self.domain = domain
        self.email_address = None
        self.emails = []

    def generate_email_address(self):
        response = requests.get(self.base_url + 'genRandomMailbox&count=1&domain=' + self.domain)
        if response.status_code == 200:
            data = response.json()
            self.email_address = data[0]['email']
            print(f"Your temporary email address is: {self.email_address}")
        else:
            print("Failed to generate email address.")

    def fetch_emails(self):
        if self.email_address is None:
            print("Please generate an email address first.")
            return

        response = requests.get(self.base_url + 'getMessages&login=' + self.email_address.split('@')[0] + '&domain=' + self.domain)
        if response.status_code == 200:
            self.emails = response.json()
            if len(self.emails) == 0:
                print("No emails found.")
            else:
                for email in self.emails:
                    print(f"From: {email['from']}")
                    print(f"Subject: {email['subject']}")
                    print(f"Body: {email['body']}")
                    print("------")
        else:
            print("Failed to fetch emails.")

    def main(self):
        self.generate_email_address()
        time.sleep(5)  # Wait for a few seconds before fetching emails
        self.fetch_emails()

if __name__ == "__main__":
    temp_email = TemporaryEmail()
    temp_email.main()
