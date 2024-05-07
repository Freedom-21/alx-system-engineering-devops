#!/usr/bin/env ruby
# regex for matching character starts with "hb" + 2-5 't's then n
puts ARGV[0].scan(/hbt{2-5}n/).join
