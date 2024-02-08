# Daily News Email API
The Daily News Email API is a simple yet powerful tool designed to deliver curated news content directly to users' email inboxes on a daily basis. With seamless integration into your application or website, this API enables you to keep your users informed and engaged with the latest updates from their favorite sources.

# Installation
1. Clone the repository:

    ```shell
    https://github.com/NithishM13/Daily-Email-News-API
    ```

2. Navigate to the project directory


3. Install the below mentioned libraries
    ```shell
   pip install requests
   pip install send_email
   pip install smtplib
   pip instal ssl
   ```
   
# Usage
### Whenever the main.py file is run an email will be sent to the mail-id mentioned in send_mail.py file. This app requires an username(sender email address) and gmail app password.
#### You can generate app password for your gmail account by 
#### - visiting google account security settings
#### - security -> 2-Step Verification -> App passwords
#### Under app password generate your own password.
```plaintext
    username = your-email@example.com
    password = your-gmail-app-password
    receiver = receiver-email@example.com
```

