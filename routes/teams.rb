get '/api/teams' do
  return Team.all.to_json
end

get '/api/teams/:id' do
  team ||= Team.get(params[:id]) || halt(404)
  return team.to_json
end

get '/api/teams/:id/players' do
  team ||= Team.get(params[:id]) || halt(404)
  return team.player.to_json
end

get '/api/teams/:id/coaches' do
  team ||= Team.get(params[:id]) || halt(404)
  return team.coach.to_json
end

get '/api/teams/:id/games' do
  games = Game.all(:home_team_id => params[:id]) | Game.all(:away_team_id => params[:id])
  return games.to_json
end
