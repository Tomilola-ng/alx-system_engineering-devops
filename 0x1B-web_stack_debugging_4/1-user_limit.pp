# 1-user_limit.pp
# INCREASE LIMIT OF OPEN FILES TO DANGEROUSLY HIGH

exec { 'CONF FOR HARD FILE':
  command => 'sed -i "/holberton hard/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx']
}

exec { 'CONF FOR SOFT FILE':
  command => 'sed -i "/holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx']
}

# Ensure Nginx service is running and will be restarted if config changes
service { 'nginx':
  ensure => running,
  enable => true,
}
