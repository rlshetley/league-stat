get '/api/coaches' do
  return Coach.all.to_json
end

get '/api/coaches/:id' do
  coach ||= Coach.get(params[:id]) || halt(404)
  return coach.to_json
end

post '/api/coaches' do
  body = JSON.parse request.body.read
  coach = Coach.create(
    first_name: body['first_name'],
    last_name: body['last_name']
  )
  status 201
  return coach.to_json
end
