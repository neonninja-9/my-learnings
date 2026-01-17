import re

# Sample text containing various email formats
raw_text = """
Contact our support team at support.portal@company.in or hr@tech-startup.com.
For sales inquiries, email sales_department123@global-solutions.org.
You can also reach out to individual developers: 
gourav.sharma@amity.edu, dev-ops_lead@internal.node.js, or info+newsletter@blog.com.

Invalid emails (should be ignored):
- plainaddress
- #@%^%#$@#$@#.com
- @missingusername.com
- Joe Smith <email@example.com> (should only grab the email part)
"""

def scrape_emails(text):
    # The Regex pattern for emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # findall returns a list of all matches
    found_emails = re.findall(email_pattern, text)
    
    return list(set(found_emails))  # Using set() to remove duplicates

# Execute the scraper
emails = scrape_emails(raw_text)

print(f"Found {len(emails)} valid emails:")
for email in emails:
    print(f" - {email}")