#!/usr/bin/env ruby
# regex matches a string that starts with 'h', ends with 'n', and has exactly one character in between
puts ARGV[0].scan(/^h.n$/).join

