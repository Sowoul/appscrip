import time
import logging
logger = logging.getLogger("latency")
class LatencyLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = (time.time() - start) * 1000  # ms
        logger.info(f"[LatencyLogger] {request.method} {request.path} took {int(duration)}ms")
        return response
