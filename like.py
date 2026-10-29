from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            target_uid = "12557849665"
            if post_data:
                try:
                    data = json.loads(post_data.decode('utf-8'))
                    target_uid = data.get("target_uid", "12557849665")
                except:
                    pass

            jwt_token = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjMiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjoxMjMyNjMyNzU5NCwibmlja25hbWUiOiIwKzJ2YTNGeE5TSTlmaUtFN09JPSIsIm5vdGlfcmVnaW9uIjoiSU5EIiwibG9ja19yZWdpb24iOiJJTkQiLCJleHRlcm5hbF9pZCI6ImY3MTkyOWRkMmUyODU3YzIxZjMwMDY1ZWM4OTBhOTg4IiwiZXh0ZXJuYWxfdHlwZSI6OCwicGxhdF9pZCI6MCwiY2xpZW50X3ZlcnNpb24iOiIiLCJjbGllbnRfdmVyc2lvbl9jb2RlIjoiIiwiZW11bGF0b3Jfc2NvcmUiOjEwMCwiaXNfZW11bGF0b3IiOnRydWUsImNvdW50cnlfY29kZSI6IlVTIiwiZXh0ZXJuYWxfdWlkIjoxMTUzMDAxMzk3ODI4LCJyZWdfYXZhdGFyIjoxMDIwMDAwMDcsInNvdXJjZSI6MCwibG9ja19yZWdpb25fdGltZSI6MTc0OTY1NDcyNCwiY2xpZW50X3R5cGUiOjEsInNpZ25hdHVyZV9tZDUiOiIiLCJ1c2luZ192ZXJzaW9uIjowLCJyZWxlYXNlX2NoYW5uZWwiOiIiLCJyZWxlYXNlX3ZlcnNpb24iOiJPQjU1IiwiZXhwIjoxNzkzMjgyNDYxfQ.mBAfkIg5Yf8RTh43xb2GaQ-jtyymzZ2va5rmx50FyRY"

            api_endpoint = "https://client.ind.freefiremobile.com/LikeProfile"

            headers = {
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Android)",
                "Authorization": f"Bearer {jwt_token}",
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip"
            }

            payload = {
                "target_uid": target_uid,
                "server_name": "ind",
                "region_name": "IN"
            }

            response = requests.post(api_endpoint, json=payload, headers=headers, timeout=10)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            result = {
                "status_code": response.status_code,
                "target_uid": target_uid,
                "response_text": response.text
            }
            self.wfile.write(json.dumps(result).encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_msg = {"status": False, "error": str(e)}
            self.wfile.write(json.dumps(error_msg).encode('utf-8'))

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Free Fire Like API is Running on Render!".encode('utf-8'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), handler)
    print(f"Server running on port {port}")
    server.serve_forever()
          
