from flask import Blueprint, request, jsonify, g
from datetime import datetime
from src.services.metrics_services import MetricsService
from src.utils.decorators import auth_required

bp = Blueprint("metrics", __name__, url_prefix="/metrics")
metrics_service = MetricsService()

def parse_date_qs(value: str):
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(value, fmt)
        except Exception:
            pass
    return None

@bp.route("", methods=["GET"])
@auth_required
def list_metrics():
    q = request.args
    start_date = parse_date_qs(q.get("start_date"))
    end_date = parse_date_qs(q.get("end_date"))
    sort_by = q.get("sort_by")
    order = q.get("order", "asc")
    page = int(q.get("page", 1))
    per_page = int(q.get("per_page", 100))

    try:
        metrics = metrics_service.list_metrics(
            start_date=start_date,
            end_date=end_date,
            sort_by=sort_by,
            order=order,
            page=page,
            per_page=per_page
        )
    except ValueError as exc:
        return jsonify({"message": str(exc)}), 400

    user_payload = getattr(g, "user", {})
    role = user_payload.get("role", "user")
    include_cost = (role.lower() == "admin")

    data = [m.to_dict(include_cost=include_cost) for m in metrics]
    return jsonify({"items": data, "count": len(data)})
