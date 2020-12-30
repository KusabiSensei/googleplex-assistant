#!/bin/sh

############################################################
#                                                          #
#         googleplex-assistant startup script              #
#                                                          #
############################################################

check_dns_for_existing_entry() {
  existingip=$(dig +short "$1")
}

map_dns_to_external_ip() {
  true
}

get_external_ip() {
  if [ -f /usr/bin/external-ip ] && [ -x /usr/bin/external-ip ]; then
    externalip=$(external-ip)
  else
    externalip="Cannot Determine External IP"
  fi
}

get_internal_ip () {
  internalip=$(hostname -i | awk '{print $1}')
}

echo "Now starting googleplex-assistant..."
echo "Setting up DNS..."
get_external_ip "$externalip"
get_internal_ip "$internalip"
hostname="$1"
check_dns_for_existing_entry "$hostname" "$existingip"
echo "The current IP for $hostname is $existingip"
echo "The currently detected external IP is $externalip"
map_dns_to_external_ip "$hostname" "$ip"

# Generate Let's Encrypt Certificate
acme.sh --staging --issue --dns dns_aws -d "$hostname"
cp /root/.acme.sh/googleplex.dickerson.io/fullchain.cer /app/app.cer
cp /root/.acme.sh/googleplex.dickerson.io/googleplex.dickerson.io.key /app/app.key
echo "Certificate is in /app/app.cer and the key is in /app/app.key"

# Setup nginx's run dir for pid and lockfiles so it will run
mkdir /run/nginx

#pipenv run uwsgi -s /tmp/googleplex.sock --manage-script-name --mount /=googleplex_assistant:application


