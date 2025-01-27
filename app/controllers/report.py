from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers import ReportManager


class ReportController:
    manager = ReportManager

    @classmethod
    def get_report(cls) -> Tuple[Any, Optional[str]]:
        try:
            report = cls.manager.get_report()
            return report, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
