

echo "Creating linear, 4 topology"
sudo mn --topo linear,4
echo -e "Pingall all hosts"
pingall
