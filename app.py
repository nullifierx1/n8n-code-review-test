"""A tiny HTTP service that returns a random focus tip."""

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import random


TIPS = [
    "Start with the smallest useful step.",
    "Turn off one distraction for the next 25 minutes.",
    "Write down the next action before taking a break.",
]


class TipHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802 - required by BaseHTTPRequestHandler
        if self.path == "/health":
            self._send_json(HTTPStatus.OK, {"status": "ok"})
        elif self.path == "/tip":
            self._send_json(HTTPStatus.OK, {"tip": random.choice(TIPS)})
        else:
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "Not found"})

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        """Keep the demo service output quiet."""


def run(host="127.0.0.1", port=8000):
    server = ThreadingHTTPServer((host, port), TipHandler)
    print(f"Focus Tips service is running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
