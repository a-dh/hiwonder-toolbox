help:
	@echo targets: install remove

services_implementation := hw_button_scan

systemd_config_files := hw_button_scan.service

install: install_hw_button_scan
remove: remove_hw_button_scan


.PHONY: install_hw_button_scan remove_hw_button_scan
hw_button_scan.service: hw_button_scan.service.in
	sed -e 's@\$${LOC}@'"$$(dirname $$(realpath hw_button_scan.py))@g" "$<" > "$@"
install_hw_button_scan: hw_button_scan.service hw_button_scan.py
	install --mode=644 --target-directory /etc/systemd/system hw_button_scan.service 
	systemctl enable hw_button_scan.service
	systemctl start hw_button_scan.service
remove_hw_button_scan: 
	systemctl stop hw_button_scan.service
	systemctl stop hw_button_scan.service
	rm /etc/systemd/system/hw_button_scan.service
