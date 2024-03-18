# setup New Ubuntu server with nginx and custom HTTP header

# Update system
exec { 'update system':
        command => '/usr/bin/apt-get update',
}

# Install nginx
package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

# Add custom index.html
file {'/var/www/html/index.html':
	content => 'Hello World!'
}

# Redirect to my linkedin profile
exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://linkedin.com/in/salma-el-maimouni-724a0622a/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Add custom HTTP header
exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Start nginx service
service {'nginx':
	ensure => running,
	require => Package['nginx']
}
