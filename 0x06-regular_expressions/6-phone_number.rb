#!/usr/bin/env ruby
# This regex matches a string that is 10 digits long
puts ARGV[0].scan(/^\d{10}$/).join

