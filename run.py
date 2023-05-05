from server.app import app
from server.website import Website
from server.backend import Backend_Api

from json import load
import os

if __name__ == '__main__':
    config = load(open('config.json', 'r'))
    site_config = config['site_config']

    site = Website(app)
    for route in site.routes:
        app.add_url_rule(
            route,
            view_func=site.routes[route]['function'],
            methods=site.routes[route]['methods'],
        )

    backend_api = Backend_Api(app, config)
    for route in backend_api.routes:
        app.add_url_rule(
            route,
            view_func=backend_api.routes[route]['function'],
            methods=backend_api.routes[route]['methods'],
        )

    host = site_config.get('host', '0.0.0.0')
    port = int(os.getenv("PORT", site_config.get('port', 5000)))
    debug = site_config.get('debug', False)

    print(f"Running on {host}:{port}")
    app.run(host=host, port=port, debug=debug)
    print(f"Closing {host}:{port}")
