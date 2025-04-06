# phishing-detector
🛡️ Simple Phishing Email Detector (Python)
This is a basic Python script I wrote to help identify potential phishing emails. It checks for common red flags like suspicious keywords (e.g. "urgent", "verify your account") and the presence of URLs. If it finds multiple warning signs, it flags the email as "Phishing Likely".

The idea behind this project was to get hands-on practice with pattern matching using re (regular expressions), working with strings, and building a simple detection logic. Great for beginners who want to learn how phishing detection works at a basic level.

What It Does:
Scans the email text for trigger words often used in phishing attacks.

Detects any URLs in the message.

Uses a simple scoring system to decide if the message seems suspicious.

Example Output:
If the script finds two or more phishing indicators, it prints:
Phishing Likely
Otherwise:
Not Phishing
