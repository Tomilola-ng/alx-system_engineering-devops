#!/usr/bin/env ruby

par = ARGV[0].scan(/flags:(.*?)\]/)
add = ARGV[0].scan(/from:(.*?)\]/)
st = ARGV[0].scan(/to:(.*?)\]/)
puts [add, st, par].join(',')
