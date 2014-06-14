#Set up the paths
Exec {path => '/usr/bin:/usr/sbin/:/bin:/sbin' }
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}
# Ensure update runs before installing pacakges
Exec['apt-get-update'] -> Package <| |>


class { 'docker':
  tcp_bind    => 'tcp://127.0.0.1:4243',
  socket_bind => 'unix:///var/run/docker.sock',
}

exec {'curl -L https://github.com/orchardup/fig/releases/download/0.4.1/linux > /usr/local/bin/fig':
}
->
exec {'chmod +x /usr/local/bin/fig':
}
