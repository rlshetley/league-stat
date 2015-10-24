
class League
  include DataMapper::Resource

  property :id,         Serial
  property :name,       String

  has n, :team
end
