from flask import Flask, jsonify
from flask_cors import CORS
from src.routes.auth_routes import bp as auth_bp
from src.routes.metrics_routes import bp as metrics_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(metrics_bp)

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"message": "not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"message": "internal server error"}), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
