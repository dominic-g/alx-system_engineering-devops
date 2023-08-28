# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.

include stdlib

file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}

# Explanation of the regex match
#
# ^  start of the line
# [#]* one or more hash character
# [\s]*  any white space characters
# (?i)IdentityFile caseinsensitive match phrase "IdentityFile"
# [\s]+ at least one whitespace character
# ~/.ssh/id_rsa path to ssh private key we intend to replace
# $      end of the line

file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}

# Explanation of the regex match
#
# ^       start of the line
# [#]*  one ir more hash character
# [\s]*  any white space characters
# (?i)PasswordAuthentication case insensitive match
# [\s]+ at least one whitespace character
# (yes|no) enum value "yes" or the value "no"
# $      end of the line
