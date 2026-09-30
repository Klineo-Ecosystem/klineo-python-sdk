import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from klineo_liquidity_os import LiquidityOsApiError, LiquidityOsClient


class RedirectTests(unittest.TestCase):
    def test_http_redirect_is_not_followed_with_tenant_credentials(self):
        calls = []

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                calls.append(self.path)
                self.send_response(302)
                self.send_header("Location", "/credential-trap")
                self.end_headers()

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            client = LiquidityOsClient(f"http://127.0.0.1:{server.server_port}/api/liquidity-studio/v2", "org", "token")
            with self.assertRaises(LiquidityOsApiError) as caught:
                client.list_scores()
            self.assertEqual(caught.exception.status, 302)
            self.assertEqual(calls, ["/api/liquidity-studio/v2/scores"])
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
