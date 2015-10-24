
get '/api/players' do
  return Player.all.to_json
end

get '/api/players/:id' do
  player ||= Player.get(params[:id]) || halt(404)
  return player.to_json
end

post '/api/players' do
  body = JSON.parse request.body.read
  player = Player.create(
    first_name: body['first_name'],
    last_name: body['last_name']
  )
  status 201
  return player.to_json
end
