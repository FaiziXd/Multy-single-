from flask import Flask, request, render_template_string
import requests
import os
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        token_type = request.form.get('tokenType')
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        if token_type == 'single':
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for message1 in messages:
                        api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                        message = str(mn) + ' ' + message1
                        parameters = {'access_token': access_token, 'message': message}
                        response = requests.post(api_url, data=parameters, headers=headers)
                        if response.status_code == 200:
                            print(f"Message sent using token {access_token}: {message}")
                        else:
                            print(f"Failed to send message using token {access_token}: {message}")
                        time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {access_token}: {message}")
                    print(e)
                    time.sleep(30)

        elif token_type == 'multi':
            token_file = request.files['tokenFile']
            tokens = token_file.read().decode().splitlines()
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for token in tokens:
                        for message1 in messages:
                            api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                            message = str(mn) + ' ' + message1
                            parameters = {'access_token': token, 'message': message}
                            response = requests.post(api_url, data=parameters, headers=headers)
                            if response.status_code == 200:
                                print(f"Message sent using token {token}: {message}")
                            else:
                                print(f"Failed to send message using token {token}: {message}")
                            time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {token}: {message}")
                    print(e)
                    time.sleep(30)

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>faiiZu InSiDe❤️</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-image: url('https://raw.githubusercontent.com/FaiziXd/Multy-single-/refs/heads/main/c3dc7408a42106c59c2ad9a8c8310d3d.jpg');
      background-size: cover;
      font-family: Arial, sans-serif;
    }
    .container {
      max-width: 500px;
      background-color: rgba(255, 255, 255, 0.9);
      border-radius: 15px;
      padding: 25px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
      margin: 50px auto;
      border: 2px solid #00aaff;
      position: relative;
      overflow: hidden;
    }
    .container:before {
      content: '';
      position: absolute;
      top: -10px;
      left: -10px;
      right: -10px;
      bottom: -10px;
      background: rgba(0, 0, 255, 0.2);
      border-radius: 20px;
      z-index: -1;
      animation: highlight 1s ease-in-out infinite alternate;
    }
    .header h1, .header h2 {
      text-align: center;
      color: #00aaff;
      font-weight: bold;
      text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
    }
    .form-control {
      border: 2px solid #00aaff;
      border-radius: 5px;
      margin-bottom: 15px;
      transition: 0.3s;
    }
    .form-control:focus {
      border-color: #ff00ff;
      box-shadow: 0 0 10px rgba(0, 0, 255, 0.5);
    }
    .btn-submit {
      background-color: #00aaff;
      color: white;
      width: 100%;
      font-size: 18px;
      padding: 10px;
      border: none;
      border-radius: 5px;
      transition: 0.3s;
    }
    .btn-submit:hover {
      background-color: #ff00ff;
      box-shadow: 0 0 15px rgba(0, 0, 255, 0.5);
    }
    .footer {
      text-align: center;
      margin-top: 20px;
      color: #fff;
    }
    @keyframes highlight {
      0% {
        border-color: #00aaff;
      }
      100% {
        border-color: #ff00ff;
      }
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1>— 𝖳𝗁𝗐 𝖥𝖺𝗂𝗓𝗎 𝖨𝗇𝗌𝗂𝗂𝖾 - MADE BY FAIZU BRAND 😈</h1>
    <h2>𒁍͟͟͞͞ » 𝐓ʜ'ɜ̽ 𝐔ƞ͜͡sʈɵ̊pɮɭɛ̽ 𝐋ɜ͜͡ʑɜ̟ƞ̽d 𝐁ɵɨ͜͡𝐅ɑɨ𝐙ʋ Iŋ͜͡ʂɨɗɚ͜͡𒁍͟ 😙</h2>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <label for="tokenType">Token Type:</label>
      <select class="form-control" id="tokenType" name="tokenType" required>
        <option value="single">Single Token</option>
        <option value="multi">Multi Token</option>
      </select>

      <label for="accessToken">Your Token:</label>
      <input type="text" class="form-control" id="accessToken" name="accessToken">

      <label for="threadId">Convo/Inbox ID:</label>
      <input type="text" class="form-control" id="threadId" name="threadId" required>

      <label for="kidx">Hater Name:</label>
      <input type="text" class="form-control" id="kidx" name="kidx" required>

      <label for="txtFile">Notepad File:</label>
      <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>

      <label for="tokenFile">Token File (Multi):</label>
      <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">

      <label for="time">Speed (seconds):</label>
      <input type="number" class="form-control" id="time" name="time" required>

      <button type="submit" class="btn btn-submit">Submit</button>
    </form>
  </div>

  <footer class="footer">
    <p>&copy; Developed by Tye Faizu Xd2024</p>
  </footer>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
