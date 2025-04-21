import re
text = "Contact us at help@example.com or admin@school.edu for support."

# TODO: Write a regex pattern to extract emails
pattern = r'[\w.%+-]+@[\w.-]+\.[\w]'
matches = re.findall(pattern, text)
print(matches)
