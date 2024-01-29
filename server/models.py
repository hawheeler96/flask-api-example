from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class Attendee(db.Model, SerializerMixin):
    __tablename__ = "attendees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    rsvps = db.Relationship(
        "RSVP", back_populates="attendee", cascade="all, delete-orphan"
    )
    event = association_proxy("rsvps", "event")

    serialize_rules = ("-rsvps",)

    def __repr__(self):
        return f"<Attendee {self.id}: {self.name}>"


class Event(db.Model, SerializerMixin):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.DateTime)

    rsvps = db.Relationship(
        "RSVP", back_populates="event", cascade="all, delete-orphan"
    )
    attendee = association_proxy("rsvps", "attendee")

    serialize_rules = ("-rsvps",)

    def __repr__(self):
        return f"<Event {self.id}: {self.name}, {self.date}>"


class RSVP(db.Model, SerializerMixin):
    __tablename__ = "rsvps"

    id = db.Column(db.Integer, primary_key=True)
    attendee_id = db.Column(db.Integer, db.ForeignKey("attendees.id"))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))

    attendee = db.Relationship("Attendee", back_populates="rsvps")
    event = db.Relationship("Event", back_populates="rsvps")

    serialize_rules = ("-attendee", "-event")

    def __repr__(self):
        return f"<RSVP {self.id}>"
