# PUPPET CODE

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

# LOOKS LIKE DEVOPS
package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

# LOOKS LIKE DEVOPS
file {'/var/www/html/index.html':
	content => 'Hello World!'
}

# LOOKS LIKE DEVOPS
exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# LOOKS LIKE DEVOPS
service {'nginx':
	ensure => running,
	require => Package['nginx']
}