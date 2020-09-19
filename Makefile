PI_IP_ADDRESS=10.0.0.88

.PHONY: copy
copy:
	@scp -r ./app pi@$(PI_IP_ADDRESS):/home/pi/
