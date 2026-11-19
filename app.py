"""A small HTTP service that returns static Dota 2 hero builds."""

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from urllib.parse import parse_qs, urlparse

from config import BUILDS, HEROES_BY_ATRIBUTE


class BuildHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802 - required by BaseHTTPRequestHandler
        request = urlparse(self.path)
        if request.path == "/health":
            self._send_json(HTTPStatus.OK, {"status": "ok"})
        elif request.path == "/build":
            hero = parse_qs(request.query).get("hero", ["axe"])[0].lower()
            build = BUILDS.get(hero)
            if build:
                self._send_json(HTTPStatus.OK, build)
            else:
                self._send_json(
                    HTTPStatus.NOT_FOUND,
                    {"error": "Hero build not found", "available_heroes": sorted(BUILDS)},
                )
        elif request.path == "/heroes":
            attribute = parse_qs(request.query).get("attribute", [None])[0]
            if attribute is None:
                self._send_json(HTTPStatus.OK, HEROES_BY_ATTRIBUTE)
            elif attribute in HEROES_BY_ATTRIBUTE:
                self._send_json(HTTPStatus.OK, {attribute: HEROES_BY_ATTRIBUTE[attribute]})
            else:
                self._sent_json(
                    HTTPStatus.BAD_REQUEST,
                    {
                        "error": "Unknown attribute",
                        "available_attributes": sorted(HEROES_BY_ATTRIBUTE),
                    },
                )
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
    server = ThreadingHTTPServer((host, port), BuildHandler)
    print(f"Dota Hero Builds service is running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
