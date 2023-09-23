file { '/etc/ssh/ssh_config':
	ensure => 'file',
	content => "
	# SSH client configuration
	Host *
	  IdentityFile ~/.ssh/school
	  PasswordAuthentication no
	",
}
