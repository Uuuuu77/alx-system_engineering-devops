# Installing and configuring nginx server.

exec { 'install config nginx':
  provider => shell,
  command  => 'apt-get -y update ; apt-get -y install nginx ; echo "Hello World!" > /var/www/html/index.html ; service nginx start ; sed -i "25i location /redirect_me {\n return 301 https://www.youtube.com/watch?v=v5nfmtFzvvk;\n}\n" /etc/nginx/sites-available/default ; service nginx restart',
}
