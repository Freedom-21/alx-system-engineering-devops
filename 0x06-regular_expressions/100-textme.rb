#!/usr/bin/env ruby
# regex for Guillaume Plessis daily task pattern
puts "#{ARGV[0].match(/\[from:(.+?)\]/)[1]},#{ARGV[0].match(/\[to:(.+?)\]/)[1]},#{ARGV[0].match(/\[flags:(.+?)\]/)[1]}"

