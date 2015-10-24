
class GamePlayerHittingStat
  include DataMapper::Resource

  property :id,         Serial
  property :at_bats, Integer
  property :hits, Integer
  property :runs, Integer
  property :walks, Integer
  property :singles, Integer
  property :doubles, Integer
  property :triples, Integer
  property :home_runs, Integer
  belongs_to :game
  belongs_to :player
end
