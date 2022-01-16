help:
	targets: install, remove
	         status

services_implementation := hw_button_scan

systemd_config_files := hw_button_scan.service

install_hw_button_scan: | hw_button_scan.service hw_button_scan.py
	install -p -T hw_button_scan.service -t /etc/systemd/service
	systemctl enable hw_button_scan.service
	systemctl start hw_button_scan.service
