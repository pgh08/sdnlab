#!/bin/zsh

echo "Creating linear,4 topology"
sudo mn --topo linear,4
echo -e "pingall all hosts"
pingall
