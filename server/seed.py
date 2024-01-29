from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Attendee, Event, RSVP

fake = Faker()


def create_events():
    events = []
    for _ in range(10):
        e = Event(name=fake.sentence(), time=rc(range(24)))
        events.append(e)

    return events


def create_attendees():
    attendees = []
    for _ in range(5):
        a = Attendee(name=fake.name())
        attendees.append(a)

    return attendees


def create_rsvps(events, attendees):
    rsvps = []
    for _ in range(20):
        r = RSVP(
            attendee_id=rc([attendee.id for attendee in attendees]),
            events_id=rc([event.id for event in events]),
        )
        rsvps.append(r)

    return rsvps


if __name__ == "__main__":
    with app.app_context():
        print("Clearing db...")
        Event.query.delete()
        RSVP.query.delete()
        Attendee.query.delete()

        print("Seeding events...")
        events = create_events()
        db.session.add_all(events)
        db.session.commit()

        print("Seeding attendees...")
        attendees = create_attendees()
        db.session.add_all(attendees)
        db.session.commit()

        print("Seeding rsvps...")
        rsvps = create_rsvps(events, attendees)
        db.session.add_all(rsvps)
        db.session.commit()

        print("Done seeding!")
