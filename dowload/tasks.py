import yt_dlp
import os
import smtplib
from email.message import EmailMessage

def download_and_convert_to_mp3(url, output_directory="download", download_options=None):
    if download_options is None:
        download_options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        }

    with yt_dlp.YoutubeDL(download_options) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', 'video')

        ydl.download([url])

    return os.path.join(output_directory, f"{video_title}.mp3")

def send_email(subject, body, to_email, attachment_path, email_options=None):
    if email_options is None:
        email_options = {
            'server': 'smtp.gmail.com',
            'port': 587,
            'username': 'bagget7777@gmail.com',
            'password': 'akyc nkta jcxl ausz',
        }

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'bagget7777@gmail.com'
    msg['To'] = to_email

    with open(attachment_path, 'rb') as file:
        msg.add_attachment(file.read(), maintype='audio', subtype='mp3', filename=os.path.basename(attachment_path))

    server = smtplib.SMTP(email_options['server'], email_options['port'])
    server.starttls()
    server.login(email_options['username'], email_options['password'])
    server.send_message(msg)
    server.quit()
