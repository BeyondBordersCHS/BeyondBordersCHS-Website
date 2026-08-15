#!/usr/bin/env python3
"""Local dev server that mimics Vercel's cleanUrls + 404.html behavior.

    python3 serve.py [port]     # default 8000
"""

import sys
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).parent.resolve()


class CleanURLHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = Path(super().translate_path(path))
        # "/about" -> "about.html", matching vercel.json cleanUrls
        if not local.exists() and not local.suffix:
            candidate = local.with_suffix(".html")
            if candidate.is_file():
                return str(candidate)
        return str(local)

    def send_error(self, code, message=None, explain=None):
        page = ROOT / "404.html"
        if code == 404 and page.is_file():
            body = page.read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    handler = partial(CleanURLHandler, directory=str(ROOT))
    print(f"Serving {ROOT} at http://localhost:{port}")
    try:
        HTTPServer(("", port), handler).serve_forever()
    except KeyboardInterrupt:
        pass
