"""A small HTTP service with a starter build for the Dota 2 hero Axe."""

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json


AXE_BUILD = {
    "hero": "Axe",
    "role": "Offlane",
    "items": ["Phase Boots", "Blink Dagger", "Blade Mail", "Black King Bar"],
    "skills": ["Berserker's Call", "Battle Hunger", "Counter Helix", "Culling Blade"],
}


class BuildHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802 - required by BaseHTTPRequestHandler
        if self.path == "/health":
            self._send_json(HTTPStatus.OK, {"status": "ok"})
        elif self.path == "/build":
            self._send_json(HTTPStatus.OK, AXE_BUILD)
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
    print(f"Dota Hero Builds service is running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
