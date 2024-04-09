import webbrowser
import os

os.system('docker compose -f ".\docker-compose.yml" up -d --build')
webbrowser.open('http://localhost:80')
