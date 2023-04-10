#!/bin/bash

project_dir=$(pwd)

cat > /etc/systemd/system/shimla.service <<EOF
[Unit]
Description=My Django Project
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=$project_dir
ExecStart=/usr/bin/python3 $project_dir/manage.py runserver 0.0.0.0:7077
Restart=always

[Install]
WantedBy=multi-user.target
EOF

echo "Service file created and updated at /etc/systemd/system/shimla.service"