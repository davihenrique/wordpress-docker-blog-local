import webbrowser
import os

from dotenv import load_dotenv
load_dotenv()
WORDPRESS_PORT = os.getenv('WORDPRESS_PORT')
os.system('docker compose -f ".\docker-compose.yml" up -d --build')
webbrowser.open('http://localhost:'+WORDPRESS_PORT)
