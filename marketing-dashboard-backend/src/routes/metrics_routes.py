from flask import Blueprint, request, jsonify, g
from datetime import datetime
from src.services.metrics_services import MetricsService
from src.utils.decorators import auth_required

bp = Blueprint("metrics", __name__, url_prefix="/metrics")
metrics_service = MetricsService()

def parse_date_qs(value: str):
    if not value:
        return None
    for date_format in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(value, date_format)
        except Exception:
            pass
    return None

@bp.route("", methods=["GET"])
@auth_required
def list_metrics():
    query_params = request.args
    start_date = parse_date_qs(query_params.get("start_date"))
    end_date = parse_date_qs(query_params.get("end_date"))
    sort_by = query_params.get("sort_by")
    order = query_params.get("order", "asc")
    page = int(query_params.get("page", 1))
    per_page = int(query_params.get("per_page", 100))

    try:
        metric_list = metrics_service.list_metrics(
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

    data = [metric .to_dict(include_cost=include_cost) for metric  in metric_list]
    return jsonify({"items": data, "count": len(data)})
