from flask import make_response, request
from flask.views import MethodView
from flask.json import jsonify
from api import db, register_controller
from api.models import League
import json


class LeagueController(MethodView):
    def get(self, league_id):
        league = League.query.filter(League.id == league_id).first()

        if league is None:
            return make_response('', 404)

        resp = jsonify(league.serialize())
        resp.status_code = 200

        return resp

    def put(self, league_id):
        league = League.query.filter(League.id == league_id).first()

        league.name = request.json_data['name']

        resp = jsonify(league.serialize())
        resp.status_code = 201

        return resp

    def delete(self, league_id):
        league = League.query.filter(League.id == league_id).first()

        db.session.delete(league)
        db.session.commit()

        return make_response('', 204)


class LeagueListController(MethodView):
    def get(self):
        results = [i.serialize() for i in League.query.all()]
        resp = jsonify(leagues=results)
        resp.status_code = 200
        return resp

    def post(self):
        league = League()

        league.name = request.json_data['name']

        db.session.add(league)
        db.session.commit()

        resp = jsonify(league.serialize())
        resp.status_code = 201

        return resp

register_controller(LeagueController, 'league_api', '/leagues/<int:league_id>/')
register_controller(LeagueListController, 'league_list_api', '/leagues/', ['GET', 'POST'])
