import re
pattern = r"\+91[\s-]*\d{10}"

text = '''In the bustling tech hubs of Bangalore and Gurgaon, communication is key. If you are trying to reach our corporate office, you can dial +91-9876543210 or contact our support lead at 09123456789. We also have several regional representatives available:

Mumbai Office: +91 22 2345 6789 (Landline)

Delhi Representative: 99887-76655

Chennai Support: +919000012345

Kolkata Branch: (033) 2465-1122

During our recent recruitment drive, we received several applications with different contact formats. For instance, Rajesh prefers using the standard international format +91 70123 45678, while Priya listed her number as 918887776665 without any symbols. In some older database entries, you might even find formats like +91-11-4567-8901 or mobile numbers written with spaces: 9444 555 666.'''

results = re.findall(pattern , text)
print(results)