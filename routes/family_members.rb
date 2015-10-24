get '/api/family_members' do
  return FamilyMember.all.to_json
end

get '/api/family_members/:id' do
  family_member ||= FamilyMember.get(params[:id]) || halt(404)
  return family_member.to_json
end

post '/api/family_members' do
  body = JSON.parse request.body.read
  family_member = FamilyMember.create(
    first_name: body['first_name'],
    last_name: body['last_name']
  )
  status 201
  return family_member.to_json
end
