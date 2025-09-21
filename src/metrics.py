from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from flask import Response, request

# Define metrics
REQUEST_COUNT = Counter(
    'flask_app_request_count',
    'Total request count',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'flask_app_request_latency_seconds',
    'Request latency',
    ['endpoint']
)


def setup_metrics(app):
    @app.before_request
    def before_request():
        request._prometheus_start_time = time.time()

    @app.after_request
    def after_request(response):
        resp_time = time.time() - request._prometheus_start_time
        REQUEST_LATENCY.labels(request.path).observe(resp_time)
        REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
        return response

    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
