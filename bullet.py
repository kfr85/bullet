import requests
import json
import sys
import os
import settings

def push_message(title, body, token):

	url = "https://api.pushbullet.com/v2/pushes"

	headers = {"content-type": "application/json", "Authorization": 'Bearer '+token}
	data_send = {"type": "note", "title": title, "body": body}

	_r = requests.post(url, headers=headers, data=json.dumps(data_send))

def main():
  token = settings.TOKEN
  if token is None:
    print('Error: configuration["PUSHBULLET_TOKEN"] failed', file=sys.stderr)
    sys.exit(1)

  title = sys.argv[1]
  body = sys.argv[2]

  push_message(title, body, token)

if __name__ == "__main__":
  main()
