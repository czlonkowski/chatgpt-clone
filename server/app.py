import os
from flask import Flask

app = Flask(__name__, template_folder='./../client/html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1338))
    app.run(host="0.0.0.0", port=port)
