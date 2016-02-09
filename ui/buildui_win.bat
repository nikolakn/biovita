@echo on
call "C:/Python27/Lib/site-packages/PyQt4/pyuic4.bat" -o UiRucne.py rucnewindow.ui

call "C:/Python27/Lib/site-packages/PyQt4/pyuic4.bat" -o UiAuto.py automainwindow.ui 

call "C:/Python27/Lib/site-packages/PyQt4/pyuic4.bat" -o UiDialog1.py dialog1.ui 

call "C:/Python27/Lib/site-packages/PyQt4/pyuic4.bat" -o UiDialogBin.py dialogbin.ui 

call "C:/Python27/Lib/site-packages/PyQt4/pyuic4.bat" -o UiDialogGotove.py gotove.ui

call "C:/Python27/Lib/site-packages/PyQt4/pyuic4.bat" -o UiDialogRecepture.py recepture.ui