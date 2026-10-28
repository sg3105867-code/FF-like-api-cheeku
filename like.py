from http.server import BaseHTTPRequestHandler
import json
import requests

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

            jwt_token = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjMiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjoxNjY3MzI1NjM5MSwibmlja25hbWUiOiJmQ0JtYTJBSE9pdzMiLCJub3RpX3JlZ2lvbiI6IklORCIsImxvY2tfcmVnaW9uIjoiSU5EIiwiZXh0ZXJuYWxfaWQiOiJhMzhlOTFlMmJhYzk1ZWI0ZGY2NzBkNGFkNjY4NWU0NyIsImV4dGVybmFsX3R5cGUiOjMsInBsYXRfaWQiOjAsImNsaWVudF92ZXJzaW9uIjoiIiwiY2xpZW50X3ZlcnNpb25fY29kZSI6IiIsImVtdWxhdG9yX3Njb3JlIjoxMDAsImlzX2VtdWxhdG9yIjp0cnVlLCJjb3VudHJ5X2NvZGUiOiJVUyIsImV4dGVybmFsX3VpZCI6OTIyMzM5MDA3NTcxOTM2NzcyOSwicmVnX2F2YXتابciOjEwMjAwMDAwNywic291cmNlIjowLCJsb2NrX3JlZ2lvbl90aW1lIjoxNzg1MzQyNzM2LCJjbGllbnRfdHlwZSI6MSwic2lnbmF0dXJlX21kNSI6IiIsInVzaW5nX3ZlcnNpb24iOjAsInJlbGVhc2VfY2hhbm5lbCI6IiIsInJlbGVhc2VfdmVyc2lvbiI6Ik9CNTUiLCJleHAiOjE3OTMyMjY2MDZ9.z3xrO9gO-UbqfaQHefJB2g63oqkSXcNlX_69TTkvl_s"

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
        self.wfile.write("Free Fire Like API is Running on Vercel!".encode('utf-8'))
          
