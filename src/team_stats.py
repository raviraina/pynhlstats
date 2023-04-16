from request_processor import NhlApiRequestProcessor


class Teams:
    def __init__(self, refresh=False):
        self.req = "/api/v1/teams"
        self.endpoint = NhlApiRequestProcessor()
        self.refresh = refresh

        self.team_data = self.endpoint.request(self.req, "team_data", self.refresh)
        self.abv_to_id_endpoints = {
            team["abbreviation"]: {"id": team["id"], "endpoint": team["link"]}
            for team in self.team_data["teams"]
        }

    def get_all_team_info(self) -> dict:
        return self.team_data

    def get_abv_to_id_endpoints_map(self) -> dict:
        return self.abv_to_id_endpoints

    def get_team_roster(
        self,
        abv_name: str,
    ) -> dict:

        try:
            req = f"{self.abv_to_id_endpoints[abv_name]['endpoint']}/roster"
            res = self.endpoint.request(req, f"rosters/{abv_name}_roster", self.refresh)
        except:
            raise Exception("Couldn't get roster")

        return res

    def get_abv_to_players_map(self) -> dict:
        team_players_mp = {}

        for team in [k for k in self.get_abv_to_id_endpoints_map()]:
            players = self.get_team_roster(team)
            team_players_mp[team] = [
                player["person"]["fullName"] for player in players["roster"]
            ]
        return team_players_mp
