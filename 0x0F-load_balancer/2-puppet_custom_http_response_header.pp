#!/usr/bin/env puppet
# automate the task of creating a custom HTTP header response with Puppet.

exec { 'apt-update':
  command     => 'sudo apt-get -y update',
  provider => shell,
}

exec { 'apt-get':
  command => 'apt-get -y install nginx',
  path    => '/usr/bin:/bin',
  require => Exec['apt-update'],
}

-> exec { 'replace':
  command => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
  provider => shell,
}

-> exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}


