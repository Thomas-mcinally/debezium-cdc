import uuid

import sqlalchemy as db
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Company(Base):
    __tablename__ = "company"

    id: Mapped[uuid.UUID] = mapped_column(
        db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    companies_house_number: Mapped[str] = mapped_column(db.String)
