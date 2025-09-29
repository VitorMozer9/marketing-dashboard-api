from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class Metric:
    account_id: str
    campaign_id: str
    cost_micros: Optional[int]
    clicks: Optional[int]
    conversions: Optional[int]
    impressions: Optional[int]
    interactions: Optional[int]
    date: datetime

    def to_dict(self, include_cost: bool = True) -> Dict[str, Any]:
        base = {
            "account_id": self.account_id,
            "campaign_id": self.campaign_id,
            "clicks": self.clicks,
            "conversions": self.conversions,
            "impressions": self.impressions,
            "interactions": self.interactions,
            "date": self.date.strftime("%Y-%m-%d")
        }
        if include_cost:
            base["cost_micros"] = self.cost_micros
        return base
