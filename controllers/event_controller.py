from flask import Blueprint, request, redirect 
from flask import render_template
from models.event_list import events, add_new_event
from models.event import Event

event_blueprint = Blueprint("events", __name__)

@event_blueprint.route("/events")
def index():
    return render_template("index.jinja", title = "My Events", events=events)

@event_blueprint.route("/events", methods=["POST"])
def add_event():
    date = request.form["date"]
    name = request.form["name"]
    number_of_guests = request.form["number_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    recurring = request.form["recurring"]
    new_event = Event(date, name, number_of_guests, room_location, description, recurring)
    add_new_event(new_event)
    return redirect("/events")

    