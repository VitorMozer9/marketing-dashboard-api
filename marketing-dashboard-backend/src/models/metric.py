from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class Metric:
    account_id: str
    campaign_id: str
    cost_micros: Optional[float]
    clicks: Optional[float]
    conversions: Optional[float]
    impressions: Optional[float]
    interactions: Optional[float]
    date: datetime

    def to_dict(self, include_cost: bool = True) -> Dict[str, Any]:
        date_value = (
            self.date.strftime("%Y-%m-%d")
            if isinstance(self.date, datetime)
            else (str(self.date) if self.date is not None else None)
        )

        return {
            "account_id": self.account_id,
            "campaign_id": self.campaign_id,
            "cost_micros": (self.cost_micros if include_cost else None),
            "clicks": self.clicks,
            "conversions": self.conversions,
            "impressions": self.impressions,
            "interactions": self.interactions,
            "date": date_value,
        }
