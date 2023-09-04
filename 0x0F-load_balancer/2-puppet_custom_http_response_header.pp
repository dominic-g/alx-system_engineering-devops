# Update system package repositories
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package and ensure it depends on system update
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# Create the Hello World HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Add a redirect rule to the Nginx configuration
exec { 'add_redirect_rule':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Add a custom HTTP header to the Nginx configuration
exec { 'add_custom_header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Ensure the Nginx service is running and depends on the Nginx package
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}

