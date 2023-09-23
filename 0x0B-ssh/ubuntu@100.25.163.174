file { '/home/ubuntu/.ssh/ssh_config':
	ensure => 'file',
	owner => 'ubuntu',
	group => 'ubuntu',
	mode => '0600',
	content => "
	host 100.25.163.174
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	PreferredAuthentications publickey
	User ubuntu
	",
}
