"""
Specifies the execution policy to set. Common policy names include:
Restricted: (Default) No scripts can be run.
AllSigned: Requires all scripts and configuration files to be signed by a trusted publisher.
RemoteSigned: Allows local scripts to run without a signature, but requires digitally signed scripts downloaded from the internet.
Unrestricted: Allows all scripts to run, but prompts for permission before running unsigned scripts downloaded from the internet.
Bypass: Nothing is blocked and no warnings or prompts are issued.
Undefined: Removes the currently set execution policy from the specified scope.
"""