from sqlalchemy import JSON
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import Base
from app.enums import EventType


class PaymentEvent(Base):
    __tablename__ = "payment_events"

    id = Column(
        Integer,
        primary_key=True,
    )

    event_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    transaction_pk = Column(
        Integer,
        ForeignKey("transactions.id"),
        nullable=False,
        index=True,
    )

    transaction = relationship(
        "Transaction",
        back_populates="events",
    )

    external_transaction_id = Column(
        String,
        nullable=False,
        index=True,
    )

    merchant_id = Column(
        Integer,
        ForeignKey("merchants.id"),
        nullable=False,
        index=True,
    )

    external_merchant_id = Column(
        String,
        nullable=False,
        index=True,
    )

    event_type = Column(
        Enum(EventType),
        nullable=False,
    )

    event_timestamp = Column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    raw_payload = Column(
        JSON,
        nullable=True,
    )

    merchant = relationship(
        "Merchant",
    )