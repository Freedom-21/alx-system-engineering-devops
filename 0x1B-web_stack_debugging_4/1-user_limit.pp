# Manifest to increase file limits of the user
exec { 'set file limits for holberton user':
  command => "echo 'holberton soft nofile 4096\nholberton hard nofile 4096' >> /etc/security/limits.conf",
  unless  => "grep -q 'holberton soft nofile 4096' /etc/security/limits.conf",
  path    => '/bin',
}

