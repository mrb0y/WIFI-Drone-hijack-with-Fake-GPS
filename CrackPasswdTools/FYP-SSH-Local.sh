clear

#$filevar = 'HashCatOfficialWebsite.hccapx'
#scp -P 80 $filevar $(grep SSHUser SystemInformation.txt |awk {'print $2'})@$(grep SSHIp SystemInformation.txt |awk {'print $2'}):/home/$(grep SSHUser SystemInformation.txt |awk {'print $2'})/Desktop #Uplaod file to remote server.
#new one
sshpass -p $(grep SSHPassword SystemInformation.txt |awk {'print $2'}) scp -P 80 CrackPasswdTools/HashCatOfficialWebsite.hccapx $(grep SSHUser SystemInformation.txt |awk {'print $2'})@$(grep SSHIp SystemInformation.txt |awk {'print $2'}):/home/$(grep SSHUser SystemInformation.txt |awk {'print $2'})/Desktop

sshpass -p $(grep SSHPassword SystemInformation.txt |awk {'print $2'}) ssh -p 80 $(grep SSHUser SystemInformation.txt |awk {'print $2'})@$(grep SSHIp SystemInformation.txt |awk {'print $2'}) "echo "" && cd Desktop && echo "" && ls && echo "" && pwd && echo "" && ./FYP-SSH-Server.sh"

