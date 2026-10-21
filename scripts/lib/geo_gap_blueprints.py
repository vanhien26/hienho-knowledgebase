"""Consolidated GEO Gap Blueprints for all 161 themes"""

from scripts.lib.gaps.insurtech import INSURTECH_GAPS
from scripts.lib.gaps.vehicle import VEHICLE_GAPS
from scripts.lib.gaps.ota import OTA_GAPS
from scripts.lib.gaps.student import STUDENT_GAPS
from scripts.lib.gaps.telco import TELCO_GAPS
from scripts.lib.gaps.entertainment_cinema import ENTERTAINMENT_CINEMA_GAPS
from scripts.lib.gaps.health_lottery_other import HEALTH_LOTTERY_OTHER_GAPS
from scripts.lib.gaps.financial import FINANCIAL_GAPS

GEO_GAP_BLUEPRINTS = {}

for module_gaps in [
    INSURTECH_GAPS,
    VEHICLE_GAPS,
    OTA_GAPS,
    STUDENT_GAPS,
    TELCO_GAPS,
    ENTERTAINMENT_CINEMA_GAPS,
    HEALTH_LOTTERY_OTHER_GAPS,
    FINANCIAL_GAPS
]:
    GEO_GAP_BLUEPRINTS.update(module_gaps)
