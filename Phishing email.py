# First, we import something called "re", which helps us find patterns in text
import re

# We are creating a function (a reusable block of code) called "is_phishing_email"
# This function will help us figure out if an email is trying to trick us (phishing)
def is_phishing_email(email_text):

    # This is a list of sneaky or scary words bad people often use in fake emails
    phishing_keywords = ["urgent", "verify your account", "password expired", "click here"]

    # This pattern helps us find links (like https://example.com) in the email
    url_pattern = r'(https?://\S+)'

    # This line finds all the links in the email and puts them in a list called 'urls'
    urls = re.findall(url_pattern, email_text)

    # We start with 0 signs that this is a phishing email
    signs_count = 0

    # Now we go through each word in our phishing keywords list
    for keyword in phishing_keywords:
        # We make the email lowercase so we don't miss any keyword (like "Urgent" vs "urgent")
        # If the keyword is found in the email, we add 1 to the signs_count
        if keyword in email_text.lower():
            signs_count += 1

    # If there is at least one link in the email, we also add 1 to the signs_count
    if urls:
        signs_count += 1

    # If there are 2 or more suspicious signs, we say it's probably phishing (a fake email)
    return signs_count >= 2

# This is where we test the function with a pretend email
email_text = "This is an urgent message. Please click here to verify your account."

# We print "Phishing Likely" if our function thinks it's a fake email,
# otherwise we say "Not Phishing"
print("Phishing Likely" if is_phishing_email(email_text) else "Not Phishing")
