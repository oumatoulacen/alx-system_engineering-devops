file { '/home/ubuntu/.ssh/ssh_config':
	ensure => 'file',
	owner => 'ubuntu',
	group => 'ubuntu',
	mode => '0744',
	content => "
		host 100.25.163.174
		IdentityFile ~/.shh/school
		PasswordAuthentication no
	"
}
