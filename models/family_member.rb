

class FamilyMember
  include DataMapper::Resource

  property :id,         Serial
  property :first_name, String
  property :last_name,  String

  has n, :player, :through => Resource
end
