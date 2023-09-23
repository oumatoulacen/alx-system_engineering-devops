file { '/etc/ssh/ssh_config':
	ensure => present,
	content => "
	# SSH client configuration
	Host *
	  IdentityFile ~/.shh/school
	  PasswordAuthentication no
	",
}
