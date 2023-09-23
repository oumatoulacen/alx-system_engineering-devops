file { '/etc/ssh/ssh_config':
	ensure => 'file',
	content => "
	# SSH client configuration
	Host *
	  IdentityFile ~/.shh/school
	  PasswordAuthentication no
	",
}
