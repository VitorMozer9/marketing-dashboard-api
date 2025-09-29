from typing import List, Optional
from datetime import datetime
from src.repositories.csv_repository import load_metrics_from_csv
from src.models.metric import Metric


class MetricsService:
    def __init__(self, metrics_path: str = None):
        self._metrics = load_metrics_from_csv(metrics_path)

    def list_metrics(self,
                     start_date: Optional[datetime] = None,
                     end_date: Optional[datetime] = None,
                     sort_by: Optional[str] = None,
                     order: str = "asc",
                     page: int = 1,
                     per_page: int = 100) -> List[Metric]:

        results = self._metrics

        if start_date:
            results = [m for m in results if m.date.date() >= start_date.date()]
        if end_date:
            results = [m for m in results if m.date.date() <= end_date.date()]

        if sort_by:
            valid_sort_fields = {
                "date",
                "account_id",
                "campaign_id",
                "impressions",
                "clicks",
                "conversions",
                "interactions",
                "cost_micros"
            }
            if sort_by not in valid_sort_fields:
                raise ValueError(f"invalid sort_by: {sort_by}")

            results.sort(
                key=lambda m: (getattr(m, sort_by) is None, getattr(m, sort_by)),
                reverse=(order == "desc")
            )

        start = (page - 1) * per_page
        end = start + per_page
        return results[start:end]
