from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base

class BusinessModel(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    industry = Column(String)
    location = Column(String)

    owner = relationship("UserModel", back_populates="businesses")
    listings = relationship("BusinessListingModel", back_populates="business")