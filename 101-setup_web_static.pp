# Puppet for setup -- redoing task 0 but wiz puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
}

-> package { 'nginx':
  ensure => installed,
}

-> file { '/data/web_static/releases/test/index.html':
  content => 'Test Page',
  group   => 'ubuntu',
  owner   => 'ubuntu',
}

-> file { ['/data/', '/data/web_static', '/data/web_static/releases/', '/data/web_static/releases/test', '/data/web_static/shared' ]:
  ensure => 'directory',
  group  => 'ubuntu',
  owner  => 'ubuntu',
}

-> file { '/data/web_static/current':
  ensure => symlink,
  target => '/usr/bin/env sed -i "/listen80 default_server/a location \
/hbnb_static/ { alias /data/web_static/current/;}" \
/etc/nginx/sites-enabled/default',
}

-> run { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
