all:
	cp -v ver.py /bin/ver
	chmod +x /bin/ver
	msgfmt ./po/messages.po
	cp -v ./messages.mo /usr/share/locale/ru/LC_MESSAGES/ver.mo
	
remove:
	rm -rv /bin/ver /usr/share/locale/ru/LC_MESSAGES/ver.mo

clean:
	rm -rv messages.mo
