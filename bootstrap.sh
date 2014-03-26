#!/usr/bin/env bash

apt-get update
printf "vagrant ALL=(scipy) NOPASSWD: ALL\n" >> /etc/sudoers
