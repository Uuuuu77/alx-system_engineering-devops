# Ensure that the holberton user exists

user { 'holberton':
  ensure => present,
}

# Set file descriptor limits for the holberton user
file { '/etc/security/limits.d/holberton_limits.conf':
  ensure  => present,
  content => "holberton hard nofile 65536\nholberton soft nofile 65536\n",
  require => User['holberton'],
}

# Reload PAM to apply the changes immediately
exec { 'reload_pam':
  command => 'pam_tally2 --reset --user holberton',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  require => File['/etc/security/limits.d/holberton_limits.conf'],
}
