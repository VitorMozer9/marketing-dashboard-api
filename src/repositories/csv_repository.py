import csv
from datetime import datetime
from typing import List
from src.models.users import Users
from src.models.metric import Metric
from src import config


def load_users_from_csv(path: str = None) -> List[Users]:
    path = path or config.USERS_CSV_PATH
    users = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(Users(
                id=row.get("id") or row.get("user_id") or "",
                email=row.get("email", "").strip(),
                password=row.get("password", "").strip(),
                role=row.get("role", "user").strip()
            ))
    return users


def parse_int(value):
    try:
        return int(value)
    except Exception:
        return None


def parse_date(value):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(value, fmt)
        except Exception:
            continue
    return None


def load_metrics_from_csv(path: str = None) -> List[Metric]:
    path = path or config.METRICS_CSV_PATH
    metric_list = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = parse_date(row.get("date", "")) or parse_date(row.get("day", ""))
            metric_list.append(Metric(
                account_id=row.get("account_id") or row.get("account", ""),
                campaign_id=row.get("campaign_id", ""),
                cost_micros=parse_int(row.get("cost_micros", "")),
                clicks=parse_int(row.get("clicks", "")),
                conversions=parse_int(row.get("conversions", "")),
                impressions=parse_int(row.get("impressions", "")),
                interactions=parse_int(row.get("interactions", "")),
                date=date
            ))
    return [metric for metric in metric_list if metric.date is not None]
