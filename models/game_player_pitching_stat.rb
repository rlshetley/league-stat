
class GamePlayerPitchingStat
  include DataMapper::Resource

  property :id,         Serial
  property :hits, Integer
  property :runs, Integer
  property :walks, Integer
  property :strikeouts, Integer
  property :innings_pitched, Integer
  belongs_to :game
  belongs_to :player
end
