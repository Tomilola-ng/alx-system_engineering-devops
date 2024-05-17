# 0-the_sky_is_the_limit_not.pp
# Configure Nginx to handle more concurrent connections

exec { 'LIMIT_EDITING':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && \
              sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:\
              /sbin:/bin:/usr/games:/usr/local/games',
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and will be restarted if config changes
service { 'nginx':
  ensure => running,
  enable => true,
}
