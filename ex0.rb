#!/usr/local/bin/ruby

require 'net/http'

uri = URI('http://pragmaticcrypto.herokuapp.com/exercise0/')
dict = IO.readlines('john.txt')
dict.each{|p|
  response = Net::HTTP.post_form(uri, 'password' => p.chomp)
  puts p
  puts response
}
