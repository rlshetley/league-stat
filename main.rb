# encoding: UTF-8
require 'json'
require 'sinatra'
require 'data_mapper'
require 'dm-migrations'

require './models/init'
require './routes/init'

DataMapper.setup(:default, "mysql://lsuser:lsuser@127.0.0.1:3306/league-stat")

DataMapper.finalize.auto_upgrade!
