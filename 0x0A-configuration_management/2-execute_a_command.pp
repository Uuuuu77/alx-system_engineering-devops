# Executing pkill command.

exec { 'killmenow':
  path    => '/usr/bin',
  command => 'pkill killmenow',
}
