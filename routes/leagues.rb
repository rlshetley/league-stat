get '/api/leagues' do
  return League.all.to_json
end

get '/api/leagues/:id' do
  league ||= League.get(params[:id]) || halt(404)
  return league.to_json
end

get '/api/leagues/:id/teams' do
  league ||= League.get(params[:id]) || halt(404)
  return league.team.to_json
end

post '/api/leagues' do
  body = JSON.parse request.body.read
  league = League.create(
    name: body['name']
  )
  status 201
  return league.to_json
end
