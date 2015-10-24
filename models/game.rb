
class Game
  include DataMapper::Resource

  property :id,         Serial
  property :away_score,  Integer
  property :home_score,  Integer
  property :game_date, DateTime
  belongs_to :away_team, :model => Team
  belongs_to :home_team, :model => Team
end
