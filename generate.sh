for name in *.ui
do
	pyuic5 $name -o Ui_${name%%.ui}.py
done
