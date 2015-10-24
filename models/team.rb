
class Team
  include DataMapper::Resource

  property :id,         Serial
  property :name,       String

  has n, :player, :through => Resource
  has n, :coach, :through => Resource
  has n, :game
  belongs_to :league
end
