#!/bin/bash
##
## Initialize college pc's for use with git
##

git config user.name "krava322"
git config user.email "serhiikravchuk2000@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
git pull

echo
echo ~~~~~~~
echo "Done!"
echo ~~~~~~~
echo