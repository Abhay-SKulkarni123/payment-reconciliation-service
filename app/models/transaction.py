from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base
from app.enums import PaymentStatus, SettlementStatus


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)

    transaction_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    merchant_id = Column(
        Integer,
        ForeignKey("merchants.id"),
        nullable=False,
        index=True,
    )

    amount = Column(
        Numeric(12, 2),
        nullable=False,
    )

    currency = Column(
        String(3),
        nullable=False,
    )

    payment_status = Column(
        Enum(PaymentStatus),
        nullable=False,
        default=PaymentStatus.INITIATED,
        index=True,
    )

    settlement_status = Column(
        Enum(SettlementStatus),
        nullable=False,
        default=SettlementStatus.PENDING,
        index=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    merchant = relationship(
        "Merchant",
        back_populates="transactions",
    )

    events = relationship(
        "PaymentEvent",
        back_populates="transaction",
        cascade="all, delete-orphan",
        order_by="PaymentEvent.event_timestamp",
    )