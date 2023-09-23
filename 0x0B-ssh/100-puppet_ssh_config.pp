file { '/home/ubuntu/.ssh/ssh_config':
	ensure => 'file',
	owner => 'ubuntu',
	content => "
		# SSH client configuration
		Host *
		IdentityFile ~/.shh/school
		PasswordAuthentication no
	"
}
