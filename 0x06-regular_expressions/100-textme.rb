#!/usr/bin/env ruby
Array = ARGV[0].scan(/from:(\+?[a-zA-Z0-9]+)|to:(\+?[a-zA-Z0-9]+)|flags:([0-1\-:]+)/).join(" ")
Array_List = Array.split
puts Array_List.join(",")
