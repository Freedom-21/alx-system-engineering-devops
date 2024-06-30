# puppet manifest that kills process named 'killmenow'
exec { 'kill_killmenow_process':
    command => 'pkill killmenow',
    path    => ['/bin', '/usr/bin', '/usr/sbin'],
    onlyif  => 'pgrep killmenow',
}