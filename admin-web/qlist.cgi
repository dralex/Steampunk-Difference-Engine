#!/usr/bin/ruby
# ----------------------------------------------------------------------------
require 'web'
require 'directory'
# ----------------------------------------------------------------------------
unless $cgi.has_key? 'dir'
	Output.error
	puts 'Не указана директория'
	exit 0
end
# ----------------------------------------------------------------------------
unless $cgi.has_key? 'field'
	Output.error
	puts 'Не указано поле запроса'
	exit 0
end
# ----------------------------------------------------------------------------
unless $cgi.has_key? 'value'
	Output.error
	puts 'Не указано поле значения'
	exit 0
end
# ----------------------------------------------------------------------------
directory = Directory.create $cgi['dir']
if directory.nil?
	Output.error
	puts "Неверная директория #{$cgi['dir']}"
	exit 0	
end
# ----------------------------------------------------------------------------
Output.start
directory.query_list($cgi['field'],$cgi['value'])
Output.finish
# ----------------------------------------------------------------------------
