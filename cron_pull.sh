#!/bin/bash
cd /home/cdaugherty/website
git pull origin master
systemctl restart nginx.service
systemctl restart website.service
