get '/api/games/:id' do
  game ||= Game.get(params[:id]) || halt(404)
  return game.to_json
end

get '/api/games/:id/batting_stats' do
  stats = GamePlayerHittingStat.all(:game_id => params[:id])

  return stats.to_json
end

get '/api/games/:id/pitching_stats' do
  stats = GamePlayerPitchingStat.all(:game_id => params[:id])

  return stats.to_json
end
