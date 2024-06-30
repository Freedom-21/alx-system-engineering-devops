# Puppet manifest to configure SSH client

file { '/home/ubuntu/.ssh':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => @("EOF")
Host ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
| EOF
  require => File['/home/ubuntu/.ssh'],
}
