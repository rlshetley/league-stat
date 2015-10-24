class Player
  include DataMapper::Resource

  property :id,         Serial
  property :first_name, String
  property :last_name,  String

  has n, :family_member, :through => Resource
  has n, :team, :through => Resource
end
